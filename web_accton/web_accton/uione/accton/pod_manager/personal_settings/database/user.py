from ...sonic.models import *
from django.contrib.auth.models import User
import sys
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers

class User_Database():
    def __init__(self):
        pass
    
    def get_username_by_id(self,username,user_type_id):
        try:
            user = User.objects.filter(username=username).values()
            for object in user :
                object["user_type"] = user_type_id
            return user
        except Exception as e:
            return Response({"error":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def save_information_by_username(self,username,key,value):
        try:
            user = User.objects.get(username=username)
            if key == "first_name":
                user.first_name = value
            elif key == "last_name":
                user.last_name = value
            user.save()
            return Response({"status":"ok"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)