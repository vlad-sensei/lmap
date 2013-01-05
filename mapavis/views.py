# Create your views here.
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
import datetime

def hello(request): 
  now = datetime.datetime.now()
  html = "<html> <body> Hello World! It is now <b>%s</b>. </body></html>" % now
  return HttpResponse(html)

from django.shortcuts import render_to_response
from django.template import Template, Context

from nodes import *

data=StoreNodes('mapavis/linkoping_map.osm')
nodes = ClipNodes(data.nodes,58.3984,58.3990,15.5733,15.5760)

def mapapp(request):
 # print request.POST
  global nodes
  global data
  isPost=False
  Path=[]
  Dist=0
  if request.method =="POST":
    print request.POST
    #if (u'dstlng' in request.POST) and (u'srclng' in )
    if True:
      # isPost=True
      sNode=findId(float(request.POST['srclat']),float(request.POST['srclng']));
      dNode=findId(float(request.POST['dstlat']),float(request.POST['dstlng']));
      if sNode!=None and dNode!=None:
        print sNode
        print dNode
        isPost=True
        Path, Dist = shortestPath(G,sNode,dNode)
        print Path
        print Dist
  DM=[]
  if Dist>0:
    for osmid in Path:
      DM+=["points.push(new google.maps.LatLng("+ str(data.nodes[osmid].lat) +","+ str( str(data.nodes[osmid].lng))+ "));"]
      print osmid
      print data.nodes[osmid].lat
      print data.nodes[osmid].lng
  print DM

  c = Context({'AGMAPS_API_KEY': 'AIzaSyCRYOHyi6AtLspaRRPz7TqNuEXMs5NVHDk', 'COORDS': CN.nodes.values(), 'ROADS': R.roads.values(), 'CD': data.nodes,\
      'DM':DM, 'DIST':Dist})
  c.update(csrf(request));
  #print c
  #print request.POST
  return render_to_response('mapavis/mapapp.html', c)

