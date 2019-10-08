from django.shortcuts import render
from django.http import HttpResponse
from .models import Node
from rest_framework import viewsets
from .Serializers import  NodeSerializer
from .utility.connect import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
#def index(request):
#    return HttpResponse("Home --> Network Page")

#def index(request):
#    return render(request, 'network/network.html')


"""
1. read data from model, based on REST framework
2. display to screen
3. Done
"""

class NodeViewSet(viewsets.ModelViewSet):
    #queryset = Node.objects.all().order_by('-date_created')
    # this one works but still NG
    #queryset = Node.objects.all().order_by('-date_created')[0:0]

    #queryset = Node.objects.all().get(node_name="this ")
    queryset = Node.objects.all().filter(id=1)
    serializer_class = NodeSerializer

def index(request):
    return render(request, "network/network.html")

@api_view(['POST'])
def command(request):
    command = request.data['command']
    connect_log = connectRemoteCMD(command)
    print(connect_log)
    return Response({"log":connect_log})

