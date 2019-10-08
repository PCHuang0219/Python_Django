from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'polls/post_list.html')

def tempindex(request):
    return HttpResponse("Hello, world. You are at the polls index.")