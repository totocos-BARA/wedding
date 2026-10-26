"""Draws the app icons (two linked rings on rose) into public/icons."""
from pathlib import Path

from PIL import Image, ImageDraw

ROSE = (166, 63, 90)
RING_A = (255, 255, 255)
RING_B = (243, 214, 160)
OUT = Path(__file__).resolve().parent.parent / "public" / "icons"


def draw(size: int, scale: float) -> Image.Image:
    """scale is the ring artwork's width as a share of the icon (smaller for maskable icons)."""
    ss = 4
    big = size * ss
    img = Image.new("RGB", (big, big), ROSE)
    d = ImageDraw.Draw(img)
    art = big * scale
    r = art * 0.30
    stroke = max(2, round(art * 0.075))
    cy = big / 2
    gap = r * 0.62
    for cx, color in ((big / 2 - gap, RING_A), (big / 2 + gap, RING_B)):
        d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=color, width=stroke)
    return img.resize((size, size), Image.LANCZOS)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    draw(180, 0.74).save(OUT / "apple-touch-icon.png")
    draw(192, 0.74).save(OUT / "icon-192.png")
    draw(512, 0.74).save(OUT / "icon-512.png")
    draw(512, 0.6).save(OUT / "icon-maskable-512.png")
    draw(32, 0.95).save(OUT / "favicon-32.png")


if __name__ == "__main__":
    main()
