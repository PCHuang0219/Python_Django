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

class Message_User_Database():
    def __init__(self):
        pass

    def create_Message_User(self,user_id,message_id,article_id,judge_type):
        try:
            _user = User.objects.get(id=user_id)
            _message = Message.objects.get(id=message_id)
            _article = Article.objects.get(id=article_id)
            message_user = Message_User(user=_user,message=_message,article=_article,judge_type=judge_type)
            message_user.save()
        except Exception as e:
            print(e)
            return Response({"error":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_judge_message_by_article_id(self,user_id,article_id):
        try:
            message_user_list = Message_User.objects.filter(user_id=user_id,article_id=article_id)
            message_user_data = list(message_user_list.values())
            return  JsonResponse(message_user_data, safe=False) 
        except Exception as e:
            print(e)
            return  Response({"error":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
