#!/usr/bin/env python3
"""Rebuild original-video GIFs and AI-readable filmstrips. Requires ffmpeg and Pillow."""
import argparse,concurrent.futures,json,pathlib,subprocess

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-dir',type=pathlib.Path,required=True);p.add_argument('--only',help='Entry id or category');p.add_argument('--jobs',type=int,default=2);p.add_argument('--force',action='store_true');a=p.parse_args()
 root=pathlib.Path(__file__).resolve().parent.parent
 data=json.loads((root/'references/catalog.json').read_text());items=[x for x in data['items'] if not a.only or a.only in (x['id'],x['category'])]
 if not items:raise SystemExit('No entries match --only')
 missing=[str(a.source_dir/x['source_video']) for x in items if not (a.source_dir/x['source_video']).is_file()]
 if missing:raise SystemExit('Missing source videos: '+', '.join(sorted(set(missing))))
 from PIL import Image,ImageDraw
 def render(x):
  src=a.source_dir/x['source_video'];gif=root/x['gif'];sheet=root/x['filmstrip'];gif.parent.mkdir(parents=True,exist_ok=True);sheet.parent.mkdir(parents=True,exist_ok=True)
  start=x['start'];duration=x['end']-start;meta=next(m for m in data['videos'] if m['id']==x['video_id']);width=800 if meta['width']>meta['height'] else 600
  crop_top=int(x.get('crop_top_px',0))
  if crop_top<0 or crop_top>=meta['height'] or crop_top%2:raise ValueError(f'Invalid crop_top_px: {x["id"]}')
  crop_filter=f'crop=iw:ih-{crop_top}:0:{crop_top},' if crop_top else ''
  expected_height=round((meta['height']-crop_top)*width/meta['width']/2)*2
  refresh_gif=a.force or not gif.exists()
  if not refresh_gif:
   with Image.open(gif) as existing:refresh_gif=existing.width != width or existing.height != expected_height
  if refresh_gif:
   temp=gif.with_suffix('.tmp.gif')
   filt=f'{crop_filter}fps=10,scale={width}:-2:flags=lanczos,split[a][b];[a]palettegen=max_colors=128:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle'
   subprocess.run(['ffmpeg','-v','error','-y','-threads','1','-ss',str(start),'-i',str(src),'-t',str(duration),'-filter_complex_threads','1','-filter_complex',filt,'-loop','0',str(temp)],check=True);temp.replace(gif)
  if a.force or refresh_gif or not sheet.exists():
   import io
   frames=[];times=[start+duration*(.03+i*.94/5) for i in range(6)]
   for t in times:
    b=subprocess.check_output(['ffmpeg','-v','error','-threads','1','-ss',str(t),'-i',str(src),'-frames:v','1','-vf',f'{crop_filter}scale={640 if width==800 else 480}:-2','-f','image2pipe','-vcodec','mjpeg','-threads','1','-'])
    frames.append(Image.open(io.BytesIO(b)).convert('RGB'))
   w,h=frames[0].size;canvas=Image.new('RGB',(3*w,2*(h+30)),'#e4e8ef');draw=ImageDraw.Draw(canvas)
   for i,(im,t) in enumerate(zip(frames,times)):
    cx=i%3*w;cy=i//3*(h+30);canvas.paste(im,(cx,cy+30));draw.text((cx+10,cy+8),f'{i+1} / 6   source {int(t)//60:02}:{t%60:04.1f}',fill='#172033')
   canvas.save(sheet,quality=90)
  print(x['id'],f'{duration:.1f}s',f'{gif.stat().st_size/1048576:.2f}MB',flush=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=max(1,a.jobs)) as ex:list(ex.map(render,items))
if __name__=='__main__':main()
