# Verification and its limits

Prepared on **20 October 2026** for an independent public reading companion.

## Source and editorial review

- Read the complete Hugging Face article prose, twelve linked sections, conclusion, and resource list.
- Inspected all eleven embedded content images locally. A prose/table discrepancy in Virgo's scores is explicitly preserved in the evidence module and claim ledger.
- Verified the closing author/editor byline and publication date. Main research bibliographic records were checked on authoritative abstract pages; bonus entries preserve their unverified author-list status.
- Kept article reports, guide explanations, observations, and speculation distinct. No full-text research audit or experimental reproduction was performed.
- Inspected the account's available `harness-learning-guide` structure after the requested `harness2-guide` returned 404.

## Reproducible offline checks

Run `python scripts/validate.py` from the repository root. The standard-library script checks required files; UTF-8 and obvious credential patterns; excluded binary/source formats; local Markdown file links and supported heading anchors; external URL syntax; source identity, byline, section coverage and hash format; reference and claim IDs; typed measurements; preserved null fields; and citation identity fields.

The script does **not** perform external HTTP requests, validate the full CFF schema, grade scientific claims, or establish the effectiveness of any model. It checks the repository's declared invariants and document integrity. The reading modules supply worked hypothetical examples, which are not research results.

Preparation run: **581 checks passed**, covering **22 files**, **14 claim records**, **15 source records**, and **85 local Markdown links**. Citation YAML was also parsed and validated separately against the official Citation File Format JSON schema; that schema check passed. It is not built into the dependency-free offline script.

## Publication checks

Publication and anonymous-access checks are separate from the offline validator. Before creation, the authenticated account repository listing was inspected for a matching guide. No matching article guide existed, and the selected repository name was available.

Observed after publication on 20 October 2026:

- GitHub's public API reported owner `0xHayd3n`, visibility `public`, default branch `main`, and the intended description.
- The repository HTML returned HTTP 200 without an authentication header.
- All **22 tracked files** matched the public Git tree's blob identities and unauthenticated raw-file bytes at the checked commit. No source capture, PDF, or image was present in that tree.
- All **22 active external destinations** returned HTTP 200. The historical `harness2-guide` structural reference remains a separately documented 404 and is not an active reading destination.
- All **12 article section anchors** matched IDs in the captured source HTML.

The final publication workflow repeats the file comparison after saving this verification note and the citation-format adjustment. The completion response identifies the final checked commit. These checks establish availability and file identity at the time checked; they cannot guarantee that external sites never change.

## Provenance boundaries

The HTML snapshot hash identifies the page captured during preparation. Dynamic page elements and unversioned edits can change it. The snapshot and source figures remain outside the repository. The article's 2025 date is not a promise that every captured byte is unchanged since then.

Underlying papers are credited but their full methods and results were not independently audited. Percentages with unknown units or protocols remain unresolved. The original article and research rights are not granted by the companion license.
