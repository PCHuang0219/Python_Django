import csv
import os
from os import listdir
from os import path
import json
from tempfile import NamedTemporaryFile
import shutil

class Database():
    def __init__(self):
        self.output_log_dir_path = "./../../job_log"
        self.output_csv_dir_path = "./../../output_csv"
        self.job_csv_path = "./../../output_csv/job.csv"
        self.image_csv_path = "../../data/image.csv"

    def generate_csv_path(self,job_id,type_name):
        job_csv_path = os.path.join(self.output_csv_dir_path,job_id)
        test_info_csv_path = os.path.join(job_csv_path, type_name+ ".csv")  
        return test_info_csv_path

    def generate_log_path(self,job_id,test_name,test_topo):
        job_dir_log_path = os.path.join(self.output_log_dir_path,job_id)
        test_log_path = os.path.join(job_dir_log_path,test_name + "-" + test_topo)
        return test_log_path
    
    def make_dir(self,path):
        if(not os.path.exists(path)):
            os.mkdir(path)

