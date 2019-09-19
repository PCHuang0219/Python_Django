from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
import base64
# Create your views here.
def index(request):
    return render(request, "personal_settings/personal_settings.html")

@api_view(['GET'])
def test(request):
    print("receive test okkk")
    return Response({"ok":"finish"})

@login_required(login_url='/login/')
@api_view(['POST'])
def post_personal_image(request):
    print("receive")
    imgdata = base64.b64decode(request.data["image"].replace('data:image/jpeg;base64,',''))

    print(request.user.id)
    print(request.user)
    # filename = str(77) + '.jpg'  # I assume you have a way of picking unique filenames
    filename = str(request.user.id) + '.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    return Response({"ok":"finish"})
