"""Builds public/index.html from src/guide.html.

src/guide.html is the page body as published to the claude.ai artifact.
This wraps it in a full document with the home-screen app tags, the
manifest and the service worker, so the same source runs on Workers.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "guide.html"
OUT = ROOT / "public" / "index.html"

HEAD = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="가족만 모여 드리는 스무 명의 예배. 스몰웨딩 후기 11편을 정리한 준비 앱.">
<meta name="wedding-standalone" content="1">
<meta name="theme-color" content="#FAF6F1" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#181215" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="스몰웨딩">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="apple-touch-icon" href="/icons/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="/icons/favicon-32.png">
"""

TAIL = """<script>
if ('serviceWorker' in navigator) {
  addEventListener('load', () => { navigator.serviceWorker.register('/sw.js').catch(() => {}); });
}
</script>
</body>
</html>
"""


def main() -> None:
    body = SRC.read_text(encoding="utf-8")
    # The artifact-only viewport hint has no meaning on a plain web page.
    body = body.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
    # Title, font links and the style block move into <head>; the rest is the body.
    style_end = body.index("</style>") + len("</style>")
    head_part = body[:style_end]
    rest = body[style_end:].lstrip("\n")
    html = HEAD + head_part + "\n</head>\n<body>\n" + rest.rstrip() + "\n" + TAIL
    OUT.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
