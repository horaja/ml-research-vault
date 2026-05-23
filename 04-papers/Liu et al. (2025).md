# CaRT: Teaching LLM Agents to Know When They Know Enough

**Authors:** Grace Liu, Yuxiao Qu, Jeff Schneider, Aarti Singh, Aviral Kumar  
**Year:** 2025  
**Venue:**   
[Open in Zotero](zotero://select/items/@liuCaRTTeachingLLM2025)  

---

**Abstract:**  
Many tasks require learned models to strategically gather relevant information over multiple rounds of interaction before actually acting on a task. Strategic information gathering requires models to know not only how to effectively acquire information, but also when to stop gathering information and make a decision, in order to avoid overthinking or getting derailed when acting. In this paper, we formalize this problem and introduce Counterfactuals and Reasoning for Termination (CaRT), an approach for teaching LLMs when to stop seeking information. To appropriately learn when to terminate, CaRT fine-tunes LLMs using counterfactual pairs of trajectories, one where termination is appropriate and a minimally modified version of the same trajectory where it is not. It trains the LLM to explain the rationale for the termination decision in either case via verbal reasoning, and imbues this capability into the base LLM via fine-tuning. We instantiate CaRT in two domains: interactive medical diagnosis and math problem solving. In both domains, we find that CaRT improves the efficiency of information gathering and task success rate compared to other fine-tuning methods.

---

**My Notes:**  

- 
