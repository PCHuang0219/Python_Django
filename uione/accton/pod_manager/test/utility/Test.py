import os
from os import listdir
from os import path
import subprocess
import sys
import time
from shutil import copyfile
import datetime

MAIN_PATH = "./test_case_script/Simba/Topology_1/1QVLAN"
DIR_PATH = "/Topology_1/1QVLAN"

import_command = 'source ./ui_script/UI_utility.tcl\n'
command = "UI_PerformTestingScript " + DIR_PATH +" " + "1QVLAN-0010.tcl" + " v19.01.R1.0\n"

class Test():
    def __init__(self,test,job_id):
        self.import_command = 'source ./ui_script/UI_utility.tcl\n'
        self.test_script_path = "./../../ui_script/test_script.tcl"
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

    def rewrite_file(self):
        category = self.now_exec_testcase.category
        topo_type = self.now_exec_testcase.topo_type
        test_name = self.now_exec_testcase.test_name
        sign = '"'
        dir_path = str(topo_type) + "/" + str(category)

        self.check_remove_old_file(self.test_script_path)
        command = "UI_PerformTestingScript " + sign + dir_path + sign +" " + sign +str(test_name) + ".tcl" + sign + " v19.01.R1.0\n"
        with open(self.test_script_path,'a') as file:
            file.write(self.import_command)
            file.write(command)
    
    def move_test_log(self):
        category = self.now_exec_testcase.category
        test_name = self.now_exec_testcase.test_name
        job_dir_path =  "./../../job_log/" + str(self.job_id) 
        print("start_write_time:" + str(self.job_id))
        if(not os.path.exists(job_dir_path)):
            os.mkdir(job_dir_path)
        
        category_dir_path = os.path.join(job_dir_path,category)
        if(not os.path.exists(category_dir_path)):
            os.mkdir(category_dir_path)

        origin_path = "./../../log/" + category + "/" + test_name + ".log"        
        self.now_exec_testcase.log_file_path = os.path.join(category_dir_path,test_name + ".log")
        copyfile(origin_path,self.now_exec_testcase.log_file_path)

    def execute(self,command):
        process = subprocess.Popen(command, cwd = "./../../",shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = process.communicate()[0]
        exitCode = process.returncode
        process.wait()
        return output

    def get_result(self):
        self.now_exec_testcase.result = check(self.now_exec_testcase.log_file_path)
        return  self.now_exec_testcase.result




