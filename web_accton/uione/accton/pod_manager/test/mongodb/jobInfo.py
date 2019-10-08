from datetime import datetime,timezone,timedelta
from .testcase import Testcase
class Job_Information:
    def __init__(self,job_name,job_describe,platform,model,user_id,testcase_topology,image_version,testcase_list):
        self.job_name = job_name
        self.job_describe = job_describe
        self.platform = platform
        self.model = model
        self.submit_time = self.get_time_now()
        self.user_id = user_id
        self.testcase_topology = testcase_topology
        self.image_version = image_version
        self.testcase_list = testcase_list
        self.status = "not start"
        self.start_time = "NULL"
        self.end_time = "NULL"
        self.result = "NULL"
        self.running_test_id = "NULL"
        self.testcase_list_json = self.get_testcase_list()
        
    def get_testcase_list(self):
        testcase_list_json = []
        index = 0
        for testcase_name in self.testcase_list:
            testcase = Testcase(testcase_name,self.platform,index)
            testcase_list_json.append(testcase.to_json())
            index += 1
        return testcase_list_json

    def get_time_now(self):
        dt = datetime.utcnow()
        dt = dt.replace(tzinfo=timezone.utc)
        tzutc_8 = timezone(timedelta(hours=8))
        local_dt = dt.astimezone(tzutc_8)
        return str(local_dt).split('.')[0]

    def to_json(self):
        return {'job_name':self.job_name,\
            'job_describe':self.job_describe,\
            'platform':self.platform,\
            'model':self.model,\
            'submit_time':self.submit_time,\
            'user_id':self.user_id,\
            'testcase_topology':self.testcase_topology,\
            'testcase_list':self.testcase_list_json,\
            'status':self.status,\
            'start_time':self.start_time,\
            'end_time':self.end_time,\
            'result':self.result,\
            'running_test_id':self.running_test_id, \
            'image_version':self.image_version}

    
