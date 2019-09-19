from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def index(response):
#    return HttpResponse("Home --> Manage Page")

def index(request):
    return render(request, 'monitor/monitor.html')