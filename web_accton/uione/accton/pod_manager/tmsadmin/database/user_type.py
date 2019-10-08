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
        
    def get_all_user_type_data(self):
        try:
            user_data = User_Type.objects.all()
            user_list = list(user_data.values())
            return Response({"data":user_list},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        