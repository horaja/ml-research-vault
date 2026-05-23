# Discovering Domain Disentanglement for Generalized Multi-Source Domain Adaptation

**Authors:** Zixin Wang, Yadan Luo, Peng-Fei Zhang, Sen Wang, Zi Huang  
**Year:** 2022  
**Venue:**   
[Open in Zotero](zotero://select/items/@wangDiscoveringDomainDisentanglement2022)  

---

**Abstract:**  
A typical multi-source domain adaptation (MSDA) approach aims to transfer knowledge learned from a set of labeled source domains, to an unlabeled target domain. Nevertheless, prior works strictly assume that each source domain shares the identical group of classes with the target domain, which could hardly be guaranteed as the target label space is not observable. In this paper, we consider a more versatile setting of MSDA, namely Generalized Multi-source Domain Adaptation, wherein the source domains are partially overlapped, and the target domain is allowed to contain novel categories that are not presented in any source domains. This new setting is more elusive than any existing domain adaptation protocols due to the coexistence of the domain and category shifts across the source and target domains. To address this issue, we propose a variational domain disentanglement (VDD) framework, which decomposes the domain representations and semantic features for each instance by encouraging dimension-wise independence. To identify the target samples of unknown classes, we leverage online pseudo labeling, which assigns the pseudo-labels to unlabeled target data based on the confidence scores. Quantitative and qualitative experiments conducted on two benchmark datasets demonstrate the validity of the proposed framework.

---

**My Notes:**  

- Orthogonal Domain Representations via Total Correlations
	- similar to [[Manifold Alignment Loss]]
