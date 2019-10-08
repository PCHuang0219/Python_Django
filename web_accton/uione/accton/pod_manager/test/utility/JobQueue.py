class JobQueue():
    def __init__(self):
        self.job_queue = []
        self.now_exec_job = ""
        self.finish_job = []

    def add_job_into_queue(self,job):
        self.job_queue.append(job)
    
    def get_queue_length(self):
        return len(self.job_queue)
    
    def get_oldest_job(self):
        self.now_exec_job = self.job_queue.pop(0)
        return self.now_exec_job
        
    def get_now_job_status(self,job_id):
        if(type(self.now_exec_job) == str ):
            if(job_id == "now"):
                return {"job_status":"no running job"}
            else:
                return "old data"
        if(job_id == "now" or str(job_id) == str(self.now_exec_job.job_id)):
            return self.now_exec_job.get_status()
        else:
            return "old data"
    
    def get_now_test_log(self):
        return self.now_exec_job.get_now_test_log()
        '''
        if(type(self.now_exec_job) == str):
            return {"job_status":"finished"}
        if((str(self.now_exec_job.status) == "running")):
            return self.now_exec_job.get_now_test_log()
        else:
            return {"job_status":"finished"}
        '''        

    
