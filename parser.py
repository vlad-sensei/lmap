from imposm.parser import OSMParser

mp='map.osm'

class NodeCounter(object):
  counter = 0
  def count(self, coords):
    self.counter += len(coords)

nodes = NodeCounter()
p = OSMParser(coords_callback=nodes.count)
p.parse(mp)

class UNodeCounter(object):
  counter = 0
  def count(self, nodes):
    self.counter+=len(nodes)

unodes = UNodeCounter()
p = OSMParser(nodes_callback=unodes.count)
p.parse(mp)

class HighwayCounter(object):
  highways = 0
  def ways(self, ways):
    for osmid, tags, refs in ways:
      if 'highway' in tags:
        self.highways += 1

hw = HighwayCounter()
p = OSMParser(concurrency=4, ways_callback=hw.ways)
p.parse(mp)

class WayCounter(object):
  ws = 0
  def ways(self, ways): self.ws+=len(ways)

wc = WayCounter()
p = OSMParser(concurrency=4, ways_callback=wc.ways)
p.parse(mp)

class RelCounter(object):
  count =0
  def rels(self, relations): self.count+=len(relations)

relc = RelCounter()
p = OSMParser(concurrency=4, relations_callback=relc.rels)
p.parse(mp)

class BC(object):
  c=0
  def b(self, nodes):
    for osmid, tags, cs in nodes:
      if 'building' in tags: self.c+=1

bs=BC()
p = OSMParser(concurrency=4, nodes_callback=bs.b)
p.parse(mp)

print( str(nodes.counter) + " Nodes")
print( str(nodes.counter - unodes.counter) + " Untagged Nodes")
print( str(hw.highways) + " Highways")
print( str(wc.ws) + " Ways")
print( str(relc.count) + " Relations")
print( str(bs.c) + " Buildings (from nodes)")

