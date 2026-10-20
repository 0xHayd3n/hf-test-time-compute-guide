# 5. Complete article navigation and provenance

[Previous: evidence](04-evidence-and-caveats.md) · [README](../README.md) · [Next: exercises](06-exercises-and-evaluation.md)

## The document being studied

[What is test-time compute and how to scale it?](https://huggingface.co/blog/Kseniase/testtimecompute) is a Hugging Face Community Article dated **6 February 2025**. The explicit closing credit is **Alyona Vert, author; Ksenia Se, editor**. Both profiles appear at the top of the page. This is an explanatory overview spanning multiple papers, not a new research paper with one experimental setup.

The source's entire prose, introduction, twelve linked sections/subsections, conclusion, resource list, and eleven embedded content figures were reviewed. Site navigation, comments, likes, and recommendation cards are not research evidence. The bonus list is included for navigation and credit, without converting it into a claim that every referenced paper was fully read. See [metadata/source.json](../metadata/source.json).

## Section-by-section reading map

Section labels below identify source locations. The questions and learning routes are original to this guide.

| Original article section | What to inspect while reading | Companion |
| --- | --- | --- |
| [The core idea behind OpenAI's o1 model](https://huggingface.co/blog/Kseniase/testtimecompute#the-core-idea-behind-openais-o1-model) | Separate the cognitive analogy from an implementation claim | [Module 1](01-compute-and-reasoning.md) |
| [What basically is Test-Time Compute (TTC)?](https://huggingface.co/blog/Kseniase/testtimecompute#what-basically-is-test-time-compute-ttc) | Ask which resource is measured, rather than equating time with compute | [Module 1](01-compute-and-reasoning.md) |
| [DeepSeek-R1's way of scaling test-time compute](https://huggingface.co/blog/Kseniase/testtimecompute#deepseek-r1s-way-of-scaling-test-time-compute) | Locate RL, cold start, distillation, and answer aggregation in different stages | [Module 2](02-training-and-inference.md), [evidence](04-evidence-and-caveats.md) |
| [Test-time compute scaling meets multimodality](https://huggingface.co/blog/Kseniase/testtimecompute#test-time-compute-scaling-meets-multimodality) | Identify which task is perception, reasoning, or generation | [Module 3](03-methods-across-modalities.md) |
| [Long-form text examples for MLLMs](https://huggingface.co/blog/Kseniase/testtimecompute#what-if-we-use-long-form-text-examples-for-training-mllms) | Keep training count and harder-subset results in their proper scope | [Modules 3](03-methods-across-modalities.md) and [4](04-evidence-and-caveats.md) |
| [Collective learning with CoMCTS](https://huggingface.co/blog/Kseniase/testtimecompute#collective-learning-with-collective-monte-carlo-tree-search) | Distinguish tree-value backup, trajectory creation, and parameter training | [Module 3](03-methods-across-modalities.md) |
| [Generating images with CoT](https://huggingface.co/blog/Kseniase/testtimecompute#generating-images-with-cot) | Compare outcome, process, and potential assessment; check metric definitions | [Modules 3](03-methods-across-modalities.md) and [4](04-evidence-and-caveats.md) |
| [Search-o1](https://huggingface.co/blog/Kseniase/testtimecompute#search-o1-enhancing-retrieval-and-agentic-capabilities) | Account separately for retrieval, document reasoning, and batching | [Module 3](03-methods-across-modalities.md) |
| [Three more research examples](https://huggingface.co/blog/Kseniase/testtimecompute#a-brief-overview-of-3-more-research) | Treat SANA 1.5, s1, and o1-Coder as brief pointers, not executable specifications | [Module 3](03-methods-across-modalities.md), [references](../references/README.md) |
| [Not without limitations](https://huggingface.co/blog/Kseniase/testtimecompute#not-without-limitations) | Identify separately underthinking, allocation, latency, and cost risks | [Module 4](04-evidence-and-caveats.md) |
| [Conclusion and test-time training](https://huggingface.co/blog/Kseniase/testtimecompute#conclusion-what-does-the-future-hold-for-test-time-compute) | Mark forecasts as forecasts; identify the possible weight-update boundary | [Module 2](02-training-and-inference.md) |
| [Bonus resources](https://huggingface.co/blog/Kseniase/testtimecompute#bonus-resources-to-dive-deeper) | Follow primary research and preserve author credit | [Research bibliography](../references/README.md) |

## Embedded figure coverage

There are eleven content images, in article order. This inventory describes their roles without copying the figures or transcribing their tables.

| Images | Article context | Reading purpose |
| --- | --- | --- |
| 1–3 | DeepSeek-R1 | RL behavior/results, R1 comparisons, and distillation comparisons |
| 4–5 | Virgo | Text-training domain distribution and multimodal benchmark table |
| 6–7 | Mulberry | Collective-search example, search efficiency, and MathVista comparison |
| 8 | PARM / PARM++ | Potential assessment, selection, reflection, and refinement schematic |
| 9–10 | Search-o1 | Retrieval/reasoning workflow and benchmark table |
| 11 | Conclusion | Screenshot of Aravind Srinivas's 30 January 2025 post, expressing a forecast about test-time training |

Images were inspected locally; no screenshots or research figures are included in the repository. Measurements selected for the ledger come from article prose, with a narrowly labeled exception recording the Virgo prose/table discrepancy. Missing figure cells must not be inferred from nearby prose. The screenshot in image 11 is commentary and is not experimental evidence.

## Version and access boundaries

The article is an unversioned URL, accessed **20 October 2026**. Its HTML snapshot SHA-256 is recorded in [source.json](../metadata/source.json). The hash identifies a local capture, not a permanent public version, and can change with dynamic site content. No claim is made that this capture is byte-for-byte identical to the article on its publication date.

The underlying research references use verified bibliographic records where available. Selected pre-article paper versions supply credit; the article does not identify every version it used. The Search-o1 paper was resolved by exact title as supplemental bibliography because the resource list omits a corresponding link. This does not add a second substantive source to the guide's coverage.

The requested structural reference, `0xHayd3n/harness2-guide`, returned HTTP 404 during preparation. The public [harness-learning-guide](https://github.com/0xHayd3n/harness-learning-guide) supplied an available structural comparison: full README, modular reading, evidence caveats, metadata, credit, and agent navigation. No content from that guide is reused as evidence about test-time compute.
