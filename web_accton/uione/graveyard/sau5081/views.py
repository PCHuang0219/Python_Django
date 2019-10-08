from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    #return HttpRequest("Hi This is SAU5081 page.")
    return render(request, "sau5081/sau5081.html")