import csv
import os

def getJobData():
    PATH = "./../../output_csv"
    data_list = []
    for job_id_dir in os.listdir(PATH):
        dir_path = os.path.join(PATH,job_id_dir) 
        csv_path = os.path.join(dir_path,"job.csv")
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append({"job_id":row['job_id'], \
                    "job_name":row['job_name'], \
                    "job_description":row['job_description'], \
                    "job_result":row['result'], \
                    "start_time":row['start_time'], \
                    "end_time":row['end_time'] \
                    })
    return sorted(data_list, key = lambda i: i['start_time'],reverse=True) 

def getTestData(job_id):
    PATH = "./../../output_csv"
    data_list = []
    for job_id_dir in os.listdir(PATH):
        if(str(job_id) == job_id_dir):
            dir_path = os.path.join(PATH,job_id_dir) 
            csv_path = os.path.join(dir_path,"test.csv")
            with open(csv_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    data_list.append({"test_name":row['test_id'], \
                        "test_status":row['status'], \
                        "result":row['result'], \
                        "start_time":row['start_time'], \
                        "end_time":row['end_time'] \
                        })
    return sorted(data_list, key = lambda i: i['start_time']) 