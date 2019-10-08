from ...sonic.models import *
from django.contrib.auth.models import User
import sys
from rest_framework.response import Response
from rest_framework import status

class User_Database():
    def __init__(self):
        pass
    
    def get_username_by_id(self,user_id):
        try:
            user = str(User.objects.get(id=user_id))
            return user
        except Exception as e:
            return Response({"error":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete_user(self,user_id):
        try:
            user_type = User_Type.objects.get(user_id=user_id)
            user_type.delete()
            user = User.objects.get(id=user_id)
            user.delete()
            return Response({"status":"ok"},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error":"error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_user_data_from_database(self):
        try:
            user_list = User.objects.all()
            user_data = list(user_list.values())
            return user_data
        except Exception as e:
            print(e)
            return []


    def get_user_information(self,user_data,user_id):
        image_path = "./user_image/" + str(user_id) + ".jpg"
        if(not os.path.isfile(image_path)):
            image_path = "./user_image/none.jpg"
        with open(image_path, "rb") as image_file:
            encoded_image_string = base64.b64encode(image_file.read())
        for user in user_data:
            if(user["id"] == user_id):
                return [user["first_name"],user["last_name"],str(encoded_image_string)]
        return ["","",""]
    
    def get_user_personal_image(self,user_id):
        try:
            image_path = "./user_image/" + str(user_id) + ".jpg"
            if(not os.path.isfile(image_path)):
                image_path = "./user_image/none.jpg"
            with open(image_path, "rb") as image_file:
                encoded_image_string = base64.b64encode(image_file.read())
            return str(encoded_image_string)
        except Exception as e:
            print(e)
            return Response({"error":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)