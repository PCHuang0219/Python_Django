from .database import *
from .jsonEncoder import *
from bson.objectid import ObjectId
from datetime import datetime,timezone,timedelta
import calendar
from bson import json_util
import json

class Lab_Info_Database():
    def __init__(self):
        self.ixia_database = lab_database.get_collection("IXIA_Info")
    
    def insert_ixia_schedule(self,ixia_info_data):
        result = self.ixia_database.insert_one(ixia_info_data).acknowledged
        return result

    def get_ixia_schedule(self):
        week_range = self.get_two_week_datetime()
        first_day = datetime.strptime(week_range[0][0], '%Y-%m-%d')
        last_day = datetime.strptime(week_range[1][6] + ' 23:59:59', "%Y-%m-%d %H:%M:%S")
        condition_1 = {'$and':[{"start_time":{'$gte':first_day}},{"end_time":{'$lte':last_day}}]}
        condition_2 = {'$and':[{"end_time":{'$gte':first_day}},{"end_time":{'$lte':last_day}}]}
        condition_3 = {'$and':[{"start_time":{'$lte':last_day}},{"start_time":{'$gte':first_day}}]}
        data_list_cursor = self.ixia_database.find({'$or':[condition_1,condition_2,condition_3]},{'_id':0})
        data_list = []
        for data in data_list_cursor:
            data = json.dumps(data, indent=4, sort_keys=True, default=str)
            data_list.append(data)
        return data_list

    def get_two_week_datetime(self):
        now_weekday = datetime.today().weekday()
        now_year = datetime.now().year
        now_month = datetime.now().month
        now_date =  datetime.now().day
        calendar.setfirstweekday(6)
        month_calendar = calendar.monthcalendar(now_year,now_month)
        w = -1
        for week in month_calendar:
            w += 1
            for i in range(0,7):
                if week[i] == now_date:
                    now_week = week
                    next_week = month_calendar[w+1]
        now_week = self.get_week_date(now_week,now_year,now_month)
        next_week = self.get_week_date(next_week,now_year,now_month)
        return [now_week,next_week]

    def get_week_date(self,now_week,now_year,now_month):
        calendar.setfirstweekday(6)
        for i in range(0,7):
            if now_week[i] == 0 :
                if now_month == 12 :
                    next_month_calendar = calendar.monthcalendar(now_year+1,1)[0]
                    now_week[i] = str(now_year+1) + "-" + str("%02d" % 1) + "-" + str("%02d" % next_month_calendar[i])
                else:
                    next_month_calendar = calendar.monthcalendar(now_year,now_month+1)[0]
                    now_week[i] = str(now_year) + "-" + str("%02d" % (now_month+1)) + "-" + str("%02d" % next_month_calendar[i])
            else:
                now_week[i] = str(now_year) + "-" + str("%02d" % now_month) + "-" + str("%02d" % now_week[i])
        return now_week

    def check_ixia_status(self,ixia_info):
        card = ixia_info["card"]
        port = ixia_info["port"]
        owner = ixia_info["owner"]
        start_time = ixia_info["start_time"]
        end_time = ixia_info["end_time"]
        condition_1 = {'$and':[{"start_time":{'$gte':start_time}},{"end_time":{'$gte':end_time}},{"start_time":{'$lte':end_time}} ]}
        condition_2 = {'$and':[{"start_time":{'$lte':start_time}},{"end_time":{'$gte':end_time}} ]}
        condition_3 = {'$and':[{"start_time":{'$lte':start_time}},{"end_time":{'$lte':end_time}},{"end_time":{'$gte':start_time}} ]}
        condition_4 = {'$and':[{"start_time":{'$gte':start_time}},{"end_time":{'$lte':end_time}} ]}
        condition = {'$or':[condition_1,condition_2,condition_3,condition_4]}
        status = self.ixia_database.find({'$and': [ {"card":card},{"port":port},condition]},{'_id':0}).count()
        if status > 0 :
            return "Failed"
        else:
            return "Success"


    def update_IXIA_Info(self,lab_info_data):
        data = lab_info_data.to_json()
        update_data = self.ixia_database.update({"location":data["location"],"model":data["model"],"port_number":data["port_number"]},{"$set":{ \
                "status":data["status"], \
                "ToRack":data["ToRack"], \
                "ToDevice":data["ToDevice"], \
                "start_time":data["start_time"], \
                "end_time":data["end_time"], \
                "owner":data["owner"], \
                "description":data["description"]}})
        if(update_data["updatedExisting"]):
            return "success"
        return "fail"

    def update_ixia_config(self):
        start_time_org = datetime.now().strftime("%Y-%m-%d")
        start_time = datetime.now().strptime(start_time_org,"%Y-%m-%d")
        end_time = datetime.now().strftime("%Y-%m-%d 23:59:59")
        end_time = datetime.now().strptime(end_time,"%Y-%m-%d %H:%M:%S")
        data_list_cursor =self.ixia_database.find({'$and':[{"start_time":{'$lte':start_time}},{"end_time":{'$gte':end_time}}]},{'_id':0})
        data_list = []
        for data in data_list_cursor:
            data = json.dumps(data, indent=4, sort_keys=True, default=str)
            data_list.append(data)
        data_list.append(start_time_org)
        return data_list

    def update_IXIA_view(self,location,model,port_number):
        data_list = []
        data_list_cursor = self.ixia_database.find({'$or':[{"location":location},{"model":model},{"port_number":port_number}]},{'_id':0})
        for data in data_list_cursor:
            data_list.append(JSONEncoder().encode(data))
        return data_list

class Device_Info_Data():
    def __init__(self):
        self.device_database = lab_database.get_collection("Device_List")
    
    def insert_device_list(self,device_data):
        result = self.device_database.insert_one(device_data).acknowledged
        return result
    
    def update_device_list(self,device_data):
        result = self.device_database.update({"rack":device_data["rack"],"location":device_data["location"]},
                                {'$set':{device_data["type"]:device_data["content"]}})
        return str(result["updatedExisting"])
    
    def get_all_device_list(self):
        data_list_cursor = self.device_database.find({},{"_id":0})
        data_list = self.sort_by_location(data_list_cursor)
        return data_list
    
    def get_device_list_by_rack(self,rack):
        data_list_cursor = self.device_database.find({"rack":rack},{"_id":0,"location":1,"model":1})
        data_list = self.sort_by_location(data_list_cursor)
        return data_list
    
    def sort_by_location(self,data_list_cursor):
        data_list = []
        for data in data_list_cursor:
            data_list.append(data)
        return data_list