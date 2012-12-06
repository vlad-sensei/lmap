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
    for l in G[v]:
      newlen = D[v] + l[1]
      if not l[0] in Q or newlen < Q[l[0]]:
        Q[l[0]]=newlen
        P[l[0]]=v
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

#G = {123:[(321,10), (111,30)],          321:[(123,10), (111,10)],         111:[(123,30), (321,10)]}
#P = shortestPath(G,123,111)
#print P
