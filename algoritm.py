#!/usr/bin/env python

import heapq

def Dijkstra(G,start,end=None):
  D={}
  P={}
  Q = []
  heapq.heappush(Q,(0,start))
  while len(Q)>0:
    l,v=heapq.heappop(Q)
    if v in D: continue
    D[v]=l
    if v==end: return(D[end], P)
    for e in G[v]:
      if e[0] in D: continue
      heapq.heappush(Q,(D[v]+e[1], e[0]))
      P[e[0]]=v
  return (-1,P)

def shortestPath(G,start,end):
  D,P = Dijkstra(G,start,end)
  if D==-1: return [],-1
  Path = []
  while 1:
    Path.append(end)
    if end == start: break
    end = P[end]
  Path.reverse()
  return Path, D
