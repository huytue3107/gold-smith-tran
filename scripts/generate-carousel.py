#!/usr/bin/env python3
"""
Generate a Gold Smith Tran carousel PDF with a clean financial style.

Style: warm cream background, serif typography, minimalist financial
illustrations, restrained gold accent, brand banner.

Usage:
    python3 scripts/generate-carousel.py --json content.json --output posts/001-test/carousel.pdf
    python3 scripts/generate-carousel.py  # uses built-in demo content

Dimensions: 1080x1350px (4:5 social carousel standard)

Customize: Edit the BRAND section below if the Gold Smith brand changes.
"""

import json
import math
import os
import sys
import argparse
import textwrap
from PIL import Image, ImageDraw, ImageFont

# ============================================================
# BRAND CUSTOMIZATION
# ============================================================
BRAND_NAME = "GOLD SMITH TRAN"          # Appears on banner
AUTHOR_NAME = "Gold Smith Tran"         # Appears on CTA slide
AUTHOR_ROLE = "Nha Gia Kim Forex"       # Appears on CTA slide

# --- BRAND COLORS (RGB) ---
BG = (245, 243, 238)       # #F5F3EE cream background
TEXT = (26, 26, 26)         # #1A1A1A black text
ACCENT = (198, 161, 91)    # #C6A15B restrained gold
SUBTLE_GREEN = (221, 232, 223)  # Light liquidity/risk accent
BANNER = (26, 26, 26)      # #1A1A1A dark banner
WHITE = (255, 255, 255)
GRAY = (120, 120, 120)     # #787878
LIGHT_CIRCLE = (225, 222, 215)  # Decorative circles
# ============================================================

# --- DIMENSIONS ---
W = 1080
H = 1350

# --- FONTS ---
FONT_DIR = os.path.expanduser("~/Library/Fonts")
SYSTEM_FONTS = "/System/Library/Fonts/Supplemental"
WIN_FONTS = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts")


def _find_font(names):
    """Return the first available font path from the candidate list."""
    search_dirs = [FONT_DIR, SYSTEM_FONTS, "/System/Library/Fonts", WIN_FONTS]
    for name in names:
        for d in search_dirs:
            path = os.path.join(d, name)
            if os.path.exists(path):
                return path
    return None


def _load_font(size, *candidates):
    """Prefer Unicode-capable fonts so Vietnamese text keeps its diacritics."""
    for path in candidates:
        if not path:
            continue
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    raise RuntimeError("No usable Unicode font found for carousel rendering.")

SERIF_BOLD_PATH = _find_font([
    "Times New Roman Bold.ttf",
    "timesbd.ttf",
    "georgiab.ttf",
    "Georgia Bold.ttf",
    "GeorgiaBold.ttf",
    "Georgia-Bold.ttf",
    "Times.ttc",
])
SERIF_ITALIC_PATH = _find_font([
    "Times New Roman Italic.ttf",
    "timesi.ttf",
    "georgiai.ttf",
    "Georgia Italic.ttf",
    "GeorgiaItalic.ttf",
    "Georgia Bold Italic.ttf",
    "Times.ttc",
])
SERIF_PATH = _find_font([
    "Times New Roman.ttf",
    "times.ttf",
    "georgia.ttf",
    "Georgia.ttf",
    "Times.ttc",
    "Arial Unicode.ttf",
])
SANS_BOLD_PATH = _find_font([
    "Arial Bold.ttf",
    "arialbd.ttf",
    "tahomabd.ttf",
    "Tahoma Bold.ttf",
    "Arial Unicode.ttf",
    "HelveticaNeue.ttc",
    "Helvetica.ttc",
    "arial.ttf",
])
SANS_PATH = _find_font([
    "Arial Unicode.ttf",
    "arial.ttf",
    "Arial.ttf",
    "tahoma.ttf",
    "Tahoma.ttf",
    "HelveticaNeue.ttc",
    "Helvetica.ttc",
    "SFNS.ttf",
])

