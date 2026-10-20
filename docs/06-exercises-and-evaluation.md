# 6. Exercises and an evaluation plan

[README](../README.md) · [Source map](05-source-map.md) · [Evidence and caveats](04-evidence-and-caveats.md)

All examples in this module are original, hypothetical teaching exercises. **No experiments were run, no model was implemented, and none of these numbers is a research result.** The evaluation plan is prospective.

## Exercise 1: classify the change

A team (a) fine-tunes on worked solutions, (b) generates five answers for a new question, (c) inserts retrieved passages into the prompt, and (d) updates model parameters using an adaptation loss at deployment. Which steps change model parameters?

**Worked answer.** Steps (a) and (d) do. Sampling in (b) and context construction in (c) do not require parameter updates. A larger workflow could include additional updates, but that would need to be stated. This exercise tests the distinction in [module 2](02-training-and-inference.md), relevant to the article's [R1 section](https://huggingface.co/blog/Kseniase/testtimecompute#deepseek-r1s-way-of-scaling-test-time-compute).

## Exercise 2: compute versus waiting

A generator runs three independent two-second jobs in parallel. A judge then runs for one second. Assume identical workers, no overhead, and no overlap between generation and judging. Find ideal request latency and total worker time.

**Worked answer.** Latency is `2 + 1 = 3` seconds. Total worker time is `3 × 2 + 1 = 7` worker-seconds. This is not a FLOP estimate: it assumes comparable workers and treats their occupied time as the accounting unit. Compare [module 1](01-compute-and-reasoning.md).

## Exercise 3: evaluate a selector

Across 100 hypothetical questions, a candidate set contains at least one correct answer for 80 questions. The selector returns a correct answer for 60. What did selection leave unused?

**Worked answer.** The selected accuracy is 60%; the candidate-set oracle opportunity is 80%. The gap is 20 percentage points. Conditional on a correct candidate existing, selection succeeds on `60 / 80 = 75%` of questions. The gap points to selection failures, but does not identify whether they came from score calibration, formatting, tie rules, or another cause. Increasing the sample count alone may leave this bottleneck intact.

## Exercise 4: an ambiguous improvement

A summary reports “10% better” without a baseline or metric. Can you enter a ten-percentage-point improvement in a results table?

**Worked answer.** No. If baseline accuracy were 50%, a relative 10% improvement would produce 55%; an absolute ten-percentage-point gain would produce 60%. A different metric might not even be accuracy. Preserve the reported wording, mark the unit unresolved, and seek the original evaluation definition. This is why [the evidence module](04-evidence-and-caveats.md) retains uncertainty around several article summaries.

## Exercise 5: more text, same error

A system uses twice as many tokens but gives the same wrong numerical answer. Has it shown improved reasoning?

**Worked answer.** Token usage alone shows additional output work under that tokenizer and configuration. It does not establish improved task performance. Inspect the task metric and intermediate checks; a failed final answer might still reveal useful diagnostic behavior, but that requires a separate definition and measurement. The article's [limitations section](https://huggingface.co/blog/Kseniase/testtimecompute#not-without-limitations) motivates asking whether spending is allocated usefully.

## A prospective evaluation protocol

Use this plan to investigate one mechanism rather than treating the overview as an executable specification.

1. **Define the task and success measure.** Choose an auditable set of questions and an answer-grading rule. Separate correctness, citation support, formatting, and subjective quality where they differ.
2. **Freeze the comparison.** Record model identifier, checkpoint, prompt, decoding settings, context policy, tool versions, and permitted information. Use a single-attempt baseline and vary one spending mechanism first.
3. **Predeclare budgets.** Measure generator tokens, verifier tokens, model calls, retrieved documents, tool work, wall time, and monetary cost separately. If using a combined resource proxy, explain its weights and limitations.
4. **Separate tuning and evaluation.** Tune stopping rules and verifier thresholds on development data. Keep evaluation answers out of retrieval, selection, and adaptation feedback unless explicitly studying an oracle upper bound.
5. **Test several budgets.** Compare achieved quality across resource levels. Report both matched-budget results and the resources needed to reach a chosen quality target. Parameter count or sample count alone is not equal compute.
6. **Inspect variation and failures.** Repeat stochastic configurations, report uncertainty, include timeouts and invalid outputs, and break results down by meaningful task difficulty. Record latency distributions rather than only their mean.

A useful record includes `question_id`, `configuration_id`, `budget`, `actual_resource_use`, `selected_answer`, `grade`, `latency`, and `failure_reason`. These proposed fields are not observations from this repository. A successful study would support a claim about its tested configurations and task distribution, not a universal rule that more inference work always helps.
