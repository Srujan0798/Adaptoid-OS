#!/usr/bin/env python3
"""Generate a synthetic terminal demo GIF for Adaptoid OS."""
import os
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 960, 540
BG = (18, 18, 24)
FG = (220, 220, 230)
GREEN = (80, 250, 123)
YELLOW = (241, 250, 140)
CYAN = (139, 233, 253)
GRAY = (98, 114, 164)
FONT_SIZE = 18
LINE_HEIGHT = 26
MARGIN = 24

# Try to load a monospace font; fall back to default
font_paths = [
    "/System/Library/Fonts/Menlo.ttc",
    "/System/Library/Fonts/Monaco.dfont",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
]
font = None
for fp in font_paths:
    if os.path.exists(fp):
        font = ImageFont.truetype(fp, FONT_SIZE)
        break
if font is None:
    font = ImageFont.load_default()

frames = []


def new_frame():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    return img, ImageDraw.Draw(img)


def text_size(draw, txt):
    bbox = draw.textbbox((0, 0), txt, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def draw_line(draw, y, text, color=FG):
    draw.text((MARGIN, y), text, fill=color, font=font)


def typewrite(lines, output_lines=None, output_color=CYAN):
    """Type lines one character at a time, then show output."""
    output_lines = output_lines or []
    typed = []
    for line in lines:
        for i in range(len(line) + 1):
            img, draw = new_frame()
            y = MARGIN
            for t in typed:
                draw_line(draw, y, t)
                y += LINE_HEIGHT
            draw_line(draw, y, line[:i], GREEN)
            # terminal cursor
            if i < len(line):
                cx, _ = text_size(draw, line[:i])
                draw.rectangle(
                    [(MARGIN + cx, y), (MARGIN + cx + 10, y + FONT_SIZE)],
                    fill=GREEN,
                )
            frames.append(img)
        typed.append(line)

    # show output
    for out in output_lines:
        img, draw = new_frame()
        y = MARGIN
        for t in typed:
            draw_line(draw, y, t)
            y += LINE_HEIGHT
        draw_line(draw, y, out, output_color)
        for _ in range(6):
            frames.append(img)
        typed.append(out)


# Scene 1: clone and validate
typewrite(
    [
        "$ git clone https://github.com/Srujan0798/Adaptoid-OS.git",
    ],
    output_lines=[
        "Cloning into 'Adaptoid-OS'... done.",
    ],
)

# Scene 2: run dogfood
typewrite(
    [
        "$ cd Adaptoid-OS && bash validators/dogfood.sh",
    ],
    output_lines=[
        "OK  archetypes unique",
        "OK  failure modes sequential",
        "OK  INDEX.md references checked",
        "OK  engine generates structure",
        "DOGFOOD: PASS ✅",
    ],
)

# Scene 3: scaffold a project
typewrite(
    [
        "$ python3 adaptor/engine.py --brief \"CLI tool for JSON to CSV\" \\",
        "  --archetype cli-tool --tier T0 --output ./my-cli",
    ],
    output_lines=[
        "Generated ./my-cli/",
        "  - README.md",
        "  - pyproject.toml",
        "  - src/json2csv/__init__.py",
        "  - tests/test_convert.py",
        "  - PROJECT-INTENT.md",
    ],
)

# Scene 4: final tagline
for _ in range(24):
    img, draw = new_frame()
    msg = "Adaptoid OS v4.0 — harness engineering as the optimization target."
    mw, mh = text_size(draw, msg)
    draw.text(((WIDTH - mw) // 2, HEIGHT // 2 - mh), msg, fill=CYAN, font=font)
    url = "github.com/Srujan0798/Adaptoid-OS"
    uw, _ = text_size(draw, url)
    draw.text(((WIDTH - uw) // 2, HEIGHT // 2 + 20), url, fill=GRAY, font=font)
    frames.append(img)

# Save GIF
out_path = os.path.join(os.path.dirname(__file__), "demo.gif")
frames[0].save(
    out_path,
    save_all=True,
    append_images=frames[1:],
    duration=60,
    loop=0,
    optimize=False,
)
print(f"Wrote {out_path} ({len(frames)} frames)")
