from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def index(request):

    messages.info(request, 'Your password has been changed successfully!')
    return render(request, "jsonform/jsonform.html")


#def index(request):
#    return render(request, "jsonform/jsonform.html")

