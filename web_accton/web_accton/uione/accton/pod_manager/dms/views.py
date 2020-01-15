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

project_info_db = Project_Info_Database()

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
    return render(request, "dms-overviews.html")

    
def uploadFile(request):
    print(request.FILES['file'])
    file=request.FILES['image']
    filename=file.filename.split('.')[0]+'_new.'+file.filename.split('.')[-1]
    path=app.config['UPLOAD_FOLDER']+'/'+filename
    print (file.filename,filename,path)
    file.save(path) 
    print ('GET=',file.filename)
    print ('UPLOAD=',filename,'#'*50)
    return Response({"path":path})

@api_view(['GET'])
@pm_viewer_required
def get_main_project_data(request):
    customer = request.query_params.get("customer")
    data_list = project_info_db.get_main_project_data(customer)
    return Response({"data":data_list})

@api_view(['POST'])
@pm_management_required
def create_bug_data(request):
    user_id = request.user.id 
    user = get_username_by_id(user_id)
    project = request.data["project"]
    start_time = request.data["start_time"]
    end_time = request.data["end_time"]
    TRR_ID = request.data["TRR_ID"]
    issue_info = Bug_Issue_Information(user,project,start_time,end_time,TRR_ID)
    result = project_info_db.insert_issue(issue_info.to_json())
    return Response({"result":result})

@api_view(['POST'])
@pm_management_required
def create_bug_data(request):
    user_id = request.user.id 
    user = get_username_by_id(user_id)
    project = request.data["project"]
    start_time = request.data["start_time"]
    end_time = request.data["end_time"]
    TRR_ID = request.data["TRR_ID"]
    module = request.data["module"]
    issue_info = Bug_Issue_Information(user,project,start_time,end_time,TRR_ID,module)
    result = project_info_db.insert_issue(issue_info.to_json())
    return Response({"result":result})

@api_view(['POST'])
@pm_management_required
def create_bug_detail_data(request):
    user_id = request.user.id 
    user = get_username_by_id(user_id)
    data_org = request.data
    data = {"code":data_org["code"],"bios":data_org["bios"],"diag":data_org["diag"],"cpld":data_org["cpld"],"onie":data_org["onie"], \
            "S/W":data_org["S/W"],"H/W":data_org["H/W"],"TRR_ID":data_org["TRR_ID"],"test_type":data_org["test_type"],"project":data_org["project"], \
            "test_phase":data_org["test_phase"],"boot":data_org["boot"],"profile_name":data_org["profile_name"],"module":data_org["module"]}
    print(data)
    result = project_info_db.insert_issue_detail(data)
    return Response({"result":result})

@api_view(['GET'])
@pm_viewer_required
def get_project_list(request):
    data = project_info_db.get_project_list()
    return Response({"data":data})

@api_view(['GET'])
@pm_viewer_required
def get_bug_information(request):
    data_list = project_info_db.get_bug_information()
    return Response({"data":data_list})

@api_view(['POST'])
@pm_management_required
def change_bug_status(request):
    TRR_ID = request.data["TRR_ID"]
    status = request.data["status"]
    return Response({"result":project_info_db.update_bug_status(TRR_ID,status)})

@api_view(['POST'])
@pm_management_required
def create_bug_detail(request):
    user_id = request.user.id
    user = get_username_by_id(user_id)
    user_type_id = get_user_type(user_id)[0]["user_type_id"]
    project = request.data["project"]
    TRR_ID = request.data["TRR_ID"]
    description = request.data["description"]
    comment_info = Bug_Issue_Comment(user,project,TRR_ID,description)
    result = project_info_db.create_bug_detail(comment_info.to_json())
    return Response({"result":result})

@api_view(['POST'])
@pm_management_required
def create_bug_issue(request):
    user_id = request.user.id
    user = get_username_by_id(user_id)
    user_type_id = get_user_type(user_id)[0]["user_type_id"]
    project = request.data["project"]
    TRR_ID = request.data["TRR_ID"]
    issue = request.data["issue"]
    comment_info = Bug_Issue(user,project,TRR_ID,issue)
    result = project_info_db.create_bug_issue(comment_info.to_json())
    return Response({"result":result})

@api_view(['GET'])
@pm_viewer_required
def get_bug_description(request):
    TRR_ID = request.query_params.get("TRR_ID")
    data = project_info_db.get_bug_description(TRR_ID)
    return Response({"data":data})

@api_view(['GET'])
@pm_viewer_required
def get_bug_issue(request):
    project = request.query_params.get("project")
    TRR_ID = request.query_params.get("TRR_ID")
    data_list = project_info_db.get_bug_issue(TRR_ID)
    return Response({"data":data_list})

@api_view(['GET'])
@pm_viewer_required
def get_bug_detail(request):
    project = request.query_params.get("project")
    TRR_ID = request.query_params.get("TRR_ID")
    data_list = project_info_db.get_bug_detail(project,TRR_ID)
    return Response({"data":data_list})

@api_view(['POST'])
def update_bug_detail_status(request):
    bug_id = request.data["id"]
    status = request.data["status"]
    result = project_info_db.update_bug_detail_status(bug_id,status)
    return Response({"result":result})

@api_view(['POST'])
def update_TRR_content(request):
    TRR_ID = request.data["TRR_ID"]
    changeType = request.data["type"]
    content = request.data["content"]
    if changeType == "Module":
        result = project_info_db.update_issue(TRR_ID,content)
    else:
        result = project_info_db.update_issue_detail(TRR_ID,changeType,content)
    return Response({"result":result})