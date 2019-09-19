from django.shortcuts import render
from django.http import HttpResponseRedirect
from .abcforms import CdefgForm


def hijk(request):
    if request.method == 'POST':
        form = CdefgForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = CdefgForm()

    return  render(request, 'djangoform/djangoform.html',
                   {'form':form})


# Create your views here.
"""
#def get_name(request):
# http://127.0.0.1:8000/djangoform
def hijk_sample_one(request):


    if request.method == 'POST':
        form = CdefgForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = CdefgForm()

    return  render(request, 'djangoform/debug.html',
                   {'form':form,
                    'body':request.body,
                    'path':request.path,
                    'bool_value': True,
                    'int_value': 100,
                    'str_value': "this is value 3"})



#def get_name(request):
# http://127.0.0.1:8000/djangoform
def hijk(request):
    if request.method == 'POST':
        form = CdefgForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = CdefgForm()

    return  render(request, 'djangoform/djangoform.html',
                   {'form':form})
                   
"""
