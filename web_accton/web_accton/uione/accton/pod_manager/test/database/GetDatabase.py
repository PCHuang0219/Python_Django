from rest_framework.response import Response
from rest_framework import status
from ..models import *

import csv
import os
from os import listdir
from os import path
import json
from tempfile import NamedTemporaryFile
import shutil
from .Database import Database

class GetDatabase(Database):
    def __init__(self):
        Database.__init__(self)

    def get_test_log(self,job_id,test_string):
        job_dir_path = os.path.join(self.output_log_dir_path,job_id)
        complete_log_dir_path = os.path.join(job_dir_path,"complete")
        test_log_path = os.path.join(complete_log_dir_path,test_string)
        with open(test_log_path) as f:
            content = f.readlines()
        return content

    def get_now_test_table(self,job_id):
        if(job_id == None):
            return []
        csv_path = self.generate_csv_path(job_id,"test")
        data_list = []
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append({"test_name":row['test_name']+"-"+row['test_case']+"-"+row['test_topology'], \
                    "test_status":row['status'], \
                    "test_result":row['result'], \
                    "start_time":row['start_time'], \
                    "end_time":row['end_time'], \
                    })
        return sorted(data_list, key = lambda i: i['start_time']) 
    
    def get_now_job_table(self):
        data_list = []
        with open(self.job_csv_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append({"job_id":row['job_id'], \
                    "job_name":row['job_name'], \
                    "job_status":row['status'], \
                    "job_description":row['job_description'], \
                    "job_result":row['result'], \
                    "start_time":row['start_time'], \
                    "end_time":row['end_time'] \
                    })
        return sorted(data_list, key = lambda i: i['start_time'],reverse=True) 
    
    def get_now_running_job_name(self):
        data_list = []
        with open(self.job_csv_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if(row['status'] == "running"):
                    data_list.append({"job_id":row['job_id'], \
                        "job_name":row['job_name'], \
                        "job_status":row['status'], \
                        "job_description":row['job_description'], \
                        "job_result":row['result'], \
                        "start_time":row['start_time'], \
                        "end_time":row['end_time'] \
                        })
        return sorted(data_list, key = lambda i: i['start_time'],reverse=True) 

    def get_image_table(self):
        data_list = []
        with open(self.image_csv_path, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                data_list.append(row)
        index = 0
        return_list = []
        while(index < len(data_list)):
            server_name = data_list[index][0]
            server_root_path = data_list[index][1]
            server_image_number = int(data_list[index][2])
            index += 1
            for i in range(0,server_image_number):
                return_list.append({
                    "server_name":server_name, \
                    "server_root_path":server_root_path, \
                    "chip_company_name":data_list[index+i][0], \
                    "build_type":data_list[index+i][1], \
                    "build_number":data_list[index+i][2]
                })
            index += server_image_number
        return return_list

class getDatabase():
    def __init__(self):
        pass
    
    def getNotFinishJob():
        job_list = Job_information.objects.filter(result='aaa')
        print(job_list)
        return Response({"not_executed":job_list},status=status.HTTP_200_OK)



