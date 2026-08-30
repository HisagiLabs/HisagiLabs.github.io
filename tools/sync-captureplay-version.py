#!/usr/bin/env python3
import argparse, json
from pathlib import Path

parser = argparse.ArgumentParser(description='Sync CapturePlay product-page Latest from package.json SSOT.')
parser.add_argument('--project-root', default='/srv/projects/development/CapturePlay')
parser.add_argument('--site-root', default=str(Path(__file__).resolve().parents[1]))
args = parser.parse_args()
project_root = Path(args.project_root)
site_root = Path(args.site_root)
package = json.loads((project_root / 'package.json').read_text(encoding='utf-8'))
version = str(package.get('version', '')).strip()
if not version:
    raise SystemExit('package.json.version is empty')
out = site_root / 'captureplay' / 'version.json'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps({'version': version, 'source': 'CapturePlay/package.json'}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'CAPTUREPLAY_PRODUCT_VERSION={version}')
print(f'CAPTUREPLAY_PRODUCT_VERSION_FILE={out}')
