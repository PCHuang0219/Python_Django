from .database import *
from .jsonEncoder import *
from bson.objectid import ObjectId
from datetime import datetime,timezone,timedelta
class Job_Info_Database():
    def __init__(self):
        self._database = database.get_collection("job_info")
    
    def insert(self,job_info_data):
        data_id = self._database.insert_one(job_info_data.to_json()).inserted_id
        return data_id
    
    def get_list(self):
        data_list_cursor = self._database.find()
        data_list = []
        for data in data_list_cursor:
            data_list.append(JSONEncoder().encode(data))
        return data_list

    def get_job_status_by_id(self,job_id):
        job_data_cursor = self._database.find({"_id":ObjectId(job_id)})
        return job_data_cursor[0]["status"]

    def get_tests_data_by_job_id(self,job_id):
        job_data_cursor = self._database.find({"_id":ObjectId(job_id)})
        return job_data_cursor[0]["testcase_list"]

    def get_job_configure_by_id(self,job_id):
        job_data_cursor = self._database.find({"_id":ObjectId(job_id)})
        return job_data_cursor[0]["testcase_topology"],job_data_cursor[0]["model"],job_data_cursor[0]["platform"]

    def get_job_progress_by_id(self,job_id):
        job_data_cursor = self._database.find({"_id":ObjectId(job_id)})
        test_list = job_data_cursor[0]["testcase_list"]
        total_test_count = len(test_list)
        unfinish_count = 0
        for test in test_list:
            if(test["test_status"] != "Finished"):
                unfinish_count += 1
        return (total_test_count - unfinish_count)/(total_test_count) * 100

    def get_job_execute_time_by_id(self,job_id):
        job_data_cursor = self._database.find({"_id":ObjectId(job_id)})
        start_time_str = job_data_cursor[0]["start_time"]
        if(start_time_str == "NULL"):
            return "0:00:00"
        date_time_obj = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
        dt = datetime.utcnow()
        dt = dt.replace(tzinfo=timezone.utc)
        tzutc_8 = timezone(timedelta(hours=8))
        local_dt = dt.astimezone(tzutc_8)
        time_now_str = str(local_dt).split('.')[0]
        date_time_now_obj = datetime.strptime(time_now_str, '%Y-%m-%d %H:%M:%S')
        return str(date_time_now_obj - date_time_obj)
    
    def get_running_test_by_job_id(self,job_id):
        job_data_cursor = self._database.find({"_id":ObjectId(job_id)})
        running_test_id_str = job_data_cursor[0]["running_test_id"]
        if(running_test_id_str == "NULL"):
            return "not start running"
        running_test_id = int(running_test_id_str)
        if(running_test_id_str == "None"):
            return "no test running"
        test_name = job_data_cursor[0]["testcase_list"][running_test_id]["test_name"]
        test_case = job_data_cursor[0]["testcase_list"][running_test_id]["test_case"]
        test_topo = job_data_cursor[0]["testcase_list"][running_test_id]["test_topo"]
        return str(test_name) + "/" + str(test_case) + "/" + str(test_topo)

    def get_platform_by_job_id(self,job_id):
        data_list = []
        data_list_cursor = self._database.find({"_id":ObjectId(job_id)},{"_id":0,"platform":1})
        for data in data_list_cursor:
            data_list.append(data)
        return data_list

    def get_running_job_list(self):
        job_list = []
        job_list_cursor = self._database.find({"status":"Active"})
        for job_data in job_list_cursor:
            job_list.append(JSONEncoder().encode(job_data))
        return job_list

    def update_test_log_path_by_id(self,job_id,test_id,path):
        test_data = self._database.update({\
            "_id":ObjectId(job_id),\
            "testcase_list.test_id":int(test_id)\
        },{\
            '$set': {"testcase_list.$.test_log_path":path}\
        })
        if(test_data["updatedExisting"]):
            return "success"
        return "fail"