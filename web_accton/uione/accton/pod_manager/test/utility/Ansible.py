import os
from os import listdir
from os import path
import subprocess
import sys
from TestCase import *
from TestInfo import *
from Time import *
import time
from shutil import copyfile
import datetime
from fetchOutput import *
import requests 

class Ansible():
    def __init__(self,test,job_id):
        self.now_exec_testcase = test
        self.time = Time()
        self.job_id = job_id
        self.test_info = TestInfo()
        self.test = []
        self.dst_file_path = ""

    def set_start_status(self):
        self.now_exec_testcase.start_time = self.time.get_time_now() 
        self.now_exec_testcase.status = "running"
    
    def set_end_status(self,output):
        self.now_exec_testcase.end_time = self.time.get_time_now() 
        self.now_exec_testcase.status = "finish"
        self.now_exec_testcase.output = output
    
    def check_remove_old_file(self,path):
        if(os.path.isfile(path)):
            os.remove(path)
    
    def write_log_file(self,data_list):
        category = self.now_exec_testcase.category
        test_name = str(self.now_exec_testcase.test_name).split('/')[1]
        job_dir_path =  "./../../job_log/" + str(self.job_id) 
        if(not os.path.exists(job_dir_path)):
            os.mkdir(job_dir_path)
        category_dir_path = os.path.join(job_dir_path,category)
        if(not os.path.exists(category_dir_path)):
            os.mkdir(category_dir_path)
        self.now_exec_testcase.log_file_path = os.path.join(category_dir_path,test_name + ".log")
        with open(self.now_exec_testcase.log_file_path, 'w') as the_file:
            for line in data_list:
                the_file.write(line)

    def execute(self):
        test_name = self.now_exec_testcase.test_name.split('/')[0]
        test_case = self.now_exec_testcase.test_name.split('/')[1]
        test_topology = self.now_exec_testcase.test_name.split('/')[2]
        r = requests.post('http://192.168.30.22:3000/run', data =  {'test_name': test_name,'test_case':test_case,"test_topology":test_topology}, verify = False)
        while(True):  
            r = requests.get('http://192.168.30.22:3000/status', data =  {}, verify = False)
            response_data = r.json()
            r = requests.get('http://192.168.30.22:3000/log', data =  {}, verify = False)
            log_data = r.json()['log']
            self.write_log_file(log_data)
            time.sleep(0.5)
            if(response_data['status'] == "finish"):
                break

    def get_result(self):
        self.now_exec_testcase.result = check(self.now_exec_testcase.log_file_path)
        return  self.now_exec_testcase.result




