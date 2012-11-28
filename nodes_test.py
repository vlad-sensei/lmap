import random
import unittest
from nodes import *

def node_inside ( node , min_lat , max_lat , min_lng , max_lng ):
  return ( min_lat < node.lat and node.lat < max_lat and min_lng < node.lng and node.lng < max_lng )


def test_all_nodes_inside(self):
  nodes = dict ()
  nodes [ 1 ] = Node (1 , - 10 , - 10 )
  nodes [ 2 ] = Node (2 , -5 , - 5 )
  selected_nodes = ClipNodes ( nodes , - 10 , 10 , - 10 , 10 )
  self.assertFalse ( nodes == selected_nodes.nodes )


class TestClipNodes(unittest.TestCase):
  def test_empty_nodes ( self ):
    nodes = dict ()
    selected_nodes = ClipNodes ( nodes ,-10 , 10 ,-10 , 10 )
    self.assertEqual ( nodes , selected_nodes.nodes )

  def test_empty_clip_nodes ( self ):
    nodes = dict ()
    nodes [ 1 ] = Node (1 ,-10 ,-10 )
    nodes [ 2 ] = Node (2 ,-5 ,-5 )
    selected_nodes = ClipNodes ( nodes , 0 , 10 , 0 , 10 )
    self.assertFalse ( selected_nodes.nodes )

  def test_random ( self ):
    nodes = dict ()
    for i in range ( 1000 ):
      node = Node (i , random.randint (-180 , 180 ) , random.randint (-90 , 90 ) )
      nodes [ i ] = node
   # for nd in nodes.values() : print str(nd.id) + " " + str(nd.lat) + " " + str(nd.lng)

    min_lat = random.randint (-90 , 90 )
    min_lng = random.randint (-180 , 180 )
    max_lat = min_lat + random.randint (0 , 90-min_lat )
    max_lng = min_lng + random.randint (0 , 180-min_lng )

    #print  str(min_lat) + " <---> " +  str(max_lat) + " :: " +  str(min_lng) + " <---> " +  str(max_lng)

    selected_nodes = ClipNodes ( nodes , min_lat , max_lat , min_lng , max_lng )

    #for nd in selected_nodes.nodes.values() : print str(nd.id) + " " + str(nd.lat) + " " + str(nd.lng)
    for n in nodes.values ():
      if n.id in selected_nodes.nodes:
        self.assertTrue ( node_inside (n , min_lat , max_lat , min_lng , max_lng ) )
      else:
        if  node_inside (n , min_lat , max_lat , min_lng , max_lng ): 
          print "Not in " + str(n.id)
        self.assertFalse ( node_inside (n , min_lat , max_lat , min_lng , max_lng ) )

    test_all_nodes_inside(self)


if __name__== "__main__":
  unittest.main ()
