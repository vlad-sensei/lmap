#!/usr/bin/env python

# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117228
from priodict import priorityDictionary

def Dijkstra(G,start, end=None):
  D = P = {}
  Q = priorityDictionary()
  Q[start] = 0

  for v in Q:
    D[v]=Q[v]
    if v==end : break

    for w,e in G:
      newlen = D[v] + e
      if w not in Q or newlen < Q[w]:
        Q[w]=newlen
        P[w]=v

  return(D, P)
