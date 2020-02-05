import jenkins

class Jenkins_conn():
    def __init__(self):
        self.jenkins_url = "http://jlo:9abcdegf!~00012@192.168.40.82:8080/"
        self.server = self.Connect()
        self.jobs = self.get_jenkins_jobs

    def Connect(self):
        self.server = jenkins.Jenkins(self.jenkins_url)
        return self.server

    def get_jenkins_jobs(self):
        job_list=[]
        jobs = self.server.get_jobs()
        for job_info in jobs:
            job_name = job_info["name"]
            job_list.append(job_name)
        return job_list

    def get_jenkins_builds_number(self,job_name):
        builds_number = self.get_jenkins_job_info(job_name)["builds"]["number"]
        return builds_number

    def get_jenkins_job_info(self,job_name):
        job_info = self.server.get_job_info(job_name)
        return job_info
    
    def get_jenkins_build_info(self,job_name,build_number):
        build_info = self.server.get_build_info(job_name,build_number)
        return build_info

    def get_jenkins_build_result(self,job_name,build_number):
        build_result = self.server.get_build_info(job_name,int(build_number))["result"]
        return build_result
    
    def submit_jenkins_build(self,job_name):
        result = self.server.build_job(job_name)
        return result

    def get_jenkins_running_builds(self):
        running_builds = self.server.get_running_builds()
        return running_builds