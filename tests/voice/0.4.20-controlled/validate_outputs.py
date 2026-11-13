"""Validate saved evaluation text without running its commands."""
import argparse
import hashlib
import json
import re
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('paths', nargs='+', type=Path)
args = parser.parse_args()
results = {}
for path in args.paths:
    text = path.read_text(encoding='utf-8')
    han = len(re.findall(r'[\u4e00-\u9fff]', text))
    sections = len(re.findall(r'^## ', text, re.M))
    controls = [{'offset': i, 'codepoint': ord(c)} for i, c in enumerate(text)
                if ord(c) < 32 and c not in '\n\r\t']
    results[path.name] = {
        'han_count': han, 'section_count': sections,
        'control_characters': controls,
        'sha256': hashlib.sha256(text.encode()).hexdigest(),
        'passed': 1000 <= han <= 1200 and sections == 6 and not controls,
    }
print(json.dumps(results, ensure_ascii=False, indent=2))
raise SystemExit(0 if all(r['passed'] for r in results.values()) else 1)
