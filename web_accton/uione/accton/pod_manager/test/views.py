from django.shortcuts import render
from django.http import HttpResponse
import logging
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import sys
import threading
import os, sys
import uuid
import requests
import json
from datetime import datetime
from .utility.Test import *
from .utility.TestInfo import *
from .utility.Job import *
from .utility.JobQueue import *
from .utility.FetchAllJobData import *
from .utility.FilterLog import *
from .utility.Config import *
from .database.UpdateDatabase import *
from .database.GetDatabase import *
from .database.SaveDatabase import *
from ..decorators import *
from django.contrib.auth.decorators import login_required
from .mongodb.jobInfo import * 
from .mongodb.jobInfoDatabase import * 
from .mongodb.labInfoDatabase import *
from .mongodb.IXIAInfo import *
from .database.conn_jenkins import Jenkins_conn

jenkins = Jenkins_conn()
test_info = TestInfo()
get_database = GetDatabase()
job_info_database = Job_Info_Database()
lab_info = Lab_Info_Database()
device_info = Device_Info_Data()

@login_required(login_url='/accounts/login/')
@job_management_required
def management(request):
    return render(request, "test/jobTable.html")

@login_required(login_url='/accounts/login/')
@job_Submission_required
def index(request):
    return render(request, "test/jobSubmit.html")

@login_required(login_url='/accounts/login/')
@job_management_required
def detail(request):
    return render(request, "test/jobDetail.html")

@login_required(login_url='/accounts/login/')
@job_Submission_required
def status(request):
    return render(request, "test/jobStatus.html")

@login_required(login_url='/accounts/login/')
@job_Submission_required
def log(request):
    return render(request, "test/jobLog.html")

@login_required(login_url='/accounts/login/')
@job_Submission_required
def image(request):
    return render(request, "test/jobImageChoose.html")

@login_required(login_url='/accounts/login/')
@job_Submission_required
def jenkins_views(request):
    return render(request, "jenkinsViews.html")

@login_required(login_url='/accounts/login/')
@job_Submission_required
def lab_status_views(request):
    return render(request, "labInformation.html")

@login_required(login_url='/accounts/login/')
@job_Submission_required
def device_management_views(request):
    return render(request ,"deviceManagement.html")

@api_view(["POST"])
def save_IXIA_Information(request):
    data_list = dict(request.data)
    Lab = data_list["Lab"][0]
    model = data_list["model"][0]
    port_number = data_list["port_number"][0]
    status = data_list["status"][0]
    ToRack = data_list["ToRack"][0]
    ToDevice = data_list["ToDevice"][0]
    owner = data_list["owner"][0]
    description = data_list["description"][0]

    ixia_info = IXIA_Information(Lab,model,port_number,status,ToRack,ToDevice,owner,description)
    data_id = lab_info.insert(ixia_info)
    return Response({"data_id":str(data_id)})

@api_view(['GET'])
def get_IXIA_Information(request):
    data_list = lab_info.get_list()
    return Response({"IXIA_Info":data_list})

@api_view(['POST'])
def update_IXIA_Information(request):
    data_list = dict(request.data)
    Lab = data_list["Lab"][0]
    model = data_list["model"][0]
    port_number = data_list["port_number"][0]
    status = data_list["status"][0]
    ToRack = data_list["ToRack"][0]
    ToDevice = data_list["ToDevice"][0]
    owner = data_list["owner"][0]
    description = data_list["description"][0]
    
    ixia_info = IXIA_Information(Lab,model,port_number,status,ToRack,ToDevice,owner,description)
    data_id = lab_info.update_IXIA_Info(ixia_info)
    return Response({"data_id":str(data_id)})

@api_view(['GET'])
def update_IXIA_Change_View(request):
    data_list = dict(request.data)
    Lab = request.query_params.get("Lab")
    model = request.query_params.get("model")
    port_number = request.query_params.get("port_number")
    data = lab_info.update_IXIA_view(Lab,model,port_number)
    return Response({"data":data})

@api_view(['GET'])
def get_ixia_schedule(request):
    data_list = []
    org_list = lab_info.get_ixia_schedule()
    for data in org_list:
        data = json.loads(data)
        data_list.append(data)
    return Response({"data":data_list})

@api_view(['GET'])
def get_week_date(request):
    data = lab_info.get_two_week_datetime()
    return Response({"data":data})

@api_view(['GET'])
def update_ixia_config(request):
    data = lab_info.update_ixia_config()
    return Response({"data":data})

