#!/usr/bin/env python3
"""Capture chosen seconds; --native --webp preserves 2880x2160 rendered pixels."""
import argparse
import io
import math
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright
from render import browser_options, draw_frame, STAGE, SCALE


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('times', type=float, nargs='+')
    parser.add_argument('--chrome')
    parser.add_argument('--out', default='out')
    parser.add_argument('--native', action='store_true')
    parser.add_argument('--webp', action='store_true')
    args = parser.parse_args()
    if any(not math.isfinite(t) or t < 0 for t in args.times):
        parser.error('times must be finite and nonnegative')
    Path(args.out).mkdir(parents=True, exist_ok=True)
    errors = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(**browser_options(args.chrome))
        page = browser.new_page(viewport=STAGE, device_scale_factor=SCALE)
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto(Path('index.html').resolve().as_uri())
        page.evaluate('document.fonts.ready')
        for time in args.times:
            draw_frame(page, time)
            if errors:
                raise RuntimeError('\n'.join(errors))
            with Image.open(io.BytesIO(page.screenshot())) as captured:
                frame = captured.convert('RGB')
                if not args.native:
                    frame = frame.resize((1440, 1080), Image.Resampling.LANCZOS)
                target = Path(args.out) / f'still_{time:g}.{ "webp" if args.webp else "png"}'
                frame.save(target, quality=98, method=6) if args.webp else frame.save(target)
                print(target.resolve())
        browser.close()


if __name__ == '__main__':
    main()
