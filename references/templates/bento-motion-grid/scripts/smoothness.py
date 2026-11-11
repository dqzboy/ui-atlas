#!/usr/bin/env python3
"""Flag per-card frame-difference spikes for visual inspection, not a pass/fail proof."""
import argparse
from concurrent.futures import ProcessPoolExecutor
import os
from pathlib import Path
import re
import numpy as np
from PIL import Image


def differences(pair):
    first, second, layout = pair
    def load(path):
        with Image.open(path) as frame:
            return np.asarray(frame.convert('L').resize((512, 384)), dtype=np.float32)
    delta = np.abs(load(first) - load(second))
    return [delta[y//2:(y+h)//2, x//2:(x+w)//2].mean() for _, x, y, w, h in layout]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('frames', nargs='?', default='frames')
    parser.add_argument('--fps', type=float, default=120)
    parser.add_argument('--skip-intro-seconds', type=float, default=2)
    parser.add_argument('--workers', type=int, default=min(6, os.cpu_count() or 1))
    args = parser.parse_args()
    if not np.isfinite(args.fps) or args.fps <= 0 or args.workers < 1:
        parser.error('fps and workers must be positive')
    if not np.isfinite(args.skip_intro_seconds) or args.skip_intro_seconds < 0:
        parser.error('skip-intro-seconds must be finite and nonnegative')
    files = sorted(Path(args.frames).glob('*.png'))
    skip = round(args.fps * args.skip_intro_seconds)
    if len(files) < skip + 3:
        parser.error('not enough frames after the intro; render longer or reduce --skip-intro-seconds')
    if [p.name for p in files] != [f'{i:05d}.png' for i in range(len(files))]:
        parser.error('frames must be a consecutive sequence starting at 00000.png')
    source = Path('index.html').read_text()
    layout = [(name, *map(int, box)) for name, *box in re.findall(
        r"\['(\w+)',(\d+),(\d+),(\d+),(\d+),'\w*'\]", source)]
    if not layout:
        parser.error('no widget rectangles found in the template layout table')
    pairs = [(a, b, layout) for a, b in zip(files, files[1:])]
    with ProcessPoolExecutor(max_workers=args.workers) as executor:
        matrix = np.array(list(executor.map(differences, pairs, chunksize=20)))
    big_count = 0
    for column, (name, *_) in enumerate(layout):
        values = matrix[:, column]
        spikes = []
        for index in range(skip, len(values)):
            neighbours = np.concatenate([values[max(0, index-6):index], values[index+1:index+7]])
            if values[index] > 1 and values[index] > 4 * np.median(neighbours) + .2:
                spikes.append((index, round(float(values[index]), 2)))
        big = [spike for spike in spikes if spike[1] > 2]
        big_count += len(big)
        print(f'{name:10s} max {values[skip:].max():5.2f}  spikes {len(spikes):3d}  big {big[:6]}')
    print(f'BIG SPIKES: {big_count}; inspect flagged frames and cycle boundaries visually.')


if __name__ == '__main__':
    main()
