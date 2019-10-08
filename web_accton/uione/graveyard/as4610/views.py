from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "as4610/as4610.html")
