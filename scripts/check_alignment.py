"""Structural gate only; call check(bars). Times in source seconds, x in scan pixels.
Each bar: start,end,left,right,beats[{time,x,verified,evidence}],free_time.
The gate cannot validate whether the supplied evidence is truthful.
"""
import math

def check(bars):
 errors=[];warnings=[];previous=None
 for i,b in enumerate(bars):
  tag=f'bar[{i}]'
  try:
   start,end,left,right=[float(b[k]) for k in ('start','end','left','right')]
   if not all(math.isfinite(v) for v in (start,end,left,right)) or end<=start or right<=left:
    raise ValueError('invalid bounds')
   if previous is not None and start<previous:errors.append(tag+': overlapping or nonmonotonic time')
   previous=end
   if b.get('free_time'):
    if not b.get('evidence'):errors.append(tag+': free-time evidence missing')
    continue
   beats=b['beats']
   if not beats:raise ValueError('missing beats')
   ts=[float(q['time']) for q in beats];xs=[float(q['x']) for q in beats]
   if not all(math.isfinite(v) for v in ts+xs):raise ValueError('nonfinite anchor')
   if not all(start<=t<end for t in ts):errors.append(tag+': beat outside bar')
   if not all(left<=x<=right for x in xs):errors.append(tag+': x outside bar')
   if any(y<=x for x,y in zip(ts,ts[1:])):errors.append(tag+': beat time not strictly increasing')
   if any(y<=x for x,y in zip(xs,xs[1:])):errors.append(tag+': beat x not strictly increasing')
   if any(q.get('verified') is not True or not q.get('evidence') for q in beats):errors.append(tag+': unverified anchor')
   if b.get('position_method')!='score_anchors':errors.append(tag+': actual score anchors required')
   intervals=[y-x for x,y in zip(ts,ts[1:]+[end])]
   if min(intervals)>0 and max(intervals)/min(intervals)>1.25:
    warnings.append(tag+': beat-duration spread >25%; inspect audio, do not auto-smooth')
  except (KeyError,TypeError,ValueError) as exc:errors.append(tag+': '+str(exc))
 return {'structural_pass':not errors,'errors':errors,'review_warnings':warnings,'music_verified':False}
