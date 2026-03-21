"""Starter LeanDojo pipeline for ProofBot.

This script separates:
- repository setup
- supervised fine-tuning
- proving/evaluation

It is intentionally simple so you can evolve it into an AlphaProof-style loop.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass
class PipelineConfig:
    model_name: str = "deepseek-ai/DeepSeek-Prover-V2-7B"
    output_dir: str = "outputs-deepseek"
    repo_url: str = "https://github.com/durant42040/lean4-example"
    commit: str = "005de00d03f1aaa32cb2923d5e3cbaf0b954a192"
    epochs_per_repo: int = 1
    batch_size: int = 2
    lr: float = 2e-5
    use_cpu: bool = True
    bf16: bool = False 
    fp16: bool = False
    metrics_path: str = "leandojo_metrics.json"


def build_agent(cfg: PipelineConfig):
    """Create trainer + HF agent."""
    from lean_dojo_v2.agent.hf_agent import HFAgent
    from lean_dojo_v2.trainer.sft_trainer import SFTTrainer

    trainer = SFTTrainer(
    model_name=cfg.model_name,
    output_dir=cfg.output_dir,
    epochs_per_repo=cfg.epochs_per_repo,
    batch_size=cfg.batch_size,
    lr=cfg.lr,
    use_cpu=cfg.use_cpu,
    bf16=cfg.bf16,
    fp16=cfg.fp16,
)
    return HFAgent(trainer=trainer)


def setup_repository(agent: Any, cfg: PipelineConfig) -> None:
    """Pin to one repo + commit to keep experiments reproducible."""
    agent.setup_github_repository(url=cfg.repo_url, commit=cfg.commit)


def run_train(agent: Any) -> None:
    """Run SFT on repository trajectories/tasks."""
    agent.train()


def run_prove(agent: Any) -> Any:
    """Run proof generation. Return raw outputs for later analysis."""
    return agent.prove()


def compute_metrics(raw_output: Any) -> dict[str, Any]:
    """Compute basic metrics from prove() output shape."""
    if raw_output is None:
        return {"num_items": 0, "num_solved": 0, "success_rate": 0.0}

    if isinstance(raw_output, list):
        num_items = len(raw_output)
        solved = 0
        for item in raw_output:
            if isinstance(item, dict):
                solved += int(bool(item.get("success") or item.get("solved")))
        success_rate = (solved / num_items) if num_items else 0.0
        return {
            "num_items": num_items,
            "num_solved": solved,
            "success_rate": success_rate,
        }

    if isinstance(raw_output, dict):
        solved = raw_output.get("num_solved")
        total = raw_output.get("num_items")
        if isinstance(solved, int) and isinstance(total, int) and total > 0:
            return {
                "num_items": total,
                "num_solved": solved,
                "success_rate": solved / total,
            }
        return {"raw_output": raw_output}

    return {"raw_output_type": type(raw_output).__name__}


def write_metrics(cfg: PipelineConfig, metrics: dict[str, Any]) -> None:
    payload = {"config": asdict(cfg), "metrics": metrics}
    Path(cfg.metrics_path).write_text(json.dumps(payload, indent=2), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="ProofBot LeanDojo starter pipeline")
    parser.add_argument(
        "--mode",
        choices=["setup", "train", "prove", "all"],
        default="all",
        help="Pipeline stage to run",
    )
    parser.add_argument("--model-name", default=PipelineConfig.model_name)
    parser.add_argument("--output-dir", default=PipelineConfig.output_dir)
    parser.add_argument("--repo-url", default=PipelineConfig.repo_url)
    parser.add_argument("--commit", default=PipelineConfig.commit)
    parser.add_argument("--epochs-per-repo", type=int, default=PipelineConfig.epochs_per_repo)
    parser.add_argument("--batch-size", type=int, default=PipelineConfig.batch_size)
    parser.add_argument("--lr", type=float, default=PipelineConfig.lr)
    parser.add_argument("--use-cpu", action="store_true", default=PipelineConfig.use_cpu)
    parser.add_argument("--metrics-path", default=PipelineConfig.metrics_path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = PipelineConfig(
        model_name=args.model_name,
        output_dir=args.output_dir,
        repo_url=args.repo_url,
        commit=args.commit,
        epochs_per_repo=args.epochs_per_repo,
        batch_size=args.batch_size,
        lr=args.lr,
        use_cpu=args.use_cpu,
        metrics_path=args.metrics_path,
    )

    agent = build_agent(cfg)

    if args.mode in {"setup", "train", "prove", "all"}:
        setup_repository(agent, cfg)
    if args.mode in {"train", "all"}:
        run_train(agent)
    if args.mode in {"prove", "all"}:
        raw_output = run_prove(agent)
        metrics = compute_metrics(raw_output)
        write_metrics(cfg, metrics)
        print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