def font_serif_bold(size):
    return _load_font(size, SERIF_BOLD_PATH, SERIF_PATH, SANS_BOLD_PATH, SANS_PATH)

def font_serif_italic(size):
    return _load_font(size, SERIF_ITALIC_PATH, SERIF_PATH, SANS_PATH)

def font_serif(size):
    return _load_font(size, SERIF_PATH, SANS_PATH)

def font_sans_bold(size):
    return _load_font(size, SANS_BOLD_PATH, SANS_PATH, SERIF_BOLD_PATH)

def font_sans(size):
    return _load_font(size, SANS_PATH, SANS_BOLD_PATH, SERIF_PATH)


# --- DRAWING HELPERS ---

def new_slide():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    return img, draw

def wrap_text(text, font, max_width):
    """Word wrap text to fit within max_width pixels."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        bbox = font.getbbox(test)
        if bbox[2] - bbox[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines

def text_width(text, font):
    bbox = font.getbbox(text)
    return bbox[2] - bbox[0]

def text_height(text, font):
    bbox = font.getbbox(text)
    return bbox[3] - bbox[1]

def draw_banner(draw, text=None):
    """Dark bottom banner with branding."""
    if text is None:
        text = BRAND_NAME
    banner_h = 80
    draw.rectangle([(0, H - banner_h), (W, H)], fill=BANNER)
    f = font_sans_bold(26)
    tw = text_width(text, f)
    draw.text(((W - tw) // 2, H - banner_h + (banner_h - 26) // 2), text, font=f, fill=WHITE)

def draw_decorative_circles(draw, cx, cy, radius=220, color=None):
    """Overlapping translucent circles (flower-of-life motif)."""
    if color is None:
        color = SUBTLE_GREEN
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    fill = (*color, 60)
    offsets = [
        (0, 0),
        (0, radius * 0.6),
        (0, -radius * 0.6),
        (radius * 0.52, radius * 0.3),
        (-radius * 0.52, radius * 0.3),
        (radius * 0.52, -radius * 0.3),
        (-radius * 0.52, -radius * 0.3),
    ]
    for dx, dy in offsets:
        x, y = int(cx + dx), int(cy + dy)
        odraw.ellipse([(x - radius, y - radius), (x + radius, y + radius)], fill=fill)
    return overlay

def draw_accent_dot(draw, x, y, r=12):
    draw.ellipse([(x - r, y - r), (x + r, y + r)], fill=ACCENT)

def draw_black_dot(draw, x, y, r=10):
    draw.ellipse([(x - r, y - r), (x + r, y + r)], fill=TEXT)

def draw_circle_outline(draw, x, y, r=10, width=2):
    draw.ellipse([(x - r, y - r), (x + r, y + r)], outline=TEXT, width=width)


# --- ILLUSTRATION GENERATORS ---

def illust_radial_dots(draw, cx, cy):
    r = 80
    for i in range(5):
        angle = math.radians(90 + i * 72)
        x = int(cx + r * math.cos(angle))
        y = int(cy + r * math.sin(angle))
        draw_black_dot(draw, x, y, 14)
    draw_accent_dot(draw, cx, cy, 16)

def illust_stacked_bars(draw, cx, cy):
    bar_h = 20
    widths = [200, 300, 250, 350, 180]
    start_y = cy - len(widths) * (bar_h + 14) // 2
    for i, w in enumerate(widths):
        y = start_y + i * (bar_h + 14)
        x = cx - w // 2
        color = ACCENT if i == 1 else LIGHT_CIRCLE
        draw.rounded_rectangle([(x, y), (x + w, y + bar_h)], radius=10, fill=color)

def illust_concentric_circles(draw, cx, cy):
    for r in [100, 75, 50]:
        draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], outline=LIGHT_CIRCLE, width=3)
    draw_accent_dot(draw, cx, cy, 20)

def illust_grid_dots(draw, cx, cy):
    spacing = 55
    for row in range(3):
        for col in range(3):
            x = cx + (col - 1) * spacing
            y = cy + (row - 1) * spacing
            if row == 1 and col == 1:
                draw_accent_dot(draw, x, y, 14)
            else:
                draw_black_dot(draw, x, y, 10)

def illust_ascending_steps(draw, cx, cy):
    step_w = 60
    step_h = 30
    steps = 5
    start_x = cx - (steps * step_w) // 2
    base_y = cy + 80
    for i in range(steps):
        x = start_x + i * step_w
        h = step_h * (i + 1)
        color = ACCENT if i == steps - 1 else LIGHT_CIRCLE
        draw.rectangle([(x, base_y - h), (x + step_w - 8, base_y)], fill=color)

def illust_triangle_dots(draw, cx, cy):
    positions = [
        (0, -70), (-50, 20), (50, 20),
        (-100, 70), (0, 70), (100, 70),
    ]
    for i, (dx, dy) in enumerate(positions):
        if i == 0:
            draw_accent_dot(draw, cx + dx, cy + dy, 16)
        else:
            draw_black_dot(draw, cx + dx, cy + dy, 12)

def illust_wave_dots(draw, cx, cy):
    points = []
    for i in range(7):
        x = cx - 180 + i * 60
        y = int(cy + math.sin(i * 1.2) * 50)
        points.append((x, y))
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=LIGHT_CIRCLE, width=3)
    for i, (x, y) in enumerate(points):
        if i == 3:
            draw_accent_dot(draw, x, y, 14)
        else:
            draw_black_dot(draw, x, y, 8)

def illust_diamond(draw, cx, cy):
    size = 80
    points = [(cx, cy - size), (cx + size, cy), (cx, cy + size), (cx - size, cy)]
    draw.polygon(points, outline=TEXT, width=3)
    draw_accent_dot(draw, cx, cy, 16)
    for px, py in points:
        draw_black_dot(draw, px, py, 8)

def illust_circles_row(draw, cx, cy):
    spacing = 65
    count = 5
    start_x = cx - (count - 1) * spacing // 2
    for i in range(count):
        x = start_x + i * spacing
        if i == 2:
            draw_accent_dot(draw, x, cy, 25)
        else:
            draw_circle_outline(draw, x, cy, 25, 3)

ILLUSTRATIONS = [
    illust_radial_dots,
    illust_stacked_bars,
    illust_concentric_circles,
    illust_grid_dots,
    illust_ascending_steps,
    illust_triangle_dots,
    illust_wave_dots,
    illust_diamond,
    illust_circles_row,
]


# --- SLIDE GENERATORS ---

def make_cover_slide(title, emphasis=None):
    """Cover/title slide."""
    img, draw = new_slide()

    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)

    fill_green = (*SUBTLE_GREEN, 45)
    fill_cream = (*LIGHT_CIRCLE, 35)
    for dx, dy in [(0, 0), (0, 130), (0, -130), (113, 65), (-113, 65), (113, -65), (-113, -65)]:
        cx, cy = W // 2 + dx, H // 2 + 50 + dy
        odraw.ellipse([(cx - 200, cy - 200), (cx + 200, cy + 200)], fill=fill_green)

    for dx, dy in [(80, 0), (0, 80), (-80, 0), (0, -80)]:
        cx, cy = W - 180 + dx, 220 + dy
        odraw.ellipse([(cx - 60, cy - 60), (cx + 60, cy + 60)], fill=fill_cream)
    for dx, dy in [(60, 0), (0, 60), (-60, 0), (0, -60)]:
        cx, cy = 160 + dx, H - 280 + dy
        odraw.ellipse([(cx - 50, cy - 50), (cx + 50, cy + 50)], fill=fill_cream)

    img_rgba = img.convert("RGBA")
    img_rgba = Image.alpha_composite(img_rgba, overlay)
    img = img_rgba.convert("RGB")
    draw = ImageDraw.Draw(img)

    dot_positions = [(120, 160), (200, 120), (160, 200), (W - 140, 180), (W - 200, 130), (W - 170, 220)]
    for x, y in dot_positions:
        draw.ellipse([(x - 4, y - 4), (x + 4, y + 4)], fill=LIGHT_CIRCLE)

    line_y = H // 2 - 180
    draw.line([(W // 2 - 60, line_y), (W // 2 + 60, line_y)], fill=ACCENT, width=4)

    margin = 100
    max_w = W - margin * 2
    f_title = font_serif_bold(72)
    f_italic = font_serif_italic(72)

    lines = wrap_text(title, f_title, max_w)
    line_h = 95
    total_h = len(lines) * line_h
    start_y = (H // 2) - total_h // 2 + 30

    for i, line in enumerate(lines):
        y = start_y + i * line_h
        if emphasis and emphasis.lower() in line.lower():
            f = f_italic
        else:
            f = f_title
        tw = text_width(line, f)
        draw.text(((W - tw) // 2, y), line, font=f, fill=TEXT)

    dot_y = start_y + len(lines) * line_h + 40
    draw_accent_dot(draw, W // 2, dot_y, 10)

    f_hint = font_sans(20)
    hint = "swipe to read"
    tw = text_width(hint, f_hint)
    draw.text(((W - tw) // 2, H - 140), hint, font=f_hint, fill=GRAY)
    arrow_y = H - 118
    arrow_x = W // 2
    draw.polygon([(arrow_x - 8, arrow_y), (arrow_x + 8, arrow_y), (arrow_x, arrow_y + 10)], fill=GRAY)

    draw_banner(draw)

    return img


def make_content_slide(number, heading, subtitle, takeaway, illust_fn):
    """Numbered content slide."""
    img, draw = new_slide()

    margin = 80
    max_w = W - margin * 2

    f_heading = font_serif_bold(60)
    heading_text = f"{number}. {heading}"
    lines = wrap_text(heading_text, f_heading, max_w)
    y = 130
    for line in lines:
        draw.text((margin, y), line, font=f_heading, fill=TEXT)
        y += 75

    y += 10
    f_sub = font_serif(34)
    sub_lines = wrap_text(subtitle, f_sub, max_w)
    for line in sub_lines:
        draw.text((margin, y), line, font=f_sub, fill=GRAY)
        y += 45

    illust_fn(draw, W // 2, H // 2 - 20)

    f_take = font_serif_italic(30)
    take_lines = wrap_text(takeaway, f_take, max_w)
    y = H - 200
    for line in take_lines:
        draw.text((margin, y), line, font=f_take, fill=TEXT)
        y += 40

    return img


def make_cta_slide(cta_text, cta_subtitle=""):
    """Final CTA slide."""
    img, draw = new_slide()

    overlay = draw_decorative_circles(draw, W // 2, H // 2 + 80, 200, SUBTLE_GREEN)
    img_rgba = img.convert("RGBA")
    img_rgba = Image.alpha_composite(img_rgba, overlay)
    img = img_rgba.convert("RGB")
    draw = ImageDraw.Draw(img)

    f_cta = font_serif_bold(54)
    margin = 100
    max_w = W - margin * 2
    lines = wrap_text(cta_text, f_cta, max_w)
    total_h = len(lines) * 70
    start_y = H // 2 - total_h // 2 - 40

    for i, line in enumerate(lines):
        y = start_y + i * 70
        tw = text_width(line, f_cta)
        draw.text(((W - tw) // 2, y), line, font=f_cta, fill=TEXT)

    if cta_subtitle:
        f_sub = font_serif_italic(34)
        tw = text_width(cta_subtitle, f_sub)
        draw.text(((W - tw) // 2, start_y + len(lines) * 70 + 20), cta_subtitle, font=f_sub, fill=GRAY)

    f_author = font_sans_bold(30)
    tw = text_width(AUTHOR_NAME, f_author)
    draw.text(((W - tw) // 2, H - 240), AUTHOR_NAME, font=f_author, fill=TEXT)

    f_role = font_sans(22)
    tw = text_width(AUTHOR_ROLE, f_role)
    draw.text(((W - tw) // 2, H - 200), AUTHOR_ROLE, font=f_role, fill=GRAY)

    draw_banner(draw)

    return img


def generate_carousel(content, output_path):
    """Generate full carousel PDF."""
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    slides = []

    # Cover
    slides.append(make_cover_slide(content["title"], content.get("title_emphasis")))

    # Content slides
    for i, slide_data in enumerate(content["slides"]):
        illust = ILLUSTRATIONS[i % len(ILLUSTRATIONS)]
        slides.append(make_content_slide(
            slide_data["number"],
            slide_data["heading"],
            slide_data["subtitle"],
            slide_data["takeaway"],
            illust,
        ))

    # CTA
    slides.append(make_cta_slide(
        content.get("cta_text", "Follow for more."),
        content.get("cta_subtitle", ""),
    ))

    # Save as PDF
    slides[0].save(
        output_path,
        "PDF",
        resolution=100.0,
        save_all=True,
        append_images=slides[1:],
    )
    print(f"Carousel saved: {output_path} ({len(slides)} slides)")

    # Also save individual PNGs for preview
    png_dir = os.path.splitext(output_path)[0] + "-slides"
    os.makedirs(png_dir, exist_ok=True)
    for i, slide in enumerate(slides):
        slide.save(os.path.join(png_dir, f"slide-{i:02d}.png"))
    print(f"Slide PNGs saved: {png_dir}/")

    return output_path


# --- DEMO CONTENT ---
DEMO_CONTENT = {
    "title": "5 Bài Học Để F0 Không Cháy Tài Khoản",
    "title_emphasis": "F0",
    "slides": [
        {
            "number": 1,
            "heading": "Đừng mua vì sợ lỡ",
            "subtitle": "FOMO không phải tín hiệu. Nó chỉ là cảm xúc mặc áo cơ hội.",
            "takeaway": "Một lệnh tốt bắt đầu bằng kịch bản, không bắt đầu bằng nỗi sợ bị bỏ lại.",
        },
        {
            "number": 2,
            "heading": "Luôn có điểm sai",
            "subtitle": "Nếu không biết sai ở đâu thì bạn không đang đầu tư. Bạn đang hy vọng.",
            "takeaway": "Điểm vô hiệu là thứ giữ tài khoản còn sống sau một lần đoán sai.",
        },
        {
            "number": 3,
            "heading": "Tỷ trọng quan trọng hơn dự đoán",
            "subtitle": "Đoán đúng nhưng vào quá tay vẫn có thể cháy khi thị trường giật ngược.",
            "takeaway": "Quản trị vốn là dây an toàn trước khi bạn nói đến lợi nhuận.",
        },
        {
            "number": 4,
            "heading": "Tin tức không phải kế hoạch",
            "subtitle": "Tin nóng chỉ cho bạn bối cảnh. Nó không thay thế hệ thống ra quyết định.",
            "takeaway": "Đọc tin để hiểu dòng tiền, không phải để bào chữa cho cảm xúc.",
        },
        {
            "number": 5,
            "heading": "Sống sót trước khi thắng lớn",
            "subtitle": "Thị trường không thưởng cho người nóng nhất. Nó thưởng cho người còn vốn.",
            "takeaway": "Tài khoản còn sống thì cơ hội còn quay lại. Tài khoản cháy thì hết quyền lựa chọn.",
        },
    ],
    "cta_text": "Lưu lại trước khi vào lệnh tiếp theo.",
    "cta_subtitle": "Gold Smith Tran - Nhà Gia Kim Forex",
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Gold Smith carousel PDF")
    parser.add_argument("--json", help="Path to JSON content file")
    parser.add_argument("--output", default="outputs/carousel-test.pdf", help="Output PDF path")
    args = parser.parse_args()

    if args.json:
        with open(args.json, encoding="utf-8") as f:
            content = json.load(f)
    else:
        content = DEMO_CONTENT

    generate_carousel(content, args.output)
