from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .database.user import User_Database
from .database.user_type import User_Type_Database
from .database.user_mongodb import *

user_db = User_Database()
user_type_db = User_Type_Database()
user_mongodb = User_Info_Database()

# Create your views here.
def index(request):
    return render(request, "personal_settings/personal_settings.html")

@api_view(['GET'])
def get_user_data(request):
    user =request.user
    user_id =request.user.id
    user_type = user_type_db.get_user_type_by_user_id(user_id)
    data = user_db.get_username_by_id(user,user_type)
    return Response({"data":data})

@login_required(login_url='/login/')
@api_view(['POST'])
def save_personal_image(request):
    user = str(request.user)
    img = request.data["img"]
    result = user_mongodb.update_personal_image(img,user)
    return Response({"result":result})

@login_required(login_url='/login/')
@api_view(['GET'])
def get_personal_image(request):
    user = str(request.user)
    data = user_mongodb.get_personal_image(user)
    return Response({"data":data})

@login_required(login_url='/login/')
@api_view(['POST'])
def save_user_information(request):
    user = str(request.user)
    key = request.data["type"]
    value = request.data["content"]
    result = user_db.save_information_by_username(user,key,value)
    return result