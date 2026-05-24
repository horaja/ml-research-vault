# Surf Project — State of the Repo (2026-05-24)

## Overview

The project is called **surf** — learning where to look by selectively allocating visual compute toward task-relevant regions. The central hypothesis: a structured spatial prior (line drawings, task semantics, language conditioning) can guide a ViT to process fewer patches while matching or beating full-patch baselines, both on classification and on household manipulation tasks.

The project has three modules in theory:
1. **Prior/selector module** — proposes which patches to process
2. **VLA/action module** — consumes selected visual evidence for task behavior
3. **Efficiency/RL module** — controls adaptive allocation under a visual budget

Only Module 1 has active experimental results. Modules 2 and 3 are planned/designed but not implemented.

---

## Repositories

### 1. `line-biased-vision-encoder/` — Complete. Results in hand.

This is the foundational experiment (vault: `e001`). The `SelectiveMagnoViT` architecture uses line drawings to score and select the top-k patches before feeding a ViT for ImageNet-10 classification.

**Stack:** Python 3.10, PyTorch 2.x, ViT backbone (DINOv2-based), informative-drawings generator as submodule. Managed with `mamba` environment (`vla`).

**Key results (ImageNet-10 val):**

| Patch budget | Top-1 | GFLOPs |
|---|---|---|
| Full (~100%) | 0.734 | 1.408 |
| ~60% | 0.757 | 0.859 |
| ~40% | **0.758** | **0.448** |
| ~22% | 0.755 | 0.283 |
| ~12% | 0.706 | 0.176 |

The 40% budget point is the headline result: **Top-1 0.758 at 0.448 GFLOPs vs 0.734 at 1.408 GFLOPs** — line-guided selection improves classification accuracy while using 3× fewer GFLOPs.

**Status:** Experiment complete. Checkpoints at `checkpoints/p0.1` through `p1.0`. Results at `results/smart/`. What's missing: repeated seeds/confidence intervals, and explicit center-bias and Canny edge-density kill baselines to rule out the result being an artifact of structural biases rather than line guidance specifically.

---

### 2. `behavior_env/` — Infrastructure complete. Frame collection blocked. No evaluation results yet.

This is the BEHAVIOR-1K evaluation axis. It uses **OmniGibson** (Isaac Sim-based physics simulator) running inside a **Singularity container** (`omnigibson.sif`, ~14 GB) on SLURM. The goal: measure whether patch selectors preserve task-relevant visual information in household manipulation tasks using MAE reconstruction quality (Q-hat metric).

**Stack:**
- OmniGibson (Isaac Sim 4.5, Python 3.10 inside `micromamba` conda env)
- `facebook/vit-mae-large` for reconstruction
- `transformers 4.47.1`, pinned (Torch 2.5.1 in container — blocked from upgrading past 4.47 due to CVE-2025-32434 requiring torch ≥ 2.6)
- `lpips`, `pytorch-msssim`, `safetensors` for dissimilarity metrics
- BDDL3 for task definitions, JoyLo for control
- SLURM with numbered pipeline scripts (`01_pull_sif.sh` → `06_run_offline_evaluation.sh`)

**Evaluation framework architecture:**

```
BDDL task file → TaskMaskConstructor → pixel mask W (task-relevant objects)
RGB frame + seg → PatchSelector → selected patches (k of 196)
selected patches → MAEReconstructor → I_recon
Q-hat = D(W⊙I, W⊙I_recon_selected) / D(W⊙I, W⊙I_recon_all)
```

Patch selectors implemented: random, center-bias, edge-density (Canny), line-drawing. Budgets: k = 20, 40, 60, 80, 100, 120 on a 14×14 grid.

**Infrastructure progress:**
- ✅ SIF pulled (job 343199)
- ✅ OmniGibson data downloaded (jobs 343204–343207)
- ✅ Packages installed in `pip_overlay/`
- ✅ All 24 tests passing as of **job 385993** (Apr 6): 12 mask/coverage tests (CPU), 7 MAE tests (GPU), 5 pipeline end-to-end tests (GPU)
  - Earlier failure (job 385132): transformers version mismatch caused CVE-2025-32434 torch.load error — resolved by pinning `transformers==4.47.1` and `huggingface-hub==0.36.2`
