from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#def index(request):
#    return HttpResponse(
#        "Hello, world. You are at monitor -> dc_back index page.")

def index(request):
    return render(request, 'dc_back/dc_back.html')