# Continuous Domain Generalization

**Authors:** Zekun Cai, Yiheng Yao, Guangji Bai, Renhe Jiang, Xuan Song, Ryosuke Shibasaki, Liang Zhao  
**Year:** 2025  
**Venue:**   
[Open in Zotero](zotero://select/items/@caiContinuousDomainGeneralization2025)  

---

**Abstract:**  
Real-world data distributions often shift continuously across multiple latent factors such as time, geography, and socioeconomic contexts. However, existing domain generalization approaches typically treat domains as discrete or as evolving along a single axis (e.g., time). This oversimplification fails to capture the complex, multidimensional nature of real-world variation. This paper introduces the task of Continuous Domain Generalization (CDG), which aims to generalize predictive models to unseen domains defined by arbitrary combinations of continuous variations. We present a principled framework grounded in geometric and algebraic theories, showing that optimal model parameters across domains lie on a low-dimensional manifold. To model this structure, we propose a Neural Lie Transport Operator (NeuralLio), which enables structure-preserving parameter transitions by enforcing geometric continuity and algebraic consistency. To handle noisy or incomplete domain variation descriptors, we introduce a gating mechanism to suppress irrelevant dimensions and a local chart-based strategy for robust generalization. Extensive experiments on synthetic and real-world datasets, including remote sensing, scientific documents, and traffic forecasting, demonstrate that our method significantly outperforms existing baselines in both generalization accuracy and robustness.

---

**My Notes:**  

- 
