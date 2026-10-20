# 3. Different ways to spend an inference budget

[Previous: training and inference](02-training-and-inference.md) · [README](../README.md) · [Next: evidence](04-evidence-and-caveats.md)

## Learning goal

For each example, locate the generator, feedback signal, selection rule, and stage where the extra work occurs. The following comparison is an **original reading framework**. The article introduces the named projects, but does not supply one common implementation or matched-budget experiment.

| Example in the article | Mechanism to look for | Key reading question |
| --- | --- | --- |
| DeepSeek-R1 | Post-training plus learned reasoning behavior | What changes during learning versus during one request? |
| Virgo | Transfer of text reasoning training to multimodal tasks | Is perception or reasoning the bottleneck? |
| Mulberry / CoMCTS | Multiple models, tree search, and training trajectories | Is search generating training data or serving a request? |
| PARM / PARM++ | Evaluation of intermediate image-generation states | Can a partial state predict a good final image? |
| Search-o1 | Retrieval and processing of external information | Is the missing ingredient knowledge or computation? |
| SANA 1.5 | Generate candidates and rank them | What does the judge prefer, and how much does judging cost? |
| s1 | Learned reasoning plus budget control | What is held fixed while duration changes? |
| o1-Coder | Planning, code generation, and generated tests | What kinds of errors can the tests actually detect? |

## Perception and reasoning are separate failure points

**Article report:** the [Virgo section](https://huggingface.co/blog/Kseniase/testtimecompute#what-if-we-use-long-form-text-examples-for-training-mllms) discusses text-based reasoning training for multimodal models and differences across task difficulty and model size.

**Guide explanation:** consider a chart question. Reading a tick label incorrectly creates a perception error; subtracting two correctly read values incorrectly creates a reasoning error. Longer verbal work may help the second problem while preserving the first. A useful analysis therefore audits intermediate observations instead of assigning every failed answer to insufficient reasoning time. The article's explanations for benchmark differences remain explanations offered by the overview, not a causal experiment established here.

## Tree search and learning need separate diagrams

**Article report:** the [CoMCTS section](https://huggingface.co/blog/Kseniase/testtimecompute#collective-learning-with-collective-monte-carlo-tree-search) connects a collective search procedure to the creation of Mulberry training material.

**Guide explanation:** search maintains candidate states and statistics about their value. A rollout explores a continuation; a backup propagates its evaluation toward earlier choices. This use of “backpropagation” in tree search should not be confused with computing neural-network gradients. A later training stage may update model parameters using selected trajectories. Search-tree statistics and model weights are different objects, even when both are informed by feedback.

For any search claim, ask how many expansions occurred, how values were obtained, and whether the same feedback would be available on an unseen task. A path selected with access to a correct answer is different from a deployable selector that must judge without it.

## Image verification adds a prediction problem

**Article report:** the [PARM section](https://huggingface.co/blog/Kseniase/testtimecompute#generating-images-with-cot) distinguishes judging a final output from judging intermediate states and their potential, then describes refinement through feedback.

**Guide explanation:** an unfinished image can be hard to evaluate. A useful early selector must distinguish a bad-looking intermediate state that can improve from one that cannot. Early rejection saves generation work only when the saved work exceeds the cost and errors of the assessor. Final prompt alignment, visual quality, and human preference are different possible targets. The article's percentage summaries do not define enough of these details to support a universal ranking; see [the evidence module](04-evidence-and-caveats.md).

## Retrieval changes the available evidence

**Article report:** [Search-o1](https://huggingface.co/blog/Kseniase/testtimecompute#search-o1-enhancing-retrieval-and-agentic-capabilities) alternates reasoning with search and document processing, and discusses batching.

**Guide explanation:** when an answer requires an unavailable fact, repeating internal generation cannot be assumed to supply it. Retrieval can change the information set. It also introduces source quality, relevance, contradiction, and summarization problems. A document processor that removes a vital qualification can make the downstream answer worse despite returning a shorter context. Count search calls, document processing, and continuation separately. Batching may improve hardware utilization; it does not alone establish a smaller total operation count or a lower latency for every request.

## Read the brief examples as pointers

The article's [three short research notes](https://huggingface.co/blog/Kseniase/testtimecompute#a-brief-overview-of-3-more-research) mention SANA 1.5, s1, and o1-Coder. They are leads for further reading, not complete method specifications. The following are guide questions, not additional research findings:

- **Candidate ranking:** would the ranking remain reliable if all candidates shared an error?
- **Budget control:** what is the stopping criterion, and what happens when the extra allowance produces repetition?
- **Code tests:** could the generator and test generator make the same mistaken assumption? Passing generated tests is evidence only for what those tests cover.

The method names are credited in [the bibliography](../references/README.md). Follow those papers to verify exact algorithms, versions, evaluation settings, and licenses before implementing a system. Continue to [evidence and caveats](04-evidence-and-caveats.md).
