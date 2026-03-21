# LeanDojo in ProofBot

This folder is your LeanDojo integration layer.

For an AlphaProof-like system, LeanDojo is the bridge between:
- your model (which proposes tactics),
- and Lean (which verifies each tactic exactly).

## What LeanDojo Does

LeanDojo gives you programmatic access to theorem proving tasks in Lean repositories. In practice, it lets your agent:
1. Load Lean files/theorems from a target repo + commit.
2. Observe proof state (goals, hypotheses, context).
3. Propose the next tactic/action.
4. Get immediate verifier feedback from Lean (`success`/`failure`, new state).

That verifier feedback is the key loop used by systems like AlphaProof.

## AlphaProof-Style Mapping

Use this mental model for ProofBot:

1. `Task Source`  
   Choose theorem tasks (from curated Lean repos).

2. `Policy Model`  
   Model predicts next tactic tokens from current proof state.

3. `Verifier (Lean via LeanDojo)`  
   Executes tactic and returns exact state transition.

4. `Reward / Signal`  
   Positive reward for solved theorem, shaped reward for progress.

5. `Training Update`  
   SFT and/or RL update policy using trajectories.

LeanDojo mainly powers steps 1, 3, and trajectory collection for 5.

## Files Here

- `proofbot_leandojo_pipeline.py`: starter pipeline with:
  - setup target Lean repo
  - optional SFT training
  - proving run
  - simple success-rate evaluation helper

## Practical Milestones

1. Make one repo run end-to-end (`setup -> train -> prove`).
2. Log theorem-level outcomes (`solved`, steps, final error).
3. Add a fixed validation set and track pass@1 over time.
4. Add curriculum: easy to hard theorem buckets.
5. Add RL fine-tuning only after stable SFT baseline.

## Notes

- Start with a small model and CPU-friendly settings to validate plumbing.
- Keep commit hashes pinned for reproducibility.
- Never trust model output alone; Lean verification is the source of truth.
