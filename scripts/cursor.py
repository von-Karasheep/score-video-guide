"""Interpolate only supplied, verified real score anchors; no equal-width fallback."""
from bisect import bisect_right
import math

def position(time, anchors):
 if not anchors:raise ValueError('anchors required')
 for q in anchors:
  if q.get('verified') is not True or not q.get('evidence'):raise ValueError('unverified anchor')
  if not all(math.isfinite(float(q[k])) for k in ('time','x')):raise ValueError('nonfinite anchor')
 ts=[float(q['time']) for q in anchors]
 if any(b<=a for a,b in zip(ts,ts[1:])):raise ValueError('time must increase')
 if not math.isfinite(time):raise ValueError('invalid time')
 j=max(0,min(len(anchors)-1,bisect_right(ts,time)-1));a=anchors[j]
 if j==len(anchors)-1 or time<ts[0]:return a['system'],float(a['x'])
 b=anchors[j+1]
 if a['system']!=b['system'] or a.get('hold'):return a['system'],float(a['x'])
 u=(time-a['time'])/(b['time']-a['time'])
 return a['system'],a['x']+u*(b['x']-a['x'])
