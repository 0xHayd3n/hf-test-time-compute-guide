# 1. Compute, time, and reasoning

[README](../README.md) · [Next: training and inference](02-training-and-inference.md)

## Learning goal

After this module, you should be able to name the extra work a system performs, identify what could make that work useful, and avoid treating a longer answer as a measurement of reasoning quality.

**Source claim.** The article introduces inference spending as a resource that can be increased for harder tasks. It uses slow and fast human thinking as an analogy. See [its TTC definition](https://huggingface.co/blog/Kseniase/testtimecompute#what-basically-is-test-time-compute-ttc) and [o1 introduction](https://huggingface.co/blog/Kseniase/testtimecompute#the-core-idea-behind-openais-o1-model).

**Guide interpretation.** Treat this analogy as a prompt for engineering questions: Which operation runs again? What new information does it produce? How is a candidate accepted? It does not establish that a model has human mental processes.

## A compute ledger

The following is an original accounting model for reading the article, not an equation from its research references:

```text
request work = generation + candidate scoring + retrieval processing + tools
```

Each term must use the same unit before the terms can be added. FLOPs, measured GPU time, and money are different ledgers. Token counts are useful proxies within a carefully controlled setup; tokens from different model sizes or different context lengths need not cost the same amount.

| Operation | What extra work buys | What can go wrong |
| --- | --- | --- |
| Continue one attempt | More intermediate computation | Repeating or elaborating an error |
| Sample several attempts | A broader set of candidates | Candidates share the same mistake |
| Score or test candidates | A way to select among attempts | A weak verifier rewards the wrong feature |
| Retrieve documents | Access to information outside the prompt | Irrelevant or unreliable evidence |
| Run a tool | An external calculation or observation | Incorrect inputs or misleading feedback |

This table is a guide taxonomy. The article's examples occupy several cells at once; they are not interchangeable implementations of one algorithm.

## Compute is not latency

**Hypothetical example.** Four candidates each require two seconds on separate workers. A final judge takes one second. Ignoring scheduling and communication, the user may wait about three seconds, while the candidate work alone consumes eight worker-seconds. Running the four attempts sequentially would change latency without changing that candidate work total.

Conversely, waiting for a search service can increase latency while the model's accelerator is idle. A system can also reduce time per request through batching while processing more total requests. Therefore report at least three quantities separately: aggregate work, request latency, and throughput. Specify the hardware and concurrency when comparing them. The article discusses batching in [Search-o1](https://huggingface.co/blog/Kseniase/testtimecompute#search-o1-enhancing-retrieval-and-agentic-capabilities); this distinction explains why batching alone is not proof that a reasoning procedure requires fewer operations.

## Why selection matters

Suppose a generator sometimes produces a correct answer. Additional samples help only if the system can identify useful candidates often enough. An oracle that knows the correct answer would measure the opportunity in the candidate set. A deployed verifier measures how much of that opportunity can actually be recovered. These are different evaluation questions.

Majority voting needs answer normalization and a rule for ties. It may also amplify correlated errors. A unit test checks only the behaviors it covers. A reward model predicts a preference or score; that prediction is not ground truth. These are conceptual cautions for reading the methods, not findings reproduced in this repository.

## Working glossary

| Term | Meaning used in this guide |
| --- | --- |
| Inference | Computation performed to produce an output from an input |
| Test-time compute | Resources spent while handling the task, with the exact accounting boundary stated |
| Chain of thought | An intermediate sequence used to develop an answer; its length does not establish correctness |
| Candidate | One proposed answer or partial solution |
| Verifier | A procedure that evaluates a candidate or intermediate state |
| Best-of-N | Generate N candidates and select one using a stated rule |
| Retrieval | Fetch external material for possible use in the answer |
| Budget | A cap on a specified resource, such as tokens, calls, elapsed time, or money |

**Checkpoint.** When someone says a method “thinks longer,” ask for the operation, resource unit, selection rule, and measured benefit. Continue to [training and inference](02-training-and-inference.md) to locate where a method changes the model itself.
