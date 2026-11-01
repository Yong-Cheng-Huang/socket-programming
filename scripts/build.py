"""Rebuild the standalone page from the editable animation source."""
from pathlib import Path
import html
import re

root = Path(__file__).resolve().parents[1]
page = (root / "index.html").read_text()
source = (root / "src/animation.html").read_text()
page, count = re.subn(r'data-srcdoc="[\s\S]*?"', lambda _: 'data-srcdoc="' + html.escape(source, quote=True) + '"', page, count=1)
if count != 1:
    raise SystemExit("Missing animation frame in index.html")
(root / "index.html").write_text(page)
output = root / "_site"
output.mkdir(exist_ok=True)
(output / "index.html").write_text(page)
(output / ".nojekyll").touch()
print("Built _site/index.html")
