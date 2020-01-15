from .database import *
from .jsonEncoder import *
from bson.objectid import ObjectId
from datetime import datetime,timezone,timedelta
import calendar
from bson import json_util
import json

def get_time_now():
    dt = datetime.utcnow()
    dt = dt.replace(tzinfo=timezone.utc)
    tzutc_8 = timezone(timedelta(hours=8))
    local_dt = dt.astimezone(tzutc_8)
    return str(local_dt).split('.')[0]

class Project_Info_Database():
    def __init__(self):
        self.issue_database = project_database.get_collection("issue")
        self.issue_description_database = project_database.get_collection("issue_description")
        self.issue_discussion_database = project_database.get_collection("issue_discussion")
        self.main_project_database = project_database.get_collection("project")
    
    def insert_TRR(self,issue_info_data):
        PLPM_data = self.main_project_database.find({"project_name":issue_info_data["project"]},{"PL":1,"PM":1,"_id":0})
        issue_info_data["PL"] = PLPM_data[0]["PL"]
        issue_info_data["PM"] = PLPM_data[0]["PM"]
        result = self.issue_database.insert_one(issue_info_data).acknowledged
        return result
    
    def update_TRR(self,TRR_ID,key,value):
        if key == "Module":
            key = "module"
        result = self.issue_database.update({"TRR_ID":TRR_ID},{'$set':{key:value}})
        return str(result["updatedExisting"])
    
    def get_project_list(self):
        data_list = []
        buff_list = []
        data_list_cursor = self.main_project_database.find({},{"project_name":1,"_id":0})
        for data in data_list_cursor:
            data = JSONEncoder().encode(data)
            if data not in buff_list:
                buff_list.append(data)
                data_list.append(data)
        return data_list
    
    def get_TRR_list(self):
        data_list = []
        data_list_cursor = self.issue_database.find({},{"_id":0}).sort([("submit_time",1)])
        for data in data_list_cursor:
            data_list.append(JSONEncoder().encode(data))
        return data_list
    
    def update_TRR_status(self,TRR_ID,status,content,MEDF):
        if status == "Verified" :
            update_content = {'$set':{"status":status,"TLConfirm":content}}
        elif status == "Assigned":
            update_content = {'$set':{"status":status,"MEDF":MEDF}}
        else:
            update_content = {'$set':{"status":status}}
        result = self.issue_database.update({"TRR_ID":TRR_ID},update_content)
        return str(result["updatedExisting"])
    
    def insert_main_project(self,project_info_data):
        result = self.main_project_database.insert_one(project_info_data).acknowledged
        return result
    
    def get_main_project_data(self,customer):
        data_list = []
        data_list_cursor = self.main_project_database.find({"customer":customer},{"_id":0})
        for data in data_list_cursor:
            data_list.append(JSONEncoder().encode(data))
        return data_list
    
    def create_TRR_description(self,issue_bug_info_data):
        project = self.issue_database.find_one({"project":issue_bug_info_data["project"]},{"_id":1})
        issue_bug_info_data["project"]=project["_id"]
        result = self.issue_description_database.insert_one(issue_bug_info_data).acknowledged
        return result

    def create_TRR_discussion(self,issue_bug_info_data):
        project = self.issue_database.find_one({"project":issue_bug_info_data["project"]},{"_id":1})
        issue_bug_info_data["project"]=project["_id"]
        result = self.issue_discussion_database.insert_one(issue_bug_info_data).acknowledged
        return result
    
    def get_TRR_discussion(self,TRR_ID):
        data_list = []
        data_list_cursor = self.issue_discussion_database.find({"TRR_ID":TRR_ID},{"_id":0,"submit_time":1,"issue":1,"user":1,"mail":1})
        for data in data_list_cursor:
            data_list.append(data)
        return data_list
    
    def get_TRR_description(self,TRR_ID):
        data_list = []
        data_list_cursor = self.issue_description_database.find({"TRR_ID":TRR_ID},{"_id":0,"submit_time":1,"description":1,"user":1})
        for data in data_list_cursor:
            data_list.append(data)
        return data_list

    def get_TRR_detail(self,project,TRR_ID):
        TRR = self.issue_database.find_one({"TRR_ID":TRR_ID},{"_id":0})
        return TRR

    def get_views_by_condition(self,condition):
        data_list = []
        condition = json.loads(condition)
        data_list_cursor = self.issue_database.find(condition,{"_id":0}).sort([("submit_time",1)])
        for data in data_list_cursor:
            data_list.append(JSONEncoder().encode(data))
        return data_list

    def get_selection_by_condition(self,condition):
        data_list = []
        buff_list = []
        data_list_cursor = self.issue_database.find({},{"_id":0,condition:1})
        for data in data_list_cursor:
            data = data[condition]
            if data not in buff_list:
                buff_list.append(data)
                data_list.append(data)
        return data_list
    
    def update_history_by_TRR_ID(self,TRR_ID,content):
        history = self.issue_database.find({"TRR_ID":TRR_ID},{"history":1,"_id":0})
        print(history["history"])
        # self.issue_database.update({"TRR_ID":TRR_ID},{"$set":{"history":}})

