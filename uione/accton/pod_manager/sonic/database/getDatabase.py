import pandas as pd
import pymongo
from pymongo import MongoClient
import json
from bson import ObjectId
from ...Config import *

class Singleton(type):  
    _instances = {}  
    def __call__(cls, *args, **kwargs):  
        if cls not in cls._instances:  
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)  
        return cls._instances[cls] 

class Database(metaclass=Singleton):
    def __init__(self,):
        self._client = MongoClient(MONGODB_HOST,MONGODB_PORT)
        self._db = self._client['device']
        self._collection = None

    def get_collection(self,db_name):
        self._collection = self._db[db_name]
        return self._collection


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

database = Database()


def get_device():

    table = database.get_collection('device_feature')
    a = list(table.find({}))
    # for i in a:
    #     data_list.append()
    thejson = json.dumps({'data':a}, cls=JSONEncoder)
    thejson = json.loads(thejson)
    print(type(thejson))
    return thejson

def get_software():

    table = database.get_collection('software')
    a = list(table.find({}))
    # for i in a:
    #     data_list.append()
    thejson = json.dumps({'data':a}, cls=JSONEncoder)
    thejson = json.loads(thejson)
    print(type(thejson))
    return thejson