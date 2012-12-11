

from imposm.parser import OSMParser

mp='map.osm'

class Node:
  def __init__(self, id, lng, lat):
    self.id = id
    self.lng = lng
    self.lat = lat
    if not (lat <= 90 and lat >= -90 and lng <= 180 and lng >= -180) :
      print "Invalid coords"
      raise NameError('Coords out of range')

class StoreNodes(object):
  def __init__(self, osmfile):
    self.nodes = dict()
    self.bounds = dict()
    self.bounds["min_lat"] =-9999 # 58.3773000
    self.bounds["max_lat"] = 9999 # 58.4236000
    self.bounds["min_lng"] =-9999 # 15.5207000
    self.bounds["max_lng"] = 9999 # 15.6248000

    p=OSMParser(coords_callback = self.coords_callback)
    p.parse(osmfile)

  def coords_callback(self, coords):
    for osmid, lng, lat in coords:
      node = Node(osmid, lng, lat)
      self.nodes[osmid]= node
      self.bounds["min_lat"] = min(self.bounds["min_lat"], lat)
      self.bounds["max_lat"] = max(self.bounds["max_lat"], lat)
      self.bounds["min_lng"] = min(self.bounds["min_lng"], lng)
      self.bounds["max_lng"] = max(self.bounds["max_lng"], lng)

N=StoreNodes(mp)
# print Nodes
# for node in N.nodes.values(): print node.id


class ClipNodes(object):
  def __init__(self, nodes, minlat, maxlat, minlng, maxlng):
    self.nodes = dict()
    self.bounds = dict()
    self.minlat=minlat
    self.maxlat=maxlat
    self.minlng=minlng
    self.maxlng=maxlng

    self.bounds["min_lat"] =-9999 # 58.3773000
    self.bounds["max_lat"] = 9999 # 58.4236000
    self.bounds["min_lng"] =-9999 # 15.5207000
    self.bounds["max_lng"] = 9999 # 15.6248000

    for node in nodes.values():
      if self.minlng < node.lng and self.minlat < node.lat and self.maxlng > node.lng and self.maxlat > node.lat:
        new_node = Node(node.id, node.lng, node.lat)
        self.nodes[node.id]= new_node
        self.bounds["min_lat"] = min(self.bounds["min_lat"], node.lat)
        self.bounds["max_lat"] = max(self.bounds["max_lat"], node.lat)
        self.bounds["min_lng"] = min(self.bounds["min_lng"], node.lng)
        self.bounds["max_lng"] = max(self.bounds["max_lng"], node.lng)

CN=ClipNodes(N.nodes,58.3984,58.3990 ,15.5733 ,15.576)
# print Nodes
#for node in CN.nodes.values(): print node.id

class Road:
  global N
  def __init__(self, id, nodes):
    self.coords = []
    self.id=id
    self.nodes=nodes
    for node in self.nodes:
      self.coords+= [{'lat': N.nodes[node].lat, 'lng': N.nodes[node].lng}]

class StoreRoads :
  def __init__ ( self , osmfile) :
    self.roads = dict ()
    p = OSMParser(ways_callback = self.ways_callback)
    p.parse(osmfile)
  def ways_callback (self,ways):
    for osmid, way, refs in ways:
      road = Road(osmid, refs)
      self.roads[osmid] = road

R=StoreRoads(mp)
#for road in R.roads.values():
#  print road.id
#  for coords in road.coords: print coords

from math import sqrt, radians, sin, cos, asin

def length_haversine(p1,p2):
  lat1, lat2, lng1, lng2 = map(radians, [p1.lat, p2.lat, p1.lng, p2.lng])
  dlat, dlng = lat2-lat1, lng2-lng1
  a=sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlng/2)**2
  return 6372797.560856 * 2*asin(sqrt(a))

def GetG(r):
  g={}
  for road in r.roads.values():
    for i in range(len(road.nodes)-1):
      id1,id2=road.nodes[i],road.nodes[i+1]
      l=length_haversine(N.nodes[id1], N.nodes[id2])
      if not id1 in g: g[id1]=[]
      if not id2 in g: g[id2]=[]
      g[id1]+=[(id2,l)]
      g[id2]+=[(id1,l)]
  return g

G=GetG(R)

#print G

from algoritm import *

#P, dist =shortestPath(G,345660400,283653684)
#print dist
#print P

def findId(lat, lng):
  res=None;
  dist=10000000
  for node in N.nodes.values():
    ds = sqrt((lat-node.lat)**2+(lng-node.lng)**2)
    if ds<dist:
      dist=ds
      res=node
  return res.id
