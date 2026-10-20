"""Offline integrity checks for this reading companion; no research validation."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import math
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ARTICLE = 'https://huggingface.co/blog/Kseniase/testtimecompute'
REPO = 'https://github.com/0xHayd3n/hf-test-time-compute-guide'
REQUIRED = [
    'README.md', 'AGENTS.md', 'LLMS.txt', 'ATTRIBUTION.md', 'LICENSE',
    'CITATION.cff', 'CONTRIBUTING.md', 'VERIFICATION.md',
    'docs/01-compute-and-reasoning.md', 'docs/02-training-and-inference.md',
    'docs/03-methods-across-modalities.md', 'docs/04-evidence-and-caveats.md',
    'docs/05-source-map.md', 'docs/06-exercises-and-evaluation.md',
    'metadata/source.json', 'metadata/claims.json', 'metadata/references.json',
    'references/README.md', 'references/article.bib', 'scripts/validate.py',
    '.gitattributes', '.gitignore',
]
errors = []
checks = 0


def check(condition, message):
    global checks
    checks += 1
    if not condition:
        errors.append(message)


def load_json(name):
    try:
        def reject_constant(value):
            raise ValueError(f'Non-finite JSON constant: {value}')

        def unique_keys(pairs):
            result = {}
            for key, value in pairs:
                if key in result:
                    raise ValueError(f'Duplicate JSON key: {key}')
                result[key] = value
            return result

        return json.loads((ROOT / name).read_text(encoding='utf-8'),
                          parse_constant=reject_constant,
                          object_pairs_hook=unique_keys)
    except (OSError, ValueError) as exc:
        errors.append(f'{name}: {exc}')
        return {}


def headings(text):
    """GitHub-style slugs for the simple headings used in this repository."""
    counts = {}
    result = set()
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        result.add(slug if count == 0 else f'{slug}-{count}')
    return result


for name in REQUIRED:
    check((ROOT / name).is_file(), f'Missing required file: {name}')

files = [p for p in ROOT.rglob('*') if p.is_file()
         and '.git' not in p.relative_to(ROOT).parts
         and '__pycache__' not in p.relative_to(ROOT).parts]
texts = {}
for path in files:
    rel = path.relative_to(ROOT).as_posix()
    check(path.suffix.lower() not in {'.pdf', '.html', '.png', '.jpg', '.jpeg',
                                     '.webp', '.zip', '.bin', '.safetensors'},
          f'Unexpected source/binary asset: {rel}')
    try:
        text = path.read_text(encoding='utf-8')
    except (UnicodeDecodeError, OSError) as exc:
        errors.append(f'{rel}: cannot read UTF-8: {exc}')
        continue
    texts[path.resolve()] = text
    check('\ufffd' not in text, f'Replacement character in {rel}')
    check('\x00' not in text, f'NUL in {rel}')
    if path.suffix != '.py':
        check(not re.search(r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})', text),
              f'Possible credential in {rel}')

local_links = 0
external_urls = set()
for path, text in texts.items():
    if path.suffix != '.md':
        continue
    prose = re.sub(r'^```.*?^```\s*$', '', text, flags=re.M | re.S)
    for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^\s]+)\)', prose):
        parsed = urlsplit(target.strip('<>'))
        if parsed.scheme in {'https', 'http'}:
            check(parsed.scheme == 'https', f'Non-HTTPS link: {target}')
            check(bool(parsed.netloc), f'Invalid external URL: {target}')
            external_urls.add(target)
            continue
        if parsed.scheme:
            continue
        local_links += 1
        destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        check(destination.is_relative_to(ROOT), f'Link leaves repository: {path.name}: {target}')
        check(destination.is_file(), f'Broken local link: {path.name}: {target}')
        if parsed.fragment and destination.is_file():
            content = texts.get(destination, destination.read_text(encoding='utf-8'))
            check(unquote(parsed.fragment) in headings(content),
                  f'Unknown local heading: {path.name}: {target}')

source = load_json('metadata/source.json')
claims_data = load_json('metadata/claims.json')
refs_data = load_json('metadata/references.json')
for label, data in [('source', source), ('claims', claims_data), ('references', refs_data)]:
    check(data.get('schema_version') == 1, f'{label}: unsupported schema version')
check(source.get('url') == ARTICLE, 'Unexpected source URL')
check(source.get('source_type') == 'community_blog_overview', 'Source must be a blog overview')
check([x['name'] for x in source.get('authors', [])] == ['Alyona Vert'], 'Wrong article author')
check([x['name'] for x in source.get('editors', [])] == ['Ksenia Se'], 'Wrong article editor')
check(source.get('published_date') == '2025-02-06', 'Wrong publication date')
check(source.get('repository', {}).get('url') == REPO, 'Repository URL mismatch')
check(bool(re.fullmatch(r'[0-9a-f]{64}', source.get('capture', {}).get('sha256', ''))),
      'Invalid source capture hash')
anchors = source.get('article_section_anchors', [])
check(len(anchors) == len(set(anchors)) == 12, 'Expected 12 unique article anchors')
check(source.get('coverage', {}).get('research_experiments_run') is False,
      'Research scope must remain explicit')
check([f.get('index') for f in source.get('figure_inventory', [])] == list(range(1, 12)),
      'Figure inventory must cover images 1 through 11')

refs = refs_data.get('sources', [])
ref_ids = [r.get('id') for r in refs]
check(len(ref_ids) == len(set(ref_ids)) == 15, 'Expected 15 unique source IDs')
for ref in refs:
    check(isinstance(ref.get('authors'), list), f'{ref.get("id")}: authors must be a list')
    check(isinstance(ref.get('metadata_verified'), bool), f'{ref.get("id")}: missing metadata status')
    check(ref.get('url', '').startswith('https://'), f'{ref.get("id")}: invalid URL')
    check(bool(ref.get('notes')), f'{ref.get("id")}: missing provenance note')

claims = claims_data.get('claims', [])
claim_ids = [c.get('id') for c in claims]
check(len(claim_ids) == len(set(claim_ids)) == 14, 'Expected 14 unique claims')
allowed_kinds = {'article_report', 'guide_observation', 'guide_interpretation', 'article_speculation'}
for claim in claims:
    label = claim.get('id')
    check(claim.get('kind') in allowed_kinds, f'{label}: invalid claim kind')
    check(claim.get('article_anchor') in anchors, f'{label}: unknown article anchor')
    check(bool(claim.get('caveat')), f'{label}: missing caveat')
    check('article' in claim.get('source_ids', []), f'{label}: article grounding missing')
    check(set(claim.get('source_ids', [])) <= set(ref_ids), f'{label}: unknown reference ID')
    for item in claim.get('measurements', []):
        value = item.get('value')
        check(isinstance(value, (int, float)) and not isinstance(value, bool)
              and math.isfinite(value), f'{label}: invalid numeric value')
        check(bool(item.get('label')) and bool(item.get('unit')), f'{label}: untyped measurement')

by_id = {c['id']: c for c in claims}
for label in ['mulberry-improvements', 'parm-improvements']:
    check(by_id.get(label, {}).get('absolute_or_relative', 'missing') is None,
          f'{label}: ambiguous unit must remain null')
    check(all(m['unit'] == 'percent_improvement_as_reported'
              for m in by_id.get(label, {}).get('measurements', [])),
          f'{label}: percentage ambiguity lost')

cff = texts.get((ROOT / 'CITATION.cff').resolve(), '')
check('cff-version: 1.2.0' in cff and 'preferred-citation:' in cff, 'CFF fields missing')
check(ARTICLE in cff and REPO in cff, 'Citation URLs mismatch')
check('given-names: "Alyona"' in cff and 'given-names: "Ksenia"' in cff,
      'Citation author/editor roles missing')

if errors:
    print('\n'.join('FAIL: ' + error for error in errors))
    sys.exit(1)
print(f'PASS: {checks} checks; {len(files)} files; {len(claims)} claims; '
      f'{len(refs)} sources; {local_links} local Markdown links; '
      f'{len(external_urls)} distinct external Markdown targets syntactically checked.')
print('Offline validation only. No network access, remote publication check, '
      'CFF schema validation, or experimental verification is performed by this script.')