@api_view(['POST'])
def create_ixia_schedule(request):
    data_list = dict(request.data)
    owner = str(request.user)
    card = data_list["card"][0]
    port = data_list["port"][0]
    start_time = data_list["start_time"][0]
    end_time = data_list["end_time"][0]
    cable = data_list["cable"][0]
    toDevice = data_list["toDevice"][0]
    ixia_info = IXIA_Schedule(owner,card,port,start_time,end_time,cable,toDevice)
    result = lab_info.check_ixia_status(ixia_info.to_json())
    if result == "Failed":
        return Response({"data":"Failed"})
    elif result == "Success":
        data = lab_info.insert_ixia_schedule(ixia_info.to_json())
        if data :
            return Response({"data":"Success"})
        else :
            return Response({"data":"Failed"})

@api_view(['GET'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def get_DUT_list(request):
    r = requests.get("http://" + IP_ADDRESS + ":" + PORT + "/getDUTList", data = {}, verify = False)
    DUT_list = r.json()['DUTList']
    return Response({"DUT_list":DUT_list})

@api_view(['GET'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def get_testcases_list(request):
    r = requests.get("http://" + IP_ADDRESS + ":" + PORT + "/getTestcasesList", data = {} , verify = False)
    testcases_list = r.json()['testcases_list']
    #testcases_list = json.loads(testcases_list)
    print(testcases_list)
    return Response({"testcases_list":testcases_list})

@api_view(['GET'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def get_now_test_log_from_server(request):
    job_id = request.query_params.get('job_id')
    platform = request.query_params.get('platform')
    if(job_id == ''):
        return Response({"job_log":""})
    # print(platform)
    if platform == "Facebook":
        r = requests.get("http://" + FB_IP_ADDRESS + ":" + FB_PORT + "/jobLog", data =  {'job_id':job_id,'platform':platform}, verify = False)
    else:
        r = requests.get("http://" + IP_ADDRESS + ":" + PORT + "/jobLog", data =  {'job_id':job_id}, verify = False)
    log_data = r.json()['log']
    return Response({"job_log":log_data})

@api_view(['GET'])

def get_platform_by_job_id(request):
    job_id = request.query_params.get('job_id')
    if job_id == '' :
        return Response({"platform":""})
    return Response(job_info_database.get_platform_by_job_id(job_id))
    
@api_view(['GET'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def get_current_test_name(request):
    job_id = request.query_params.get('job_id')
    if(job_id == ''):
        return Response({"name":""})
    return Response({"name":job_info_database.get_running_test_by_job_id(job_id)})

@api_view(['POST'])
def receive_finished_log_from_server(request):
    complete_log = json.loads(request.data['complete_log'])
    brief_log = json.loads(request.data['brief_log'])
    job_id = request.data['job_id']
    test_id = request.data['test_id']
    complete_log_path = "./../../../../log/" + str(job_id) +"/" + str(test_id) +"/" + "complete_log.txt"
    brief_log_path = "./../../../../log/" + str(job_id) +"/" + str(test_id) +"/" +"brief_log.txt"
    try:
        os.makedirs("./../../../../log/" + str(job_id) +"/" + str(test_id) +"/")
    except FileExistsError:
        # directory already exists
        pass
    with open(complete_log_path,'w') as f:
        for line in complete_log :
            f.write(line)
    with open(brief_log_path,'w') as f:
        for line in brief_log :
            f.write(line)
    return Response({"status":job_info_database.update_test_log_path_by_id(job_id,test_id,complete_log_path)})

@api_view(['POST'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def get_test_case(request):
    platform = request.data['platform']
    topology = request.data['topology']
    model = request.data['model']
    test_name_list = test_info.get_by_topo_platform(topology,platform)
    return Response({"testData":test_name_list,"platform":platform})

@api_view(['GET'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def get_test_log(request):
    job_id = request.query_params.get('job_id')
    test_id = request.query_params.get('test_id')
    complete_log_path = "./../../../../log/" + str(job_id) +"/" + str(test_id) +"/" + "complete_log.txt"
    if(job_id == ''):
        return Response({"log":""})
    if os.path.isfile(complete_log_path):
        with open(complete_log_path,'r') as f:
            content = f.readlines()
        content = [x.strip() for x in content] 
        return Response({"log":content})
    return Response({"log":""})

@api_view(['GET'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def get_job_status(request):
    job_id = request.query_params.get('job_id')
    if(job_id == ''):
        return Response({"job_status":""})
    return Response({"job_status":job_info_database.get_job_status_by_id(job_id)})

@api_view(['GET'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def get_job_table(request):
    return Response({"data":job_info_database.get_list()})

@api_view(['POST'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def submit_testcase(request):
    user_id = request.user.id 
    data_list = dict(request.data)
    if(data_list == {}):
        return Response({"job_id":"no test"})
    test_list = data_list['testList[]']
    job_name = data_list['job_name'][0]
    job_description = data_list['job_description'][0]
    job_model = data_list['model'][0]
    job_topo = data_list['topology'][0]
    job_platform = data_list['platform'][0]
    image_version = data_list['image_version'][0]

    job_info = Job_Information(job_name,job_description,job_platform,job_model,user_id,job_topo,image_version,test_list)
    job_id = job_info_database.insert(job_info)
    if job_platform == "Facebook":
        r = requests.post("http://" + FB_IP_ADDRESS + ":" + FB_PORT +"/submitJob",\
        data = {"job_id":str(job_id)},verify = False)
    else:
        r = requests.post("http://" + IP_ADDRESS + ":" + PORT +"/submitJob",\
        data = {"job_id":str(job_id)},verify = False)
    return Response({"job_id":str(job_id)})

@api_view(['GET'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def get_job_configuration(request):
    job_id = request.query_params.get('job_id')
    if(job_id == ''):
        return Response({"job_topo":"","job_model":"","job_platform":""})
    job_topo,job_model,job_platform = job_info_database.get_job_configure_by_id(job_id)
    return Response({"job_topo":job_topo,"job_model":job_model,"job_platform":job_platform})

@api_view(['GET'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def get_job_progress(request):
    job_id = request.query_params.get('job_id')
    if(job_id == ''):
        return Response({"progress":0})
    return Response({'progress':job_info_database.get_job_progress_by_id(job_id)})

@api_view(['GET'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def get_test_table_in_job(request):
    job_id = request.query_params.get('job_id')
    if(job_id == ''):
        return Response({"testTable":{}})
    return Response({"testTable":job_info_database.get_tests_data_by_job_id(job_id)})

@api_view(['GET'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def get_job_table(request):
    return Response({"data":job_info_database.get_list()})

@api_view(['GET'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def get_job_execute_time(request):
    job_id = request.query_params.get('job_id')
    if(job_id == ''):
        return Response({"time":"0:00:00"})
    return Response({"time":job_info_database.get_job_execute_time_by_id(job_id)})

@api_view(['GET'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def get_image_table(request):
    return Response({"image_table":get_database.get_image_table()})

@api_view(['GET'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def get_running_job_list(request):
    return Response({"data":job_info_database.get_running_job_list()})

@api_view(['GET'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def get_jenkins_builds(request):
    info_list = []
    job_name = request.query_params.get('job_name')
    builds = jenkins.get_jenkins_job_info(job_name)
    for number in builds["builds"]:
        build_number = number["number"]
        result = jenkins.get_jenkins_build_result(job_name,build_number)
        info_list.append({"job_name":job_name,"build_number":build_number,"result":result})
    return Response({"builds":info_list})

@api_view(['GET'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def get_jenkins_jobs(request):
    job_list = jenkins.jobs()
    return Response({"jobs":job_list})

@api_view(['GET'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def build_jenkins_job(request):
    job_name = request.query_params.get('job_name')
    result = jenkins.submit_jenkins_build(job_name)
    return Response({"result":"Success"})

@api_view(['GET'])
@login_required(login_url='/accounts/login/')
@job_Submission_required
def get_build_result(request):
    job_name = request.query_params.get('job_name')
    build_number = request.query_params.get('build_number')
    result = jenkins.get_jenkins_build_result(job_name,build_number)
    return Response({"result":result})

@api_view(['POST'])
@login_required(login_url='/accounts/login/')
def create_deivce_list(request):
    data = dict(request.data)
    rack = data["rack"][0]
    rack = rack.split(" ")[0].lower() + rack.split(" ")[1].title() + rack.split(" ")[2]
    location = data["location"][0]
    model = data["model"][0]
    platform = data["platform"][0]
    console = data["console"][0]
    PDU = data["PDU"][0]
    IP = data["IP"][0]
    user = data["user"][0]
    power = data["power"][0]
    status = data["status"][0]
    device = Device_Data(rack,location,model,platform,console,IP,user,power,status,PDU)
    result = device_info.insert_device_list(device.to_json())
    return Response({"result":result})

@api_view(['GET'])
@login_required(login_url="/accounts/login/")
def get_device_list(request):
    data_list = device_info.get_all_device_list()
    return Response({"data":data_list})

@api_view(['GET'])
@login_required(login_url="/accounts/login/")
def get_device_list_by_rack(request):
    rack = request.query_params.get("rack")
    rack = rack.split(" ")[0].lower() + rack.split(" ")[1].title() + rack.split(" ")[2]
    data_list = device_info.get_device_list_by_rack(rack)
    return Response({"data":data_list})

@api_view(['POST'])
@login_required(login_url='/accounts/login/')
def change_device_list(request):
    data = dict(request.data)
    rack = data["rack"][0]
    rack = rack.split(" ")[0].lower() + rack.split(" ")[1].title() + rack.split(" ")[2]
    location = data["location"][0]
    changeType = data["type"][0]
    content = data["content"][0]
    data = {"rack":rack,"location":location,"type":changeType,"content":content}
    result = device_info.update_device_list(data)
    return Response({"result":result})