from .database import *
from .jsonEncoder import *
from bson.objectid import ObjectId
from datetime import datetime,timezone,timedelta
import calendar
from bson import json_util
import json

class Project_Info_Database():
    def __init__(self):
        self.issue_database = project_database.get_collection("issue")
        self.issue_content_database = project_database.get_collection("issue_content")
        self.issue_description_database = project_database.get_collection("issue_description")
        self.issue_discussion_database = project_database.get_collection("issue_discussion")
        self.main_project_database = project_database.get_collection("project")
    
    def insert_issue(self,issue_info_data):
        result = self.issue_database.insert_one(issue_info_data).acknowledged
        return result
    
    def update_issue(self,TRR_ID,module):
        result = self.issue_database.update({"TRR_ID":TRR_ID},{'$set':{"module":module}})
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
    
    def get_bug_information(self):
        data_list = []
        data_list_cursor = self.issue_database.find({},{"_id":0})
        for data in data_list_cursor:
            data_list.append(JSONEncoder().encode(data))
        return data_list
    
    def update_bug_status(self,TRR_ID,status):
        result = self.issue_database.update({"TRR_ID":TRR_ID},{'$set':{"status":status}})
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
    
    def create_bug_detail(self,issue_bug_info_data):
        project = self.issue_database.find_one({"project":issue_bug_info_data["project"]},{"_id":1})
        issue_bug_info_data["project"]=project["_id"]
        result = self.issue_description_database.insert_one(issue_bug_info_data).acknowledged
        return result

    def create_bug_issue(self,issue_bug_info_data):
        project = self.issue_database.find_one({"project":issue_bug_info_data["project"]},{"_id":1})
        issue_bug_info_data["project"]=project["_id"]
        result = self.issue_discussion_database.insert_one(issue_bug_info_data).acknowledged
        return result
    
    def get_bug_issue(self,TRR_ID):
        data_list = []
        data_list_cursor = self.issue_discussion_database.find({"TRR_ID":TRR_ID},{"_id":0,"submit_time":1,"issue":1,"user":1})
        for data in data_list_cursor:
            data_list.append(data)
        return data_list
    
    def get_bug_description(self,TRR_ID):
        data_list = []
        data_list_cursor = self.issue_description_database.find({"TRR_ID":TRR_ID},{"_id":0,"submit_time":1,"description":1,"user":1})
        for data in data_list_cursor:
            data_list.append(data)
        return data_list
    
    def insert_issue_detail(self,issue_detail_data):
        PL = self.main_project_database.find_one({"project_name":issue_detail_data["project"]},{"PL":1,"_id":0})
        PM = self.main_project_database.find_one({"project_name":issue_detail_data["project"]},{"PM":1,"_id":0})
        issue_detail_data["PL"] = PL
        issue_detail_data["PM"] = PM
        result = self.issue_content_database.insert_one(issue_detail_data).acknowledged
        return result
    
    def update_issue_detail(self,TRR_ID,key,value):
        result = self.issue_content_database.update({"TRR_ID":TRR_ID},{'$set':{key:value}})
        return str(result["updatedExisting"])

    def get_bug_detail(self,project,TRR_ID):
        data_list = []
        TRR = self.issue_database.find_one({"TRR_ID":TRR_ID},{"_id":0})
        data_list.append(TRR)
        TRR_detail = self.issue_content_database.find({"TRR_ID":TRR_ID},{"_id":0})
        for data in TRR_detail:
            data_list.append(data)
        return data_list
    
    def update_bug_detail_status(self,bug_id,status):
        result = self.issue_content_database.update({"_id":ObjectId(bug_id)},{'$set':{"status":status}})
        return str(result["updatedExisting"])