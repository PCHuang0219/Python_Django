from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .mongodb.database import *
from .mongodb.projectInfo import *
from .mongodb.projectInfoDatabase import *
from ..sonic.models import *
from ..decorators import *
import os

# Create your views here.

def get_user_type(user_id):
    answer = User_Type.objects.filter(user_id=user_id)
    answer_data = list(answer.values())
    return answer_data

def get_username_by_id(user_id):
    user = str(User.objects.get(id=user_id))
    return user

@login_required(login_url="/accounts/login/")
@pm_viewer_required
def index(request):
    return render(request, "project_status.html")

@login_required(login_url="/accounts/login/")
@pm_viewer_required
def att(request):
    return render(request, "project_att.html")

@login_required(login_url="/accounts/login/")
@pm_viewer_required
def fb(request):
    return render(request, "project_fb.html")

@login_required(login_url="/accounts/login/")
@pm_viewer_required
def amozon(request):
    return render(request, "project_amozon.html")

@login_required(login_url="/accounts/login/")
@pm_viewer_required
def sonic(request):
    return render(request, "project_sonic.html")

@login_required(login_url="/accounts/login/")
@pm_viewer_required
def TR_detail(request):
    return render(request, "bug_issue_detail.html")

@login_required(login_url="/accounts/login/")
@pm_viewer_required
def NTC_tasks(request):
    return render(request, "NTC_tasks.html")

@login_required(login_url="/accounts/login/")
@pm_viewer_required
def NTC_task_detail(request):
    return render(request, "NTC_tasks_detail.html")

@login_required(login_url="/accounts/login/")
@pm_viewer_required
def submit_EPR(request):
    return render(request, "submit_EPR.html")

@login_required(login_url="/accounts/login/")
@pm_viewer_required
def EPR_page(request):
    return render(request, "EPR_list.html")

@login_required(login_url="/accounts/login/")
@pm_viewer_required
def EPR_detail(request):
    return render(request, "EPR_detail.html")
    
@api_view(['POST'])
@pm_management_required
def create_main_project_data(request):
    user_id = request.user.id 
    user = get_username_by_id(user_id)
    cust_model = request.data["cust_model"]
    project_name = request.data["project_name"]
    description = request.data["description"]
    customer = request.data["customer"]
    issue_info = Main_Project_Information(user,cust_model,project_name,description,customer)
    result = project_info_db.insert_main_project(issue_info.to_json())
    return Response({"result":result})

@api_view(['GET'])
@pm_viewer_required
def get_main_project_data(request):
    customer = request.query_params.get("customer")
    data_list = project_info_db.get_main_project_data(customer)
    return Response({"data":data_list})

@api_view(['POST'])
@pm_management_required
def create_TRR_data(request):
    user_id = request.user.id 
    user = get_username_by_id(user_id)
    data_org = request.data
    data = {"user":user,"code":data_org["code"],"bios":data_org["bios"],"diag":data_org["diag"],"cpld":data_org["cpld"],"onie":data_org["onie"], \
            "S/W":data_org["S/W"],"H/W":data_org["H/W"],"TRR_ID":data_org["TRR_ID"],"test_type":data_org["test_type"],"project":data_org["project"], \
            "test_phase":data_org["test_phase"],"boot":data_org["boot"],"profile_name":data_org["profile_name"],"module":data_org["module"], \
            "start_time":data_org["start_time"],"end_time":data_org["end_time"]}
    issue_info = Bug_Issue_Information(data)
    result = project_info_db.insert_TRR(issue_info.to_json())
    return Response({"result":result})

@api_view(['GET'])
@pm_viewer_required
def get_project_list(request):
    data = project_info_db.get_project_list()
    return Response({"data":data})

@api_view(['POST'])
@pm_management_required
def change_TRR_status(request):
    data_list = dict(request.data)
    TRR_ID = data_list["TRR_ID"][0]
    status = data_list["status"][0]
    MEDF = data_list["MEDF"][0]
    content_list = []
    if status == "Verified":
        content = data_list["content"][0]
    elif status == "Assigned":
        content_list_org = data_list["content[]"]
        for content in content_list_org:
            TD = content.split("/")[0]
            TC = content.split("/")[1]
            engineer = content.split("/")[2]
            MEDF = content.split("/")[3]
            Task_ID = content.split("/")[4]
            project = content.split("/")[5]
            TRR_ID = content.split("/")[6]
            content_list.append({"TD":TD,"TC":TC,"owner":engineer,"MEDF":MEDF,"status":"Allocated","Task_ID":Task_ID, \
                                "project":project,"TRR_ID":TRR_ID})
        tasks_info_db.insert_tasks(content_list)
        content = ""
    else:
        content = ""
    return Response({"result":project_info_db.update_TRR_status(TRR_ID,status,content,MEDF)})

@api_view(['POST'])
@pm_management_required
def create_TRR_description(request):
    user_id = request.user.id
    user = get_username_by_id(user_id)
    user_type_id = get_user_type(user_id)[0]["user_type_id"]
    project = request.data["project"]
    TRR_ID = request.data["TRR_ID"]
    description = request.data["description"]
    comment_info = Bug_Issue_Comment(user,project,TRR_ID,description)
    result = project_info_db.create_TRR_description(comment_info.to_json())
    return Response({"result":result})

