# Contributing corrections

For a factual correction, include the affected file, the article section URL, and a concise explanation. State whether the article itself is ambiguous or whether this guide misread it. Keep the article's historical report intact when introducing separately labeled primary-paper evidence or later developments.

For a numeric claim, specify model, benchmark version, task subset, metric unit, baseline, sampling/selection protocol, and compute accounting. Unknown details must stay unknown. A percent sign alone is not enough to infer a relative improvement or a percentage-point difference.

Keep `metadata/claims.json` and the human evidence module consistent. Add bibliographic metadata with a verification scope; do not label full-text research as verified after reading only an abstract page. Preserve article author/editor roles and underlying research credit.

Please do not contribute source PDFs, copies of the article, third-party figures, datasets, model weights, or credentials. Add original teaching material and links to authorized sources instead.

Run `python scripts/validate.py` from the repository root. Explain which additional source or remote checks you performed. Research replication, if added in future, needs its own methods, environment, data rights, and results; it cannot be inferred from this documentation.
