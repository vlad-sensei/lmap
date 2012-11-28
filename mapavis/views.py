# Create your views here.
from django.http import HttpResponse
import datetime

def hello(request): 
  now = datetime.datetime.now()
  html = "<html> <body> Hello World! It is now <b>%s</b>. </body></html>" % now
  return HttpResponse(html)

from django.shortcuts import render_to_response
from django.template import Template, Context

from nodes import *


def mapapp(request):
  data=StoreNodes('mapavis/linkoping_map.osm')
  nodes = ClipNodes(data.nodes,58.3984,58.3990,15.5733,15.5760)
  c = Context({'AGMAPS_API_KEY': 'AIzaSyCRYOHyi6AtLspaRRPz7TqNuEXMs5NVHDk', 'COORDS': CN.nodes.values(), 'ROADS': R.roads.values(), 'CD': CN.nodes })
  return render_to_response('mapavis/mapapp.html', c)
