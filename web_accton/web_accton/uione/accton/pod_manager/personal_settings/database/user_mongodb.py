from .database import *
from .jsonEncoder import *
from bson.objectid import ObjectId
from datetime import datetime,timezone,timedelta
import calendar
from bson import json_util
import json

class User_Info_Database():
    def __init__(self):
        self.user_info_db = database.get_collection("user_info")
    
    def get_personal_image(self,user):
        data_list=[]
        data_list_cursor = self.user_info_db.find({"user":user},{"_id":0,"img":1})
        for data in data_list_cursor:
            data_list.append(JSONEncoder().encode(data))
        return data_list
    
    def update_personal_image(self,img,user):
        result = self.user_info_db.update({"user":user},{'$set':{"img":img}},True,True)
        return str(result["updatedExisting"])