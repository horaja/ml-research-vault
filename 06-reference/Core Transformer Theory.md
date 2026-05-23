## Self-Attention as a Kernel Method
#### Self-Attention

Computes a representation for each token in the input sequence by *attending* to all the input tokens

For each of the input tokens it 'attends' to, it calculates an *attention score* in terms of its own *query* vector, and the token that it is attending to's *key* vector. In matrix notation: $$\texttt{score} = \texttt{similarity($Q$,$K$)} = \frac{QK^T}{scaling}$$where $scaling = \sqrt{d_k}$ to ensure variance of attention scores stays bounded and stable.

#### Kernel Methods

**Key Idea**: Map input data into a high-dimensional feature space, where it can be linearly separated. 

**The Kernel Trick**: Allows for operation in high-dimensional feature spaces without ever needing to pay the computational costs associated with it.

Instead of computing the inner product in high-dimensional space, use a **kernel function** to compute the inner product directly in the input space.

Some examples:
- Linear Kernel: $K(x,x') = x^Tx'$
- Gaussian (RBF) Kernel: $K(x,x') = e^{-\gamma||x-x'||^2}$
##### Symmetric vs Asymmetric Kernels

**Symmetric**: $K(x,y) = K(y,x)$
Used for general similarity, undirected data, standard SVMs/ML

**Asymmetric**: $K(x,y) \neq K(y,x)$
Used in directed Graphs, conditional probabilities, source/target features.

#### The Link to Transformers

Via [[Tsai et al. (2019)]], it is apparent that **Scaled Dot Product Self-Attention** can be viewed through '*the lens of a kernel*'.

A Transformer's Self-Attention Mechanism is **asymmetric**, meaning token A's relevance to token B is not necessarily the same as token B's relevance to token A.

Thus, via [[Chen et al. (2023)]], the attention mechanism can be framed as **asymmetric KSVD**.

#### The Key Question for [[Project Overview - DISCONTINUED#Executive Summary|Dual Stream VLA]]
Can **adaptive patch selection** be formalized as a novel *kernel specification* for the Transformer's Attention mechanism?
## Expressivity and Approximation Theory of Transformers

## Position Encoding Theory
