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

user_database = User_Database()
class Article_Database():
    def __init__(self):
        pass

    def create(self,user_id,title,content):
        try:
            _user = User.objects.get(id=user_id)
            article = Article(user=_user,content=content,awesome_number="0", \
                            view_number="0",title=title)
            article.save()
            return article.id
        except Exception as e:
            print(e)
            return Response({"error":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_Article_Tag_from_article_ID(self,article_id):
        try:
            article_list = Article_Tag.objects.filter(article_id=article_id)
            return article_list
        except Exception as e:
            print(e)
            return Response({"error":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_Article_Tag_from_tag_name(self,tag_name):
        try:
            article_list = Article_Tag.objects.filter(tag_name=tag_name)
            return article_list
        except Exception as e:
            print(e)
            return Response({"error":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_list_by_tag(self,start_index,tag_name):
        article_list = Article_Tag.objects.select_related("article__user").filter(tag_name=tag_name).values\
        ('article__id','article__title','article__content','article__awesome_number','article__time',\
        'article__view_number','article__user_id','tag_name','article__user__id','article__user__first_name','article__user__last_name')
        for article_info_index in article_list:
            article_info_index["personal_image"] = user_database.get_user_personal_image(article_info_index["article__user__id"])
            reply_number = len(list(Message.objects.filter(article_id=article_info_index['article__id']).values()))
            article_info_index["reply_number"] = reply_number
            article_info_index["time"] = change_time_mode(str(article_info_index["article__time"]))
        
        return JsonResponse(list(article_list)[start_index:start_index+10], safe=False) 

    def get_list(self,start_index=0):
        article_list = Article.objects.all().order_by('-time').values('id','title','content'\
            ,'awesome_number','time','view_number','user_id','user__first_name','user__last_name')
        article_list = list(article_list)[start_index:start_index+10]
        
        for article_info_index in article_list:
            article_info_index["personal_image"] = user_database.get_user_personal_image(article_info_index["user_id"])
            reply_number = len(list(Message.objects.filter(article_id=article_info_index['id']).values()))
            article_info_index["reply_number"] = reply_number
            article_info_index["time"] = change_time_mode(str(article_info_index["time"]))

        return JsonResponse(list(article_list), safe=False) 

    def put_views_by_article_id(self,article_id):
        try:
            article = Article.objects.get(id=article_id)
            view_number = article.view_number
            new_article = Article.objects.filter(id=article_id).update(view_number=view_number+1)
            return  Response({"status":"ok"},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return  Response({"error":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_info_by_id(self,article_id):
        article_list = Article.objects.filter(id=article_id)
        article_data = list(article_list.values())
        tag_list = Article_Tag.objects.filter(article_id=article_id)
        tag_data =  list(tag_list.values())
        user_data = user_database.get_user_data_from_database()
        article_data = article_data[0]
        article_data["author_first_name"],article_data["author_last_name"],article_data["author_personal_image"] = user_database.get_user_information(user_data,article_data["user_id"])
        article_data["tag"] = tag_data
        return Response({"data":article_data},status=status.HTTP_200_OK) 

    def get_list_length(self):
        return Response({"article_total_number":Article.objects.count()},status=status.HTTP_200_OK) 