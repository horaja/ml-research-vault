See [[Project Overview - DISCONTINUED]] for more information about the Project, and [[Implementation Notes]] for relevant Implementation Level Details.

## Phase 1: Basic Implementation, Baseline Measurements
#### Experiment 1.1.1: Base Implementation, Evaluation with 100% Patches
#### Experiment 1.1.2: Base Implementation, Evaluation with 40% Patches and Visualization
 - Exp ID: 20251112_211443
 - Notes:
	 - Some images have **heavy line drawing** in the background, leads to no patches selected from main visual concept.
	- Solution: Foreground/Background Segmentation or Depth Map + small MLP to determine which *layer* to heavily bias patches toward.
#### Experiment 1.1.3: Base Implementation, visualize CoG

#### *[TODO]* Experiment 1.1.4: Ablation Study—Positional Embedding Versions (Trained, Fixed, Logarithmic, etc.)
#### Experiment 1.1.5: Fine Tune ViT End-to-End
#### Experiment 1.1.6: Compare GFlops btwn varying patch percentages for LARGE ViT Backbone
- Hypothesis: Preprocessing GFlops is large itself, comparable to ViT Large
- Note: Don't Train, just run inference on pretrained weights
- Measure difference in total GFlops.
	- Hypothesis: Should be closer to a quadratic change.
#### Experiment 1.1.7: Baseline Test with Random Selection.
- For all patches (1.0 -> 0.1), uniformly randomly select the indices.
- IF random selection and LD-selection aren't too different, then SFT ViT with LD-selection to create an 'inductive bias', then use random sampling during inference to retain a low computational cost.
#### Experiment 1.1.7.1: Baseline Test with Non-Trivial Adaptive/Active Selection (SOTA)
#### Experiment 1.1.8.1: Baseline Test with very small number of patches.
- For all patches (0.1 -> 0.01).
#### Experiment 1.1.8.2: Baseline with only classification head fine-tuning
- Purpose: should be able to see more difference btwn DINO and ImageNet Pretrained.
#### *[TODO]* Experiment 1.1.9: Baseline with a more complex dataset
- Imagenet-100, with proper held-out test dataset
#### *[TODO]* Experiment 1.1.10: [[2025-12-18#A question|Key Scaling Question]].
#### *[TODO]* Experiment 1.2.1
Hypothesis: Patch Sparsification exhibits consistent efficiency-allocation tradeoffs across different pretrained visual representations
- Shows Patch Selection Method is Representation-Agnostic
Setup:
- ViT pretrained on DINO + ViT pretrained on ImageNet
- Both finetuned on Imagenette
- Gradual Patch Percentage Reduction (1.0 -> 0.1)
Key Question: Does the *relative degradation curve* depend on the pretrained visual prior?
Expected Outcome: In these relatively normal settings, the curves should be shaped the same.
#### *[TODO]* Experiment 1.3.1
Hypothesis: **Shape-biased representations** concentrate task-relevant information into *fewer spatial patches*
Purpose: Directly supporting the efficiency benefits of shape-guided patch selection.
Setup:
- Two pretrained models with contrasting inductive-biases:
	- DINO pretrained ViT
	- Imagenet pretrained ViT
- Do gradual patch percentage reduction (0.1 -> 0.01)
	- Measure classification accuracy as a function of retained patch percentage
Key Metrics: Accuracy **drop-off** (not absolute accuracy)
Expected Outcome: Since this is a stress-test setting, the shape-biased model has gradual degredation, texture-biased model has sharp drop-off.
Main Obstacle: Texture-biased model TOO good.
- Increase complexity of dataset, make patch removal more aggressive/adversarial, go down to 1% patch percentage, consider alternative tasks.
- **USE VLA TASK HERE**
	- SmolVLA backbone
	- Metric: 7D action L2 Error

Meeting notes for slightly different experiment:
- Networks that are shape-biased, then stripping away shape-biased tokens should not reduce the accuracy by much.
	- ex: MAE/DINO, timm-based, ViT-based models (10-15)
		- Pre-trained models
	- Opposite for texture-biased networks
	- Basically accuracy curves should drop off at much lower pp%.
	- **Link Shape-Bias with Patch Percentage and Efficiency**.
### Phase 1.4: Rigorous Benchmarking
#### *[TODO]* Experiment 1.4.1: Benchmark Random vs. LD on Object Segmentation task.
- Dataset: https://github.com/tue-mps/benchmark-vfm-ss
- Hypothesis: Since Line Drawings are just contours, LD-selection should be better at this task than random selection of patches.
### Phase 1.5: Depth Map & FG/BG Segmentation
#### *[TODO]* Experiment 3.1.1: Augment Patch Scorer Module with Disparity Mappings
- [[Implementation Notes#^1ab047|Score Calculation]]
#### *[TODO]* Experiment 3.1.2: Augment Patch Selector Module with Depth Awareness
1. Replace 2D Gaussian with depth-aware **kernel**: [[Implementation Notes#^c1f12d|Kernel Code]]
2. Possible Extension: *Induce Correlation Bias (Anisotropic Weighting)*
	1. Patches at similar depths receive higher correlation bias
## Phase 2: VLA Task
#### *[TODO]* Task 2.1: Setup SmolVLA pipeline for regression task
1. Find/Create Dataset with ground-truth continuous action labels
	1. $\texttt{lerobot/libero}$
		1. Libero-Goal has language prompts, with 256x256 images
2. Run eval script on correct environment, with the right args
#### Task 2.2: Integrate Custom Visual Encoder
1. Extend SmolVLA policy with custom encoder
	1. Augment Architecture to support:
		1. Multi-view Encoding
		2. Feature Projection
2. Extend traing script to Train Encoder + Projection layer, finetune others...?