@api_view(['POST'])
@pm_management_required
def create_TRR_discussion(request):
    user_id = request.user.id
    user = get_username_by_id(user_id)
    user_type_id = get_user_type(user_id)[0]["user_type_id"]
    project = request.data["project"]
    TRR_ID = request.data["TRR_ID"]
    issue = request.data["issue"]
    mail = request.data["mail"]
    comment_info = Bug_Issue(user,project,TRR_ID,issue,mail)
    result = project_info_db.create_TRR_discussion(comment_info.to_json())
    return Response({"result":result})

@api_view(['GET'])
@pm_viewer_required
def get_TRR_discussion(request):
    TRR_ID = request.query_params.get("TRR_ID")
    data = project_info_db.get_TRR_discussion(TRR_ID)
    return Response({"data":data})

@api_view(['GET'])
@pm_viewer_required
def get_TRR_description(request):
    project = request.query_params.get("project")
    TRR_ID = request.query_params.get("TRR_ID")
    data_list = project_info_db.get_TRR_description(TRR_ID)
    return Response({"data":data_list})

@api_view(['GET'])
@pm_viewer_required
def get_TRR_detail(request):
    user_id = request.user.id
    user = get_username_by_id(user_id)
    project = request.query_params.get("project")
    TRR_ID = request.query_params.get("TRR_ID")
    data_list = project_info_db.get_TRR_detail(project,TRR_ID)
    return Response({"data":data_list,"user":user})

@api_view(['POST'])
def update_TRR_content(request):
    TRR_ID = request.data["TRR_ID"]
    changeType = request.data["type"]
    content = request.data["content"]
    result = project_info_db.update_TRR(TRR_ID,changeType,content)
    return Response({"result":result})

@api_view(['GET'])
def get_TD_list(request):
    data = testcase_info_db.get_all_TD_list()
    return Response({"data":data})

@api_view(['GET'])
def get_TC_list(request):
    TD_ID = request.query_params.get("TD_ID")
    data = testcase_info_db.get_all_TC_list_by_TD(TD_ID)
    return Response({"data":data})

@api_view(['GET'])
def get_selection_by_condition(request):
    condition = request.query_params.get("data")
    data = project_info_db.get_selection_by_condition(condition)
    return Response({"data":data})

@api_view(['GET'])
def get_views_by_condition(request):
    condition = request.query_params.get("data")
    if condition == "":
        data = project_info_db.get_TRR_list()
    else:
        data = project_info_db.get_views_by_condition(condition)
    return Response({"data":data})

@api_view(["POST"])
def test(request):
    TRR_ID = request.data["TRR_ID"]
    content = request.data["content"]
    project_info_db.update_history_by_TRR_ID(TRR_ID,content)
    return Response({"data":"data"})

@api_view(["POST"])
def save_EPR_attachment(request):
    data = dict(request.POST)
    attachment_list = []
    project = data["project"][0]
    EPR_ID = EPR_info_db.get_EPR_ID(project)
    file_list = data['fileList'][0]
    count = file_list.count(',')
    path = "/home/jlo/share/EPR/" + project + "/" + EPR_ID + "/"
    try:
        os.makedirs(path)
    except :
        pass
    for i in range(0,count+1):
        description = file_list.split(',')[i]
        FILE = request.FILES.get(description)
        fname = path + FILE.name
        attachment_description = {"description":description,"file_path":fname,"file_name":FILE.name,"file_size":FILE.size}
        attachment_list.append(attachment_description)
        with open(fname, 'wb') as f:
            for c in FILE.chunks():
                f.write(c)
    result = EPR_info_db.insert_EPR_attachment(EPR_ID,attachment_list)
    return Response({"data":EPR_ID})

@api_view(["POST"])    
def save_EPR_content(request):
    data = request.data
    content = {"headline":data["headline"],"severity":data["severity"],"CSC":data["CSC"],
                "rate":data["rate"],"problem":data["problem"],"expect":data["expect"],
                "procedure":data["procedure"],"user":data["user"],"project":data["project"]}
    EPR_ID = data["EPR_ID"]
    result = EPR_info_db.update_EPR_content_by_ID(EPR_ID,content)
    return Response({"data":result})

@api_view(["GET"])
def get_EPR_list(request):
    EPR_ID = request.query_params.get("EPR_ID")
    if (EPR_ID):
        condition = {"EPR_ID":EPR_ID}
    else:
        condition = {}
    data_list = EPR_info_db.get_EPR_list(condition)
    return Response({"data":data_list})

@api_view(["GET"])
def get_tasks_list(request):
    owner = request.query_params.get("owner")
    if (owner):
        condition = {"owner":owner}
    else:
        condition = {}
    data_list = tasks_info_db.get_tasks_list(condition)
    return Response({"data":data_list})

@api_view(["GET"])
def get_task_detail_by_task_ID(request):
    Task_ID = request.query_params.get("Task_ID")
    condition = {"Task_ID":Task_ID}
    data = tasks_info_db.get_task_detail_by_task_ID(condition)
    return Response({"data":data})