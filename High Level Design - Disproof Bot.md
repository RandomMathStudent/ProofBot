# High Level Design - ProofBot

## Objective

Build an AlphaProof-inspired theorem proving system where a language model proposes Lean tactics and Lean verifies them step-by-step.

## Core Loop

1. Select theorem task.
2. Encode current proof state (goal + hypotheses + local context).
3. Model proposes next tactic/action.
4. Lean verifier executes tactic.
5. Receive transition signal:
   - new state,
   - success/failure,
   - solved/not solved.
6. Repeat until solved or step budget is exhausted.

## System Components

### 1) Task & Data Layer
- Source Lean repos + pinned commit hashes.
- Build theorem splits:
  - train set,
  - validation set,
  - held-out test set.
- Store trajectories for replay/training.

### 2) Lean Environment Layer (LeanDojo)
- Loads repository and theorem contexts.
- Provides verifier-backed transitions from action to new state.
- Guarantees formal correctness via Lean kernel.

### 3) Policy Layer
- Base model: code/math-capable LLM.
- Input: serialized Lean state.
- Output: next tactic (or short tactic sequence).

### 4) Training Layer
- Phase A: SFT on successful proof trajectories.
- Phase B (optional): RL / search fine-tuning using verifier feedback.

### 5) Search Layer (optional but important)
- Beam search / best-first search / MCTS over tactics.
- Uses model log-prob + verifier outcomes as score signal.

### 6) Evaluation Layer
- Main metric: theorem pass rate (pass@1, pass@k).
- Secondary metrics:
  - average steps to solve,
  - invalid tactic rate,
  - timeout rate.

## Why LeanDojo Matters

LeanDojo is the execution interface between the policy model and formal proof checking. It turns text generation into a closed-loop decision process with exact correctness feedback.

Without this verifier loop, generated proofs are unverifiable text; with LeanDojo, they become checkable mathematical objects.

## First Deliverable

End-to-end baseline in one Lean repo:
1. Setup repo in LeanDojo.
2. Train small SFT run.
3. Run proving.
4. Save solved/failed statistics.

This is enough to validate plumbing before scaling models or adding RL/search.
