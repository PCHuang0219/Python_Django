import pymongo
from pymongo import MongoClient
from .Config import * 
import datetime
# client = MongoClient('192.168.40.82',27017)
# db = client.test_database
# collection = db.test_collection

# post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.datetime.utcnow()}
# posts = db.posts
# post_id = posts.insert_one(post).inserted_id

class Singleton(type):  
    _instances = {}  
    def __call__(cls, *args, **kwargs):  
        if cls not in cls._instances:  
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)  
        return cls._instances[cls] 

class Database(metaclass=Singleton):
    def __init__(self,):
        self._client = MongoClient(DATABASE_IP,DATABASE_PORT)
        self._db = self._client['user']
        self._collection = None

    def get_collection(self,db_name):
        self._collection = self._db[db_name]
        return self._collection

database = Database()