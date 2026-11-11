#!/usr/bin/env bash
# Usage: bash scripts/encode.sh [frames_dir] [out_dir] [input_fps]
set -euo pipefail
frame_dir=${1:-frames}
output_dir=${2:-out}
input_fps=${3:-120}
if ! [[ "$input_fps" =~ ^[1-9][0-9]*$ ]]; then
  echo 'input_fps must be a positive integer matching render.py --fps' >&2
  exit 1
fi
mkdir -p "$output_dir"
master="$output_dir/grid_${input_fps}.mp4"
ffmpeg -v error -n -framerate "$input_fps" -i "$frame_dir/%05d.png" -c:v libx264 -preset slow -crf 14 -pix_fmt yuv420p -movflags +faststart -an "$master"
ffprobe -v error -count_frames -show_entries stream=width,height,r_frame_rate,nb_read_frames,pix_fmt:format=duration -of compact "$master"
if (( input_fps > 60 )); then
  delivery="$output_dir/grid_60.mp4"
  ffmpeg -v error -n -framerate "$input_fps" -i "$frame_dir/%05d.png" -vf fps=60 -c:v libx264 -preset slow -crf 14 -pix_fmt yuv420p -movflags +faststart -an "$delivery"
  ffprobe -v error -count_frames -show_entries stream=width,height,r_frame_rate,nb_read_frames,pix_fmt:format=duration -of compact "$delivery"
fi
