from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from ..decorators import *
from .database.count import Database_Count,Database_Table_Size
from .database.user_type import User_Type_Database
from .database.user import User_Database

user_database = User_Database()
user_type_database = User_Type_Database()
database_count = Database_Count()
database_table_size = Database_Table_Size()

# Create your views here.
@login_required(login_url='/accounts/login/')
@tms_management_required
def index(request):
    return render(request, "tmsadmin/tmsadmin.html")

@login_required(login_url='/accounts/login/')
@tms_management_required
def usermgmt(request):
    return render(request, "tmsadmin/usermgmt.html")

@login_required(login_url="/accounts/login/")
@tms_management_required
def ixia_schedule(request):
    return render(request, "tmsadmin/usermgmt.html")


def get_every_table_data_count(request):
    '''
    print(database_count.get_user_count())
    print(database_count.get_article_count())
    print(database_count.get_message_count())
    print(database_count.get_message_user_count())
    print(database_count.get_article_tag_count())
    return ""
    '''

@api_view(['GET'])
def get_username_by_id(request):
    user_id = request.query_params.get("user_id")
    return Response({"user_name":user_database.get_username_by_id(user_id)},status=status.HTTP_200_OK)

@api_view(['POST'])
def update_user_priority(request):
    user_id = request.data["user_id"]
    user_type_id = request.data["user_type_id"]
    return user_type_database.update_user_type(user_id,user_type_id)

@api_view(['GET'])
def get_user_type_table(request):
    return user_type_database.get_all_user_type_data()

@api_view(['GET'])
def get_account_list(request):
    return Response({"status":user_database.get_user_data_from_database()},status=status.HTTP_200_OK)

@api_view(['POST'])
def delete_user(request):
    user_id = request.data["user_id"]
    return user_database.delete_user(user_id)