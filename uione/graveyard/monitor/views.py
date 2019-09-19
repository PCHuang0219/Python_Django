from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'monitor/monitor.html')


def index2(request):
    return HttpResponse("Hi")

# Create your views here.
def index3(request):
    return HttpResponse\
        ("Hello, world. You are at pod_manager->monitor index page.")

#def index3(request):
#    return render(request, 'monitor.html')




"""
from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'books/search_results.html',
                      {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')
"""