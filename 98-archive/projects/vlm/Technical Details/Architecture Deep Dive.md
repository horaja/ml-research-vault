## Data Preprocessing
Given a raw dataset, we need
1. Color, 256x256
2. Black and White, 256x256 -> Line Drawing, 256x256
## Block 1: Patch Importance Scorer
Given patch size as hyperparameter.
Inputs: Line Drawing Images/Patches
1. Calculate Score via LD Density
	1. Normalize score into probability distribution via softmax
2. Calculate center of gravity for each image
Outputs: scores of shape (B, num_patches), cog of shape (B, 2) where each (y,x) in [0,1]
## Block 2: Spatial Threshold Selector
**Inputs: Patch Percentage, Threshold, Gaussian Standard Deviation**
#### a. Create Gaussian Weights given number of patches on the height and the width
**Inputs**:
- $H_p$, $W_p$
	- representing the number of patches on width and height ST $N = H_p \cdot W_p$
- $c$
	- tensor with entries $c_b = (y_b, x_b)$ for all $b = 1 ... B$
1. Create Patch Coordinate Grid—(0,0) in top left, (1,1) in bottom right—for each image in batch
	1. Apply row-major flattening to get $N$ patch indices.
2. For each batch $b$ and patch index $n$
	1. Calculate the squared euclidean distance from the center $c_b$ as $$d_{b,n} = ||p_n - c_b||^2 = (y_n - y_b)^2 + (x_n - x_b)^2$$
	2. Using $\sigma$ as the gaussian standard deviation, $$g_{b,n} = \exp(-\frac{d_{b,n}}{2\sigma^2})$$
3. Per-Batch Normalization to create spatial prior
**Outputs**:
- Normalized Matrix $G \in \mathbb{R}^{B \times N}$ where $G_{b,n} = \frac{g_{b,n}}{\sum_{n'}g_{b,n'}}$
**Hyperparameter Controls**: Small $\sigma$ ensure weights are more focused around center, large $\sigma$ flattens the.
#### d. Finally, Select Patches
**Inputs**:
- $\texttt{patches}$ of shape (B, N, D)
- $\texttt{positional\_embeddings}$ of shape (1, N+1, D)
- $\texttt{scores}$ of shape (B, N)
- $\texttt{line\_drawings}$ of shape (B, 1, H, W)
1. Calculates Gaussian Weights
2. Create Joint Distribution over softmax-ed scores and weights
	1. Renormalize
3. Multinomial Sampling to obtain selected indices
4. Gather to selected patches
5. Remap positional embedding layer