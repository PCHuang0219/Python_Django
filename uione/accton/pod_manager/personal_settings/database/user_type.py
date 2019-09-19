from ...sonic.models import *
from django.contrib.auth.models import User
import sys
from rest_framework.response import Response
from rest_framework import status

class User_Type_Database():
    def __init__(self):
        pass

    def update_user_type(self,user_id,user_type_id):
        try:
            if User_Type.objects.filter(user=user_id) :
                User_Type.objects.filter(user=user_id).update(user_type_id=user_type_id)
            else :
                _user = User.objects.get(id=user_id)
                create_user_type = User_Type(user=_user,user_type_id=user_type_id)
                create_user_type.save()
            return Response({"status":"ok"},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get_user_type_by_user_id(self,user_id):
        try:
            user_type_id_org = User_Type.objects.filter(user=user_id).values("user_type_id")
            user_type_id = [entry for entry in user_type_id_org]  # converts ValuesQuerySet into Python list
            user_type_id = user_type_id[0]["user_type_id"]
            type_name = ''
            if user_type_id == 1 or user_type_id == "":
                type_name = "General User"
            elif user_type_id == 2:
                type_name = "Subscriber"
            elif user_type_id == 3:
                type_name = "Lab-Controller"
            elif user_type_id == 4:
                type_name = "Lab-Master"
            elif user_type_id == 5:
                type_name = "Reseller"
            elif user_type_id == 6:
                type_name = "Channel_Parnets"
            elif user_type_id == 7:
                type_name = "TMS Admin"
            elif user_type_id == 8:
                type_name = "TMS_Project Manager"
            elif user_type_id == 9:
                type_name = "TMS_Project Viewer"
            return type_name
        except Exception as e:
            print(e)
            return Response({"error":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)