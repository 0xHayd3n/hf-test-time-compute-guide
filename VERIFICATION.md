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

## Publication checks

Publication and anonymous-access checks are separate from the offline validator. Before creation, the authenticated account repository listing was inspected for a matching guide. After upload, the publication workflow checks repository visibility and description, compares remote file blobs with local files, fetches the repository and README without authentication, and checks linked source/reference destinations. The completion response reports the actual outcomes and any unresolved network failures; this section describes the checks rather than claiming them in advance.

## Provenance boundaries

The HTML snapshot hash identifies the page captured during preparation. Dynamic page elements and unversioned edits can change it. The snapshot and source figures remain outside the repository. The article's 2025 date is not a promise that every captured byte is unchanged since then.

Underlying papers are credited but their full methods and results were not independently audited. Percentages with unknown units or protocols remain unresolved. The original article and research rights are not granted by the companion license.
