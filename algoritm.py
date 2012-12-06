#!/usr/bin/env python

# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117228
from priodict import priorityDictionary

def Dijkstra(G,start, end=None):
  D = {}
  P = {}
  Q = priorityDictionary()
  Q[start] = 0
  for v in Q:
    D[v]=Q[v]
    if v==end : break
    for w,e in G[v]:
      newlen = D[v] + e
      if not w in Q or newlen < Q[w]:
        Q[w]=newlen
        P[w]=v
 # print D[end]
  #print P
  return(D, P)

def shortestPath(G,start,end):
  D,P = Dijkstra(G,start,end)
  Path = []
  while 1:
    Path.append(end)
    if end == start: break
    end = P[end]
  Path.reverse()
  return Path

#G = [[(1,10), (2,30)],          [(0,10), (2,10)],          [(0,30), (1,10)]]
#P = shortestPath(G,0,2)
#print P
