#!/usr/bin/env python3
"""Generate the four minimalist wallpapers for a Samsung Galaxy A55 (1080x2340)."""
import os
from PIL import Image, ImageDraw

W, H = 1080, 2340
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wallpapers")


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def gradient(top, bottom):
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    t, b = hex_rgb(top), hex_rgb(bottom)
    for y in range(H):
        k = y / (H - 1)
        d.line([(0, y), (W, y)], fill=tuple(round(t[i] + (b[i] - t[i]) * k) for i in range(3)))
    return img


def conduccion():
    img = gradient("#0B0F14", "#13222E")
    d = ImageDraw.Draw(img)
    y = int(H * 0.62)
    d.rectangle([W * 0.30, y, W * 0.70, y + 4], fill=hex_rgb("#2EC4B6"))
    return img


def trabajo():
    img = gradient("#EEF0F2", "#D6DBE0")
    d = ImageDraw.Draw(img)
    y = int(H * 0.80)
    d.rectangle([W * 0.42, y, W * 0.58, y + 4], fill=hex_rgb("#6B7785"))
    return img


def familia():
    img = gradient("#F8EADB", "#EFD2B8")
    d = ImageDraw.Draw(img)
    r, cx, cy = 150, W // 2, int(H * 0.68)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=hex_rgb("#F2B38A"))
    return img


def relax():
    img = gradient("#0B1530", "#1C2648")
    d = ImageDraw.Draw(img)
    r, cx, cy = 110, int(W * 0.5), int(H * 0.30)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=hex_rgb("#E8E4F5"))
    # carve a crescent with a circle of the local background colour
    # (the gradient is vertical, so sample outside the moon at the cut's height)
    cut = img.getpixel((10, cy - 20))
    d.ellipse([cx - r + 70, cy - r - 20, cx + r + 70, cy + r - 20], fill=cut)
    return img


MODES = {"conduccion": conduccion, "trabajo": trabajo, "familia": familia, "relax": relax}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, fn in MODES.items():
        path = os.path.join(OUT, f"{name}.png")
        fn().save(path, optimize=True)
        print("wrote", path)
