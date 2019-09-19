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

class Article_Tag_Database():
    def create_Article_Tag(self,article_id,tag_list):
        try:
            _article = Article.objects.get(id=article_id)
            for tag in tag_list:
                article_tag = Article_Tag(article=_article,tag_name=tag)
                article_tag.save()
        except Exception as e:
            print(e)
            return Response({"error":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get_all_tag_name(self):
        # tag_list = Article_Tag.objects.order_by('tag_name').values('tag_name').distinct()
        tag_list = Article_Tag.objects.values('tag_name').annotate(count=Count('tag_name'))
        tag_data = list(tag_list)
        print(tag_data)
        return Response({"status":tag_data},status=status.HTTP_200_OK)

        
