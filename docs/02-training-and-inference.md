# 2. What changes during training and inference?

[Previous: compute and reasoning](01-compute-and-reasoning.md) · [README](../README.md) · [Next: methods](03-methods-across-modalities.md)

## Learning goal

Classify a proposed improvement by what it changes and when it changes it. A training recipe and an inference policy can work together, but evidence for one does not automatically establish the benefit of the other.

**Source claim.** The article places reinforcement learning, cold-start examples, and distillation beside inference scaling in [its DeepSeek-R1 discussion](https://huggingface.co/blog/Kseniase/testtimecompute#deepseek-r1s-way-of-scaling-test-time-compute). Its conclusion separately introduces [test-time training](https://huggingface.co/blog/Kseniase/testtimecompute#conclusion-what-does-the-future-hold-for-test-time-compute).

**Guide interpretation.** These descriptions become easier to compare when split into a capability-building stage and a request-handling stage. This split is an explanatory framework, not a new claim about the internals of every model mentioned.

## Two objects to keep separate

Let `theta` denote model parameters, and let `pi` denote a policy for using the model. Here, “policy” means a procedure such as generating multiple attempts, making a search call, or stopping after a budget. The notation is introduced by this guide.

```text
training:       data and feedback -> a changed theta
inference:      input + theta + pi -> an output and a resource bill
```

A different `theta` may use the same inference procedure more effectively. A different `pi` may extract better answers from the same frozen model. If an experiment changes both, its final score does not tell you how much each change contributed. A useful comparison holds one fixed while varying the other, then checks whether their combination behaves differently.

| Change | Parameters updated as part of that change? | Reading question |
| --- | --- | --- |
| Supervised fine-tuning | Yes | What examples and target outputs were used? |
| Reinforcement learning | Yes | What reward and feedback shaped the update? |
| Distillation through fine-tuning | Yes | What teacher outputs became student training data? |
| More samples from a frozen model | No | How are answers selected and budgets matched? |
| Retrieval into the context | Not by retrieval alone | What evidence is fetched and retained? |
| Test-time training | Yes, for the adapted parameters | What update signal is available without leaking evaluation answers? |

## Reading the R1 example carefully

The article describes R1-Zero as using RL without labeled examples. Read that description in the context of the reasoning post-training stage: “Zero” does not mean the system began with no pretrained language model or no previous training. It also does not imply that training receives no task information or reward signal. The important contrast in the overview is the absence of a supervised reasoning warm-up before that RL stage.

Cold-start supervised examples provide target behavior before reinforcement learning. Conceptually, that can constrain formatting and demonstrate the kind of solution being rewarded. RL then changes behavior through a feedback objective. An inference run subsequently uses the resulting parameters. Watching that run revise an answer does not, by itself, show a parameter update during the request.

Distillation through training is another parameter-changing process. **Original analogy:** a teacher prepares worked exercises, and a student practices on them. The student need not contact the teacher every time it later solves a problem. Accordingly, teacher data generation cost, student training cost, and student inference cost belong in separate columns. Calling the student “efficient” requires stating which column is smaller and for what performance target.

## Three meanings of improvement

1. **Across training:** a later checkpoint performs better because its parameters changed.
2. **Within one request:** a fixed model or workflow improves an answer by revising, searching, sampling, or checking.
3. **Across an adaptation procedure:** test-time training updates selected parameters using an allowed signal from the new setting.

These are guide distinctions. The article's language about reflection and self-evolution should not erase them. The conclusion's suggestion that test-time training could help future systems is a forward-looking proposal, not a result established by the overview.

## A minimal causal check

**Hypothetical comparison.** Model A answers once; model B has different training and gets eight attempts plus a judge. If B wins, that supports the complete B configuration on that evaluation. It does not isolate training, sampling, or judging. Add comparisons using A with eight attempts and B with one attempt, record the judge cost, and retain a held-out evaluation. Even this design must account for different per-token model costs.

Continue to [methods across modalities](03-methods-across-modalities.md), then use [the exercises](06-exercises-and-evaluation.md) to practice classifying these mechanisms.
