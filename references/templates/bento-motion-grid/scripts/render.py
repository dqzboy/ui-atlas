#!/usr/bin/env python3
"""Render draw(frame / fps) to 1440x1080 PNGs; run from a copied template."""
import argparse
import io
import math
import os
from multiprocessing import Process
from pathlib import Path
import shutil

STAGE = {'width': 1024, 'height': 768}
SCALE = 2.8125


def browser_options(chrome=None):
    candidates = [chrome] if chrome else [
        shutil.which('google-chrome'), shutil.which('chromium'),
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    ]
    options = {'args': ['--force-color-profile=srgb', '--font-render-hinting=none']}
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            options['executable_path'] = str(candidate)
            break
    if chrome and 'executable_path' not in options:
        raise FileNotFoundError(f'Browser not found: {chrome}')
    return options


def draw_frame(page, time):
    # Flush layout and compositing before capturing a newly rebuilt DOM.
    page.evaluate('''async t => {
        window.draw(t);
        await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
    }''', time)


def worker(worker_index, args, count):
    from playwright.sync_api import sync_playwright
    from PIL import Image
    errors = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(**browser_options(args.chrome))
        page = browser.new_page(viewport=STAGE, device_scale_factor=SCALE)
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto(Path('index.html').resolve().as_uri())
        page.evaluate('document.fonts.ready')
        for index in range(worker_index * count // args.workers,
                           (worker_index + 1) * count // args.workers):
            draw_frame(page, index / args.fps)
            if errors:
                raise RuntimeError('\n'.join(errors))
            with Image.open(io.BytesIO(page.screenshot())) as frame:
                frame.convert('RGB').resize((1440, 1080), Image.Resampling.LANCZOS).save(
                    Path(args.out) / f'{index:05d}.png', compress_level=1)
        browser.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fps', type=float, default=120)
    parser.add_argument('--seconds', type=float, default=24)
    parser.add_argument('--workers', type=int, default=min(6, max(1, (os.cpu_count() or 4) - 2)))
    parser.add_argument('--out', default='frames')
    parser.add_argument('--chrome')
    args = parser.parse_args()
    if not all(math.isfinite(v) and v > 0 for v in (args.fps, args.seconds)) or args.workers < 1:
        parser.error('fps, seconds and workers must be positive')
    count = round(args.fps * args.seconds)
    if count < 1:
        parser.error('duration must include at least one frame')
    if not Path('index.html').is_file():
        parser.error('run from the copied template folder containing index.html')
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    if any(out.iterdir()):
        parser.error('output directory must be empty; choose another --out')
    args.workers = min(args.workers, count)
    processes = [Process(target=worker, args=(index, args, count)) for index in range(args.workers)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    if any(process.exitcode != 0 for process in processes):
        raise SystemExit('Rendering failed; partial frames remain for inspection.')
    if len(list(out.glob('*.png'))) != count:
        raise SystemExit('Frame count does not match the requested duration.')
    print(f'{count} frames at {args.fps:g} fps; {count / args.fps:g} seconds')


if __name__ == '__main__':
    main()