class Test_Case_Info_Database():
    def __init__(self):
        self.TD_database = testcase_database.get_collection("TD")
        self.TC_database = testcase_database.get_collection("TC")
        
    def insert_TD(self,TD_data):
        result = self.TD_database.insert_one(TD_data).acknowledged
        return result
    
    def insert_TC(self,TC_data):
        result = self.TC_database.insert_one(TC_data).acknowledged
        self.update_TC_count(TC_data["TD_ID"])
        return result

    def update_TC_count(self,TD_Number):
        TC_count = self.TC_database.find({"TD_ID":TD_Number}).count()
        self.TD_database.update({"TD_ID":TD_Number},{"$set":{"TC_count":TC_count}})
    
    def get_all_TD_list(self):
        data_list = []
        data_list_cursor = self.TD_database.find({},{"TD_ID":1,"_id":0})
        for data in data_list_cursor:
            data = JSONEncoder().encode(data)
            data_list.append(data)
        return data_list
    
    def get_all_TC_list_by_TD(self,TD_ID):
        data_list = []
        data_list_cursor = self.TC_database.find({"TD_ID":TD_ID},{"TC_ID":1,"_id":0})
        for data in data_list_cursor:
            data = JSONEncoder().encode(data)
            data_list.append(data)
        return data_list

class EPR_Info_Database():
    def __init__(self):
        self.EPR_database = project_database.get_collection("EPR")
    
    def get_EPR_ID(self,project):
        count = self.EPR_database.find({"project":project}).count()
        EPR_ID = "EPR-" + project + "-" + str(int(count)+1).zfill(3)
        return EPR_ID
    
    def insert_EPR_attachment(self,EPR_ID,file_list):
        submit_time = get_time_now()
        content = {"attachments":file_list,"EPR_ID":EPR_ID,"submit_time":submit_time,"status":"Submitted"}
        result = self.EPR_database.insert_one(content).acknowledged
        return result
    
    def update_EPR_content_by_ID(self,EPR_ID,content):
        result = self.EPR_database.update({"EPR_ID":EPR_ID},{'$set':content})
        return str(result["updatedExisting"])
    
    def get_EPR_list(self,condition):
        data_list = []
        data_list_cursor = self.EPR_database.find(condition,{"_id":0}).sort([("submit_time",1)])
        for data in data_list_cursor:
            data_list.append(JSONEncoder().encode(data))
        return data_list

class Tasks_Info_Database():
    def __init__(self):
        self.tasks_database = project_database.get_collection("tasks")
    
    def insert_tasks(self,content_list):
        submit_time = get_time_now()
        for content in content_list:
            content["submit_time"] = submit_time
            self.tasks_database.insert_one(content)
        
    def get_tasks_list(self,condition):
        data_list = []
        data_list_cursor = self.tasks_database.find(condition,{"_id":0}).sort([("submit_time",1)])
        for data in data_list_cursor:
            data_list.append(JSONEncoder().encode(data))
        return data_list
    
    def get_task_detail_by_task_ID(self,condition):
        data_list = []
        data_list_cursor = self.tasks_database.find(condition,{"_id":0})
        for data in data_list_cursor:
            data_list.append(JSONEncoder().encode(data))
        return data_list

project_info_db = Project_Info_Database()
testcase_info_db = Test_Case_Info_Database()
EPR_info_db = EPR_Info_Database()
tasks_info_db = Tasks_Info_Database()