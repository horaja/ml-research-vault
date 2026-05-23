## Information Bottleneck Principle

^281ba6

From [[Tishby et al. (2015)]], an information theoretic tradeoff between **compression** and **prediction**.

**Mutual Information**: Given two random variables $X$ and $Y$, and the entropy of a random variable $H$, the mutual information between $X$ and $Y$ describes how much clarity about the value of one variable is gained by observing the other. $$I(Y;X) = H(Y)-H(Y|X)$$
Note: mutual information is *symmetric*.

**Minimal Sufficient Statistic**: Denoted by $\hat{X}$, it is the simplest mapping of X that captures the mutual information $I(X;Y)$. In other words, it is the relevant part of $X$, with respect to $Y$.

We thus assume the Markov Chain $Y \rightarrow X \rightarrow \hat{X}$, where $X$ is generated from $Y$, and $\hat{X}$ only depends on $X$, and have the following objectives:

Objective 1: Minimize $I(X;\hat{X})$, and **compress** information.
Objective 2: Maximize $I(\hat{X},Y)$, and **predict** information.

**The Lagrangian Objective Function**
Finding an optimal representation $\hat{X} \in \mathcal{\hat{X}}$ is formulated as the minimization of the following Lagrangian subject to the Markov Chain Constraint: 
$$\mathcal{L[p(\hat{x}|x)]} = I(X;\hat{x})-\beta I(\hat{X};Y)$$
where $\beta$ is the positive Lagrange Multiplier that operates as a tradeoff parameter between the complexity (*rate*) of preservation, $R = I(X;\hat{X})$ and the amount of information preserved, $I_y = I(\hat{X};Y)$. ^6befa3

Note, an equivalent form:$$\mathcal{L[p(\hat{x}|x)]} = I(X;\hat{x})+\beta I(X;Y|\hat{X})$$This is because $I(X;Y|\hat{X})$ is the **residual information** (what $\hat{X}$ failed to capture about the $Y \rightarrow X$ relationship). 

#### For Deep Learning

Note: Each layer in a DNN processes inputs from only the previous layer, letting us assume the following Markov Chain:$$Y \rightarrow X \rightarrow h \rightarrow h \rightarrow h \cdots \rightarrow \hat{Y}$$Then by the data processing inequality, for any $i \geq j$, $$I(Y;X) \geq I(Y;h_j) \geq I(Y;h_i) \cdots \geq I(Y;\hat{Y})$$Following from the Lagrangian Formulation above, each layer $i$ should attempt to
1. Maximize $I(Y;h_i)$
2. Minimize $I(h_{i-1}, h_i)$

Since $I(Y;\hat{Y})$ measures how much of the predictive features in X of Y are captured by the model, let it be the natural quantifier for the **quality** of a DNN.

In a learning theoretic framework, reducing $I(h_{i-1}, h_i)$ represents the minimum description length of the layer.

Thus, we can formulate the **optimal IB limit** for some layer $i$, for some $\beta$ $$I(h_{i-1};h_i) + \beta I(Y;h_{i-1}|h_i)$$where $h_0 = X$ and $h_{m+1}=\hat{Y}$. ^c8f935

**Some Takeaways**
- Input layer $X$ has the lowest IB Distortion, and successive layers only increase this distortion.
- However, successive layers also compress inputs, hopefully eliminating only irrelevant inputs.

*TODO*: Analyze Figure 2 and Generalization Bounds
#### Deep Variational Information Bottleneck

[[Alemi et al. (2019)]] use **variational approximations** to make the *Information Bottleneck Principle* trainable with standard deep learning techniques.

*TODO*: Explore this model in more depth.
## Rate-Distortion Theory

Branch of Information Theory that provides the theoretical foundations for **lossy data compression**.

**Rate**: $I(X;\hat{X})$
- \# of *bits* stored
**Distortion**: $I(X;Y|\hat{X})$
- In the simplest case, distortion is the difference between input and output signal
- Commonly used: Mean-Squared Error
#### Impacts of Sparsity
#### Connection to Learned Representations
## Token Pruning Theory and Approximation Bounds
#### Importance Scoring Theory
#### Top-k Selection