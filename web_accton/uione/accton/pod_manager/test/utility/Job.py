import uuid
import csv
import numpy as np
import pandas as pd


class Job():
    def __init__(self,Job_name,Job_description,Test_list,Job_platform,Job_model,Job_topology):
        self.job_name = Job_name
        self.job_description = Job_description
        self.job_id = str(uuid.uuid4())
        self.start_time = ""
        self.end_time = "###"
        self.status = ""
        self.output_dir_path = ""
        self.test_info = TestInfo()
        self.time = Time()
        self.result = ""
        self.platform = Job_platform
        self.model = Job_model
        self.topology = Job_topology
        self.test_list = self.add_test(Test_list)
        self.csv_dir_path = "./../../output_csv/" + self.job_id  
        self.now_execute_test = ""


    def get_status(self):
        data_list = []
        for test in self.test_list:
            data_list.append({"test_name":test.test_name,"test_status":test.status,"start_time":test.start_time,"end_time":test.end_time,"result":test.result})
        return data_list

    def add_test(self,test_list):
        test_case_list = []
        for test_name in test_list:
            data_list = self.test_info.get_by_testId(test_name,self.platform)
            print(data_list)
            topo_type = data_list[0]['topology']
            category = data_list[0]['category']
            test_case_list.append(TestCaseData(test_name,topo_type,category))
        return test_case_list

    def set_start_status(self):
        self.start_time = self.time.get_time_now()
        self.status = "running"
        return self.start_time

    def set_end_status(self):
        self.end_time = self.time.get_time_now()
        self.status = "finish"
        self.result = self.set_result()

    def run_test_case(self):
        for single_test_data in self.test_list:
            self.now_execute_test = single_test_data
            print(single_test_data.test_name)
            if(self.platform == "SONiC"):
                test = Ansible(single_test_data,self.job_id)
                test.set_start_status()
                output = test.execute()
                print(output)
                test.set_end_status(output)
                #test.move_test_log()
                #test.get_result()
            else:
                test = Test(single_test_data,self.job_id)
                test.set_start_status()
                test.rewrite_file()
                output = test.execute("tclsh ./ui_script/test_script.tcl")
                print(output)
                test.set_end_status(output)
                test.move_test_log()
                test.get_result()

    def running(self,test):
        test.set_start_status()
        test.rewrite_file()
        output = test.execute("tclsh ./ui_script/test_script.tcl")
        print(output)
        test.set_end_status(output)
        test.move_test_log()
        test.get_result()

    def write_to_file(self):
        if(not os.path.exists(self.csv_dir_path)):
            os.mkdir(self.csv_dir_path)

        job_info_csv_path = os.path.join(self.csv_dir_path,"job.csv")  
        with open(job_info_csv_path, "a") as f:
            writer = csv.writer(f)
            writer.writerow(['job_name','job_description','job_id','status','result','start_time','end_time'])
            writer.writerow([self.job_name,self.job_description,self.job_id,self.status,self.result,self.start_time,self.end_time])

        test_info_csv_path = os.path.join(self.csv_dir_path,"test.csv")  
        with open(test_info_csv_path, "a") as f:
            writer = csv.writer(f)
            writer.writerow(["test_id","status","result","start_time","end_time","log_path"])
            for test_data in self.test_list:
                writer.writerow([test_data.test_name,test_data.status,test_data.result,test_data.start_time,test_data.end_time,test_data.log_file_path])

    def get_now_test_log(self):
        print(self.platform)
        #if(self.platform == "SONiC"):
        r = requests.get('http://192.168.30.22:3000/log', data =  {}, verify = False)
        log_data = r.json()['log']
        print(log_data)
        return {"job_status":{"log":log_data},"model":self.model,"topology":self.topology,"platform":self.platform,"test_name":self.now_execute_test.test_name}             
        '''
        else:
            log_path = "../../log/" + str(self.now_execute_test.category) + "/" + str(self.now_execute_test.test_name) + ".log"
            with open(log_path) as f:
                lines = f.readlines()
            return {"job_status":{"log":lines[-80:]},"model":self.model,"topology":self.topology,"platform":self.platform,"test_name":self.now_execute_test.test_name}
        '''
    def set_result(self):
        pass_num = 0
        fail_num = 0
        strange_num = 0
        error_num = 0
        result = ""
        for test in self.test_list:
            if(test.result == "pass"):
                pass_num+=1
            elif(test.result == "fail"):
                fail_num+=1
            elif(test.result == "strange"):
                strange_num+=1
            elif(test.result == "error"):
                error_num+=1
        if(pass_num > 0):
            result += "pass:" + str(pass_num)
        if(fail_num > 0):
            result += "fail:" + str(fail_num)
        if(strange_num > 0):
            result += "strange:" + str(strange_num)
        if(error_num > 0):
            result += "error:" + str(error_num)
        return result




    