- ❌ **Frame collection (step 05) is blocked.** Three tasks attempted: `turning_on_radio`, `sorting_vegetables`, `assembling_gift_baskets`. All three `evaluation_data/` directories exist but are empty (no `.npy` files, no `metadata.json`).

  Failure modes across attempts:
  - **Jobs 386155–386160** (`turning_on_radio`): cancelled on node `mind-0-18` (now excluded in the script)
  - **Job 386220** (`turning_on_radio`): `TypeError: Type parameter ~_T without a default follows type parameter with a default` — a Python 3.10 vs `typing_extensions` compatibility crash inside Isaac Sim's extension loading path (`omni.kit.pip_archive`)
  - **Job 386230** (`sorting_vegetables`): **Segmentation fault** at `simulation_app.py:_wait_for_viewport` — Isaac Sim viewport init crash
  - **Job 386322**: ran outside the container, hit `OmniGibson is not available` immediately
  - **Job 386544**: `No module named 'numba'` — wrong Python environment
  - **Job 388080**: `No module named 'huggingface_hub'` — pip_overlay not mounted (used wrong SLURM script variant)

  The core issue: two concurrent blockers: (1) a `typing_extensions` / Isaac Sim extension TypeVar error on some nodes, (2) a segfault inside Isaac Sim viewport initialization on others. The segfault class matches the blocker noted previously in `eval/behavior.md`.

- ❌ **Step 06 (offline evaluation)** not run — depends on frames from step 05

---

### 3. `magno_stream_encoder/` — Archived / defunct

Static HTML site (`index.html`, `404.html`). Last touched Jan 26. This is a GitHub Pages placeholder, not active experimental code. The real encoder code is in `line-biased-vision-encoder/`.

---

### 4. `lerobot/` — Cloned but unused

Hugging Face LeRobot repository (cloned Dec 24, last meaningful commit Jan 17). Environment defined (`lerobot` conda env). No outputs or training runs. Pulled as a potential VLA/action backbone for Module 2 but not used yet.

---

### 5. `BEHAVIOR-1K/` (top-level, Tianqin's) — Read-only / upstream reference

Tianqin's fork of BEHAVIOR-1K without the evaluation code added by this project. Not actively modified.

---

## Designed-but-not-started experiments

**Language conditioning** (`behavior_env/docs/contrastive_alignment.md`): A TRIPS-inspired design for replacing the task-agnostic line-drawing scorer with a cross-modal contrastive scorer. Patch embeddings projected to a shared space alongside a frozen language encoder; top-k selected by cosine similarity. Two-stage training: contrastive pre-training on DAA gaze data → fine-tune end-to-end on BEHAVIOR-1K with action loss. Fully designed (projectors, training loop, failure modes, ablation plan) but not yet implemented.

**Kill baselines for e001**: center-bias and Canny edge-density comparisons on the same ImageNet-10 setup are absent from the results. These are necessary to confirm the "structure helps" claim is not an artifact of spatial biases.

---

## Active blockers

| Blocker | Location | Status |
|---|---|---|
| Isaac Sim segfault during `_wait_for_viewport` | `behavior_env/` step 05 | Unresolved — multiple nodes affected |
| `typing_extensions` TypeVar error inside Isaac Sim extensions | `behavior_env/` step 05 | Unresolved — node-dependent |
| No kill baselines for e001 | `line-biased-vision-encoder/` | Not started |
| No actual Q-hat results | `behavior_env/` | Blocked by frame collection |

The single highest-leverage unblock is fixing frame collection. Once frames exist, the full evaluation pipeline (selectors × budgets × metrics) can run in one SLURM job (step 06) — the pipeline tests confirmed the eval code works end-to-end with synthetic frames.
