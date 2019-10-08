import os
from os import listdir
from os import path
import subprocess
import sys
from TestCase import *
from TestInfo import *
import time
from shutil import copyfile
import datetime
from datetime import datetime,timezone,timedelta


MAIN_PATH = "./test_case_script/Simba/Topology_1/1QVLAN"
DIR_PATH = "/Topology_1/1QVLAN"

import_command = 'source ./ui_script/UI_utility.tcl\n'
command = "UI_PerformTestingScript " + DIR_PATH +" " + "1QVLAN-0010.tcl" + " v19.01.R1.0\n"

class Test():
    def __init__(self):
        self.test_case_list = []
        self.finish_case_list = []
        self.import_command = 'source ./../../ui_script/UI_utility.tcl\n'
        self.test_script_path = "./../../ui_script/test_script.tcl"
        self.now_exec_testcase = ""
        self.job_start_time = ""
        self.test_info = TestInfo()

    def get_time_now(self):
        dt = datetime.utcnow()
        dt = dt.replace(tzinfo=timezone.utc)
        tzutc_8 = timezone(timedelta(hours=8))
        local_dt = dt.astimezone(tzutc_8)
        return str(local_dt).split('.')[0]

    def add_test_case(self,testList):
        self.job_start_time = self.get_time_now()
        for test_name in testList:
            data_list = self.test_info.get_by_testId(test_name)
            topo_type = data_list[0]['topology']
            category = data_list[0]['category']
            self.test_case_list.append(TestCaseData(test_name,topo_type,category))
    
    def get_oldest_testCase(self):
        self.now_exec_testcase = self.test_case_list.pop(0)
        self.now_exec_testcase.start_time = time.time()
        self.now_exec_testcase.status = "running"
        return self.now_exec_testcase

    def get_test_list_size(self):
        return len(self.test_case_list)

    def check_remove_old_file(self,path):
        if(os.path.isfile(path)):
            os.remove(path)

    def rewrite_file(self,test_case):
        sign = '"'
        dir_path = str(test_case.topo_type) + "/" + str(test_case.category)
        self.check_remove_old_file(self.test_script_path)
        command = "UI_PerformTestingScript " + sign + dir_path + sign +" " + sign +str(self.now_exec_testcase.test_name) + ".tcl" + sign + " v19.01.R1.0\n"
        with open(self.test_script_path,'a') as file:
            file.write(self.import_command)
            file.write(command)
    
    def move_test_log(self,test_case):
        category = test_case.category
        test_name = test_case.test_name
        job_dir_path =  "./job_log/" + str(self.job_start_time) 
        if(not os.path.exists(job_dir_path)):
            os.mkdir(job_dir_path)
        
        category_dir_path = os.path.join(job_dir_path,category)
        if(not os.path.exists(category_dir_path)):
            os.mkdir(category_dir_path)

        origin_path = "./log/" + category + "/" + test_name + ".log"        
        dst_path = os.path.join(category_dir_path,test_name + ".log")
        copyfile(origin_path,dst_path)

    def execute(self,command):
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = process.communicate()[0]
        exitCode = process.returncode
        process.wait()
        self.now_exec_testcase.end_time = time.time()
        self.now_exec_testcase.status = "finish"
        self.now_exec_testcase.output = output
        print(self.now_exec_testcase.test_name)
        print("spend time :" + str(self.now_exec_testcase.calculate_spend_time()))
        self.finish_case_list.append(self.now_exec_testcase)
        self.move_test_log(self.now_exec_testcase)
        return output



