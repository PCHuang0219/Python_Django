from ..models import *
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from itertools import chain
from django.db import connection
import base64
import os
from django.db.models import Count
from datetime import datetime, timezone
import pytz
from rest_framework.response import Response
from rest_framework import status
from .user import *
from ..utility.time import *
from .message_user import *

message_user_database = Message_User_Database()
user_database = User_Database()
class Message_Database():
    def __init__(self):
        pass

    def create_Message(self,user_id,article_id,message_id,content):
        try:
            _user = User.objects.get(id=user_id)
            _article = Article.objects.get(id=article_id)
            if(message_id == "NULL"):
                message = Message(user=_user,article=_article, \
                            content=content,awesome_number="0",bad_number="0")
            else:
                print("have message id")
                _message = Message.objects.get(id=message_id)
                message = Message(user=_user,article=_article,main_message=_message, \
                    content=content,awesome_number="0",bad_number = "0")
            message.save()
            return Response({"status":"ok"},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete_message_method(self,user_id,message_id,judge_type):
        try:
            Message_User.objects.filter(user_id=user_id,message_id=message_id,judge_type=judge_type).delete()
            message = Message.objects.get(id=message_id)
            if(judge_type == "awesome"):
                awesome_number = message.awesome_number
                message = Message.objects.filter(id=message_id).update(awesome_number=awesome_number-1)
            else:
                bad_number = message.bad_number
                message = Message.objects.filter(id=message_id).update(bad_number=bad_number-1)
            return Response({"status":"ok"},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"status":"you don't have "  + judge_type + "on this"},status=status.HTTP_200_OK)

    def put_message_method(self,user_id,message_id,article_id,type_name):
        try:
            output = Message_User.objects.get(user_id=user_id,message_id=message_id,judge_type=type_name)
            return Response({"status":"you have " + type_name +" on this"},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            message = Message.objects.get(id=message_id)
            if(type_name == "awesome"):
                awesome_number = message.awesome_number
                message = Message.objects.filter(id=message_id).update(awesome_number=awesome_number+1)
            else:
                bad_number = message.bad_number
                message = Message.objects.filter(id=message_id).update(bad_number=bad_number+1)
            message_user_database.create_Message_User(user_id,message_id,article_id,type_name)
        return Response({"status":"ok"},status=status.HTTP_200_OK)

    def get_message_by_article_id(self,article_id):
        user_data = user_database.get_user_data_from_database()
        message_list = Message.objects.filter(article_id=article_id)
        message_data = list(message_list.values())
        for message in message_data:
            message["first_name"],message["last_name"],message["personal_image"] = user_database.get_user_information(user_data,message["user_id"])
        return Response({"data":message_data},status=status.HTTP_200_OK) 
