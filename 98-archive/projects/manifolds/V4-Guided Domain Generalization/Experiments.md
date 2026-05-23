See [[Research Proposal]] for more information on the Project.
# Phase 1: Baseline Characterization

### Experiment 1.1: *Layer-wise V4 Similarity Analysis*
Method: Compute RSA between each *Backbone* Layer and V4 Responses
Stimuli: *(Pre-decided I think?)*
Purpose: Identify optimal alignment layer
Details:
- Backbone: *ResNet-50*/ViT
- Similarity Metric: *RSA*/CKA
- Dataset: *STL-10*
Results: *Best layer: **layer3** (RSA = 0.1834)*
#### Experiment 1.1.2: *Using CKA*
Method: Same as above, but with CKA
Purpose: CKA is *invariant* to orthogonal transformations and scaling
Results: *Best CKA: **layer3** (0.4082)*

### Experiment 1.2: *Baseline Domain Transfer*
Method: Train *Backbone (ResNet-50)* on STL-10 Color, test on STL-10 LD with no fine-tuning
Metrics: Accuracy, top-1 accuracy
Purpose: Set baseline transfer accuracy
Details:
- Current progress:
	- Creating STL-10 LD TEST Dataset ONLY
		- Use Generator from [[Chan et al. (2022)]]
		- Style: *contour-style*
		- run on GPU

# Phase 2: Alignment Implementation

### Experiment 2.1: *Geometric Alignment*

### Experiment 2.2: *Neural Response Prediction - Implicit Alignment (analyze)*
