import csv
import os
from os import listdir
from os import path
import json
from tempfile import NamedTemporaryFile
from rest_framework.response import Response
from rest_framework import status
from ..models import *
import shutil

class SaveDatabase():
    def __init__(self):
        pass
    
    def add_new_job(self,job_id,data_list,test_list,user):
        job_name = data_list['job_name'][0]
        job_description = data_list['job_description'][0]
        job_model = data_list['model'][0]
        job_topo = data_list['topology'][0]
        job_platform = data_list['platform'][0]

        job_id = self.save_job_information(user,job_name,job_description,job_model,job_topo,job_platform)

        for test_data in test_list:
                test_name = test_data.split('/')[0]
                test_case = test_data.split('/')[1]
                test_topology = test_data.split('/')[2]
                self.save_job_test_list(job_id,test_case,test_name,test_topology)

        '''
        if(not os.path.exists(test_csv_dir_path)):
            os.mkdir(test_csv_dir_path)
        if(not os.path.exists(self.job_csv_path)):
            with open(self.job_csv_path, "a") as f:
                writer = csv.writer(f)
                writer.writerow(['job_name','job_description','job_id','status','result','start_time','end_time','model','topology','platform'])

        with open(self.job_csv_path, "a") as f:
            writer = csv.writer(f)
            writer.writerow([job_name,job_description,job_id,"not start","not start","not start","not start",job_model,job_topo,job_platform])

        test_info_csv_path = os.path.join(test_csv_dir_path,"test.csv")  
        with open(test_info_csv_path, "w") as f:
            writer = csv.writer(f)
            writer.writerow(["test_name","test_case","test_topology","status","result","start_time","end_time","log_path"])
            
        '''

    def save_job_information(self,user,job_name,job_description,job_model,job_topo,job_platform,status="Not start",result="Not start",start_time="Not_start",end_time="Not start"):
        try:
            job_information = Job_information(user=user,Job_name=job_name,Job_description=job_description,model=job_model,topo=job_topo, \
                                                platform=job_platform,status=status,result=result,start_time=start_time,end_time=end_time)
            job_information.save()
            return job_information.id
        except Exception as e:
            print(e)
            return Response({"error":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def save_job_test_list(self,job_id,case,name,topology="null"):
        try:
            job = Job_information.objects.get(id=job_id)
            job_test_list = Job_test_list(job=job,testcase=case,testcase_name=name,testcase_topology=topology)
            job_test_list.save()
        except Exception as e :
            print(e)
            return Response({"error":e},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def save_log(self,job_id,test_name,test_case,test_topo,log,log_type="origin"):
        job_dir_log_path = os.path.join(self.output_log_dir_path,job_id)
        self.make_dir(job_dir_log_path)
        file_name = test_name + "-" + test_case+ "-" + test_topo
        if(log_type == "complete"):
            complete_dir_path = os.path.join(job_dir_log_path,"complete")
            self.make_dir(complete_dir_path)
            test_log_path = os.path.join(complete_dir_path,file_name)
        else:
            simple_dir_path = os.path.join(job_dir_log_path,"simple")
            self.make_dir(simple_dir_path)
            test_log_path = os.path.join(simple_dir_path,file_name)
        with open(test_log_path, "w") as f:
            for line in log:
                f.write(line)