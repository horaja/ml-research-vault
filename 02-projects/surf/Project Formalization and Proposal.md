### Problem Overview
#### Problem
Vision Encoders in VLA models process all image patches uniformly, thus allocating equal computational power to task-irrelevant background patches as they do for task-critical object regions. 
- Biologically Implausible
- Computationally Wasteful
#### Question
What prior should guide selective allocation of computational power?
#### Solution
Key **Observations**:
1. Well-documented **Shape Bias** in biological vision
	1. Primary carrier of *affordance information*.
		1. For manipulation tasks, affordance-relevant regions are where action decisions concentrate.
2. Mid-level representations in **V4** are best suited to capture shape-bias by encoding the *skeleton* of an object.
**Iterative Selection**:
- Mirroring biological coarse-to-fine processing
- Natural fit for sequential Value of Information

### Research Questions

1. Can line-drawing-derived shape representations serve as an effective prior for patch/token allocation in vision models?
	1. Ablations to consider: depth map, etc.
2. Does selective allocation transfer to VLA settings, and does the efficiency gain hold when downstream task is action prediction over manipulation?
3. Can iterative (coarse-to-fine) selection improve over single-pass selection?
4. Do V4-aligned feature preferences provide complementary or superior guidance to line drawings?

### Setup/Assumptions
Clarify assumptions to make, scope of project

### Model
![[model_architecture.jpeg]]

### Methodology

### Results
STATE what you have found.

### Analysis
VALIDATION of results

### Limitations/Extensions

### Conclusion
Tie back to ORIGINAL Problem





































