# Loss of plasticity in deep continual learning

**Authors:** Shibhansh Dohare, J. Fernando Hernandez-Garcia, Qingfeng Lan, Parash Rahman, A. Rupam Mahmood, Richard S. Sutton  
**Year:** 2024  
**Venue:**   
[Open in Zotero](zotero://select/items/@dohareLossPlasticityDeep2024)  

---

**Abstract:**  
Artificial neural networks, deep-learning methods and the backpropagation algorithm form the foundation of modern machine learning and artificial intelligence. These methods are almost always used in two phases, one in which the weights of the network are updated and one in which the weights are held constant while the network is used or evaluated. This contrasts with natural learning and many applications, which require continual learning. It has been unclear whether or not deep learning methods work in continual learning settings. Here we show that they do not—that standard deep-learning methods gradually lose plasticity in continual-learning settings until they learn no better than a shallow network. We show such loss of plasticity using the classic ImageNet dataset and reinforcement-learning problems across a wide range of variations in the network and the learning algorithm. Plasticity is maintained indefinitely only by algorithms that continually inject diversity into the network, such as our continual backpropagation algorithm, a variation of backpropagation in which a small fraction of less-used units are continually and randomly reinitialized. Our results indicate that methods based on gradient descent are not enough—that sustained deep learning requires a random, non-gradient component to maintain variability and plasticity., The pervasive problem of artificial neural networks losing plasticity in continual-learning settings is demonstrated and a simple solution called the continual backpropagation algorithm is described to prevent this issue.

---

**My Notes:**  

- 
