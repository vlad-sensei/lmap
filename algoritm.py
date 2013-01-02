#!/usr/bin/env python

# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117228
#from priodict import priorityDictionary

#def Dijkstraold(G,start, end=None):
#  D = {}
#  P = {}
#  Q = priorityDictionary()
#  Q[start] = 0
#  for v in Q:
#    D[v]=Q[v]
#    if v==end : break
#    for l in G[v]:
#      newlen = D[v] + l[1]
#      if not l[0] in Q or newlen < Q[l[0]]:
#        Q[l[0]]=newlen
#        P[l[0]]=v
  #print D[end]
  #print P
#  return(D[end], P)

import heapq

def Dijkstra(G,start,end=None):
  D={}
  P={}
  Q = []
  heapq.heappush(Q,(0,start))
  while len(Q)>0:
#    print D
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

#G = {123:[(321,10), (111,30)], 321:[(123,10), (111,10)], 111:[(123,30), (321,10)], 1000:[]}
#P = shortestPath(G,123,111)
#print P
#P = shortestPath(G,123,1000)
#print P
