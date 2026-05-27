---
type: claim
project: surf
status: supported
---

# efficiency without collapse

## claim
Selective patch processing can reduce compute without obvious classification accuracy collapse in the current ImageNet-10 setup.

## evidence
- [[sources/line-biased-vision-encoder]] reports full patch budget Top-1 `0.734`, Top-5 `0.964`, `1.408` GFLOPs.
- [[sources/line-biased-vision-encoder]] reports line-guided low compute Top-1 `0.758`, Top-5 `0.968`, `0.448` GFLOPs.

## interpretation
The result supports an efficiency-accuracy tradeoff for the current classification implementation. It does not yet establish action-task efficiency.

## missing evidence
- Repeated seeds and confidence intervals.
- Compute-matched dense or random selector controls.
- VLA/action prediction results.

## links
- [[concepts/visual budget]]
- [[experiments/e001]]
- [[eval/baselines]]
