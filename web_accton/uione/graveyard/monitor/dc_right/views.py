from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#def index(request):
#    return HttpResponse(
#        "Hello, world. You are at monitor -> dc_right index page.")

def index(request):
    return render(request, 'dc_right/dc_right.html')

