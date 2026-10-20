# 4. Evidence, numbers, and limits

[Previous: methods](03-methods-across-modalities.md) · [README](../README.md) · [Next: source map](05-source-map.md)

## What kind of evidence is available?

The source is an accessible overview of multiple projects. It supplies prose summaries and embedded research figures, not a single shared evaluation protocol. **Every number below is reported by the article, not measured or independently reproduced here.** Bibliographic checks establish research identities and credits; they do not validate experiments. The machine-readable counterpart is [claims.json](../metadata/claims.json).

## Selected article-reported measurements

| Claim ID | Article report | Essential qualification |
| --- | --- | --- |
| `r1-zero-aime` | AIME accuracy 15.6% → 71%; 86.7% with majority voting | Training improvement and multi-answer aggregation are different comparisons. The prose does not specify all sampling and budget details. |
| `r1-distillation-data` | 800,000 examples used for distillation | Training-data count, not inference-token budget or proof of lower cost at equal quality. |
| `virgo-training-data` | 5,000 long-form text examples | A training-data quantity. Do not interpret it as the number of visual test questions. |
| `virgo-benchmark-scores` | MathVision 38.4%; OlympiadBench 29.3% | These are the prose values. The embedded table's text-trained Virgo-72B row shows 38.8 and 29.9 instead; do not silently reconcile the discrepancy. |
| `virgo-hard-subset` | Virgo 54.7% versus QVQ 48.6% on hard questions | A harder subset comparison, not a whole-benchmark or universal model ranking. |
| `mulberry-data` | Mulberry-260K contains 260,000 multimodal questions | Dataset size, not number of independent human labels or inference attempts. |
| `mulberry-improvements` | +4.2% for 7B and +7.5% for 11B versus their stated bases; +5.7% MathVista and +3.0% MMMU | Preserve the percent sign as reported. The prose does not resolve absolute versus relative units or all model/aggregation contexts. |
| `parm-improvements` | PARM +6%; PARM++ up to +24% and +15% versus Stable Diffusion 3 | Metric, denominator, and complete protocol are insufficiently specified in prose. Do not turn these into percentage-point deltas or a universal quality ranking. |
| `s1-training-data` | s1K has 1,000 examples | Training-set size, not evidence that inference is always cheap. |

Source locations: [DeepSeek-R1](https://huggingface.co/blog/Kseniase/testtimecompute#deepseek-r1s-way-of-scaling-test-time-compute), [Virgo](https://huggingface.co/blog/Kseniase/testtimecompute#what-if-we-use-long-form-text-examples-for-training-mllms), [Mulberry](https://huggingface.co/blog/Kseniase/testtimecompute#collective-learning-with-collective-monte-carlo-tree-search), [PARM](https://huggingface.co/blog/Kseniase/testtimecompute#generating-images-with-cot), [brief research notes](https://huggingface.co/blog/Kseniase/testtimecompute#a-brief-overview-of-3-more-research).

These are selected prose reports, not an exhaustive transcription of image tables. In particular, Search-o1's result image is not converted into a fresh dataset here. The figure review checks context; it does not create an independent results extraction.

**Source-internal discrepancy:** the Virgo image is the fifth content image in article order. Its `Virgo-72B` text-training row differs from the prose values, as noted above. The overview does not explain this difference or pin the paper version behind the image. This is a guide observation about two parts of the source, not an independently verified correction to the research. The ledger keeps both with their provenance.

## How to read a strong comparison

**Guide analysis.** A score belongs to a complete experimental configuration. To turn a secondary report into a dependable comparison, recover the model checkpoint, benchmark version and split, metric, prompt, sampling rule, selection method, resource cap, and failure handling. If one method receives more samples or a more expensive judge, its higher score may be useful while remaining a different cost-quality point.

An improvement can also have two denominators. From a hypothetical baseline accuracy of 40%, a relative 10% improvement yields 44%; a ten-percentage-point gain yields 50%. This arithmetic is original teaching material. It is not a reconstruction of the article's ambiguous percentages. Unknown fields are explicitly `null` in the ledger.

## Editorial cautions

| Wording or framing in the overview | Careful reading |
| --- | --- |
| R1-Zero is trained without pre-labeled data | Guide clarification: scope this to the reasoning post-training contrast with preliminary supervised fine-tuning. The overview's wording should not be expanded into a claim about all pretraining data. This guide has not audited the complete training protocol. |
| Search “backpropagation” makes a model learn | Tree-value backup and neural parameter updates are distinct operations. See [module 3](03-methods-across-modalities.md). |
| Slow thinking resembles human System-2 cognition | An analogy is not an identification of a model's mechanism or mental state. |
| Reflection shows self-awareness or proves deep reasoning | Observable revision behavior does not establish consciousness, introspective accuracy, or a general proof. |
| Search-o1 retains “relevant and redundant” information | The wording appears inconsistent with the stated filtering purpose. This guide flags the ambiguity rather than treating redundancy as a verified design objective. |
| Open-source examples uncover o1's core principles | Similar behavior is not documented access to a closed system's implementation. Model and code licenses must be checked individually. |
| Test-time training may be a next step | This is a prospective suggestion in the conclusion, not an experimental result of the article. |

## Limits named by the article

The [limitations section](https://huggingface.co/blog/Kseniase/testtimecompute#not-without-limitations) discusses underthinking, uneven latency, poor allocation, variable behavior, and unpredictable request costs. Its conclusion's wider predictions are commentary.

**Guide analysis:** evaluate those issues separately. A model can switch paths too quickly even while emitting many tokens. Variable latency is observable without proving why it occurs. Sampling randomness, service scheduling, and budget policies are different possible sources of variation; the overview does not establish their causal contributions. Simple tasks also do not require a universal ban on extra compute: the useful question is whether a particular added operation earns its cost on the target distribution.

## Limits of this companion

- The article is unversioned; the captured page may contain later edits.
- Paper versions and exact experimental protocols were not reconstructed from full texts.
- No independent benchmark, model run, causal ablation, or reproduction supports this repository.
- No current state-of-the-art, model availability, or deployment-cost claim is made.
- Figure-only values and full paper tables are deliberately not redistributed as a dataset.

Use the [source map](05-source-map.md) to return to context and the [evaluation exercises](06-exercises-and-evaluation.md) to plan what additional evidence would be needed.
