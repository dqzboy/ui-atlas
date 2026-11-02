#!/usr/bin/env python3
"""Search the bundled UI reference index. Uses only the Python standard library."""
import argparse,json,pathlib

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('query',nargs='?',default='');p.add_argument('--id',dest='entry_id');p.add_argument('--json',action='store_true');a=p.parse_args();root=pathlib.Path(__file__).resolve().parent.parent
 data=json.loads((root/'references/catalog.json').read_text());q=a.query.strip().casefold()
 items=[x for x in data['items'] if (x['id']==a.entry_id if a.entry_id else all(w in ' '.join(str(x[k]) for k in ['id','name','english','summary','category_title']).casefold() for w in q.split()))]
 if a.json:print(json.dumps(items,ensure_ascii=False,indent=2));return
 if not items:p.exit(1,'未找到匹配条目，请换用分类或中英文名称。\n')
 for x in items:
  print(f"{x['id']} | {x['name']} / {x['english']}")
  print(f"  要点: {x['summary']}\n  例句: {x['prompt']}")
  print(f"  说明: {root}/references/{x['category']}.md#{x['slug']}")
  print(f"  GIF: {root/x['gif']}\n  六帧图: {root/x['filmstrip']}\n")
if __name__=='__main__':main()
