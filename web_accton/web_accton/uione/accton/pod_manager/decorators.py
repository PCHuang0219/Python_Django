from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from .sonic.models import User_Type
from django.shortcuts import render, redirect

def sonic_required(function):
    def check(request, *args, **kwargs):
        answer = User_Type.objects.filter(user_id=request.user.id)
        if(len(answer) == 0):
            return redirect("/accounts/permission-denied/")
        return function(request, *args, **kwargs)
    return check

def sonic_download_required(function):
    def check(request, *args, **kwargs):
        answer = User_Type.objects.filter(user_id=request.user.id)
        answer_data = list(answer.values())
        if(len(answer) == 0):
            return redirect("/accounts/permission-denied/")
        elif(answer_data[0]["user_type_id"] != 7 ):
            return redirect("/accounts/permission-denied/")
        return function(request, *args, **kwargs)
    return check

def job_management_required(function):
    def check(request, *args, **kwargs):
        answer = User_Type.objects.filter(user_id=request.user.id)
        answer_data = list(answer.values())
        if(len(answer) == 0):
            return redirect("/accounts/permission-denied/")
        elif(answer_data[0]["user_type_id"] == 1 or answer_data[0]["user_type_id"] == 2 or answer_data[0]["user_type_id"] == 8 or answer_data[0]["user_type_id"] == 9):
            return redirect("/accounts/permission-denied/")
        return function(request, *args, **kwargs)
    return check

def job_Submission_required(function):
    def check(request, *args, **kwargs):
        answer = User_Type.objects.filter(user_id=request.user.id)
        answer_data = list(answer.values())
        if(len(answer) == 0):
            return redirect("/accounts/permission-denied/")
        elif(answer_data[0]["user_type_id"] == 1 or answer_data[0]["user_type_id"] == 2 or answer_data[0]["user_type_id"] == 5 or answer_data[0]["user_type_id"] == 6 or answer_data[0]["user_type_id"] == 8 or answer_data[0]["user_type_id"] == 9):
            return redirect("/accounts/permission-denied/")
        return function(request, *args, **kwargs)
    return check

def tms_management_required(function):
    def check(request, *args, **kwargs):
        answer = User_Type.objects.filter(user_id=request.user.id)
        answer_data = list(answer.values())
        if(len(answer) == 0):
            return redirect("/accounts/permission-denied/")
        elif(answer_data[0]["user_type_id"] != 7 ):
            return redirect("/accounts/permission-denied/")
        return function(request, *args, **kwargs)
    return check

def pm_viewer_required(function):
    def check(request, *args, **kwargs):
        answer = User_Type.objects.filter(user_id=request.user.id)
        answer_data = list(answer.values())
        if(len(answer) == 0):
            return redirect("/accounts/permission-denied/")
        elif(answer_data[0]["user_type_id"] == 7 or answer_data[0]["user_type_id"] == 8 or answer_data[0]["user_type_id"] == 9):
            return function(request, *args, **kwargs)
        return redirect("/accounts/permission-denied/")
    return check

def pm_management_required(function):
    def check(request, *args, **kwargs):
        answer = User_Type.objects.filter(user_id=request.user.id)
        answer_data = list(answer.values())
        if(len(answer) == 0):
            return redirect("/accounts/permission-denied/")
        elif(answer_data[0]["user_type_id"] == 8 or answer_data[0]["user_type_id"] == 7):
            return function(request, *args, **kwargs)
        return redirect("/accounts/permission-denied/")
    return check