import csv
import os
from os import listdir
from os import path
import json
from tempfile import NamedTemporaryFile
import shutil
from .Database import Database

class UpdateDatabase(Database):
    def __init__(self):
        Database.__init__(self)
    
    def update_start_job_information(self,data):
        job_id = data['job_id']
        status = data['status']
        start_time = data['start_time']
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        fields = ['job_name','job_description','job_id','status','result','start_time','end_time','model','topology','platform']

        with open(self.job_csv_path, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                if row['job_id'] == str(job_id):
                    print('updating start job table row', row['job_id'])
                    row['status'] = status
                    row['start_time'] = start_time
                row = {'job_name': row['job_name'], 'job_description': row['job_description'], 'job_id': row['job_id'], \
                        'status': row['status'], 'result': row['result'],'start_time': row['start_time'],'end_time': row['end_time'], \
                        'model': row['model'], 'topology': row['topology'], 'platform': row['platform']}
                writer.writerow(row)

        shutil.move(tempfile.name, self.job_csv_path)

    def update_job_result_information(self,data):
        job_id = data['job_id']
        result = data['result']
        status = data['status']
        end_time = data['end_time']
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        fields = ['job_name','job_description','job_id','status','result','start_time','end_time','model','topology','platform']

        with open(self.job_csv_path, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                if row['job_id'] == str(job_id):
                    print('updating job table row', row['job_id'])
                    row['status'] = status
                    row['result'] = result
                    row['end_time'] = end_time
                row = {'job_name': row['job_name'], 'job_description': row['job_description'], 'job_id': row['job_id'], \
                        'status': row['status'], 'result': row['result'],'start_time': row['start_time'],'end_time': row['end_time'], \
                        'model': row['model'], 'topology': row['topology'], 'platform': row['platform']}
                writer.writerow(row)

        shutil.move(tempfile.name, self.job_csv_path)

    def update_start_test_information(self,data):
        job_id = data['job_id']
        test_case = data['test_case']
        test_topo = data['test_topo']
        status = data['status']
        start_time = data['start_time']
        filename = self.generate_csv_path(job_id,"test")
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        fields = ['test_name', 'test_case', 'test_topology', 'status', 'result','start_time','end_time','log_path']

        with open(filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)

            for row in reader:
                if row['test_case'] == str(test_case) and row['test_topology'] == str(test_topo):
                    print('updating test table row', row['test_case'])
                    row['status'] = status
                    row['start_time'] = start_time
                    row['result'] = "running"
                    row['end_time'] = "running"

                row = {'test_name': row['test_name'], 'test_case': row['test_case'], 'test_topology': row['test_topology'], \
                        'status': row['status'], 'result': row['result'],'start_time': row['start_time'],'end_time': row['end_time'], \
                        'log_path': row['log_path']}
                writer.writerow(row)

        shutil.move(tempfile.name, filename)

    def update_finished_test_information(self,data):
        job_id = data['job_id']
        test_case = data['test_case']
        test_topo = data['test_topo']
        test_name = data['test_name']
        result = data['result']
        print("-------------------************************")
        print(result)
        status = data['status']
        start_time = data['start_time']
        end_time = data['end_time']

        filename = self.generate_csv_path(job_id,"test")
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        fields = ['test_name', 'test_case', 'test_topology', 'status', 'result','start_time','end_time','log_path']

        with open(filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                if row['test_case'] == str(test_case) and row['test_topology'] == str(test_topo):
                    print('updating finished test table row', row['test_case'])
                    row['test_name'], row['test_case'], row['test_topology'], row['status'], \
                    row['result'] , row['start_time'], row['end_time'] ,row['log_path'] \
                    = test_name, test_case, test_topo, status, result, start_time, end_time, self.generate_log_path(job_id,test_name,test_topo)
                row = {'test_name': row['test_name'], 'test_case': row['test_case'], 'test_topology': row['test_topology'], \
                        'status': row['status'], 'result': row['result'],'start_time': row['start_time'],'end_time': row['end_time'], \
                        'log_path': row['log_path']}
                writer.writerow(row)

        shutil.move(tempfile.name, filename)

        
        
