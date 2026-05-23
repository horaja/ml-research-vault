## Masked Autoencoder Theory
##### Overview of MAEs, from [[He et al. (2021)]]
MAE **masks random patches** of the input image and reconstructs the missing patches in the *pixel space*.

Has an **asymmetric** encoder-decoder design, where the encoder operates on the input image without masked tokens, but the decoder (very lightweight) reconstructs the full image.

##### Formalization
Given natural image $\bar{x}$ from an unlabeled dataset $\mathcal{D}_u$, we
1. reshape into n patches, $\bar{x} \in \mathcal{R}^{n\times s}$
2. uniformly draw a random binary mask $m \in \{0, 1\}^n$
to get two complementary masked views of $\bar{x}$,
- $x_1 = \bar{x}[m] \in \mathcal{R}^{n_1\times s}$
- $x_2 = \bar{x}[1-m] \in \mathcal{R}^{n_2\times s}$
where $n = n_1 + n_2$. 
This can be re-formulated as drawing $x_1, x_2$ from a joint distribution $\mathcal{M}(x_1, x_2 | \bar{x})$, with marginal distributions $\mathcal{M_1}(x_1|\bar{x})$, $\mathcal{M_2}(x_2|\bar{x})$ respectively.

Let the MAE hypothesis model be $h = g \circ f$, an encoder-decoder architecture.
Let the following be the adaptation of the simple MSE loss $$\mathcal{L}_{MAE}(h) = \mathbb{E}_{\bar{x}}\mathbb{E}_{x_1, x_2} ||g(f(x_1)) -x_2||^2$$
#### Reconstruction as a Pretext Task
In [[He et al. (2021)]], the *reconstruction target* is the **normalized pixel values** of each masked patch. Thus, the reconstruction takes place in *the pixel space*.
#### Implicit Contrastive Learning in Masking
In [[He et al. (2021)]], *random sampling without replacement* was used for selecting patches to mask. Note however, **structured sampling** can also be implemented.

[[Zhang et al. ()]] argues that masking
- is implicit contrastive learning
- implicitly creates positive pairs
- reconstruction loss is lower bounded by the alignment loss between those pairs
Firstly, 
#### Implicit Regularization in Masking
## Contrastive Learning, DINO