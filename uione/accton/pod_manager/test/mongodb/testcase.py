import json

class Testcase:
    def __init__(self, test_string, platform, index, thread_id):
        self.platform = platform
        self.case, self.name, self.topo, self.stage_id, self.time_period = self.split_string(test_string)
        self.status = "not running"
        self.start_time = ["NULL"]
        self.end_time = ["not finished"]
        self.during_time = ["not finished"]
        self.log_path = "not finished"
        self.result = ["not finished"]
        self.index = index
        self.thread_id = thread_id

    def split_string(self,test_string):
        test_string = json.loads(test_string)
        if self.platform == "SONiC":
            name = test_string['TD']
            case = test_string['TC'].split("--")[1]
            topo = case.split("--")[1]
            stage_id = ""
            time_period = ""
        else:
            ## Anber: Need to fix,for non_SONiC_Ansible format
            name = test_string['TD']
            case = test_string['TC']
            topo = ""
            stage_id = test_string['stage_id']
            time_period = test_string['time_period']
        return case, name, topo, stage_id, time_period

    def to_json(self):
        return {'test_id':self.index,\
            'test_case':self.case,\
            'test_name':self.name,\
            'test_topo':self.topo,\
            'test_status':self.status,\
            'test_start_time':self.start_time,\
            'test_end_time':self.end_time,\
            'test_during_time':self.during_time,\
            'test_log_path':self.log_path,\
            'test_result':self.result, \
            'test_thread_id': self.thread_id, \
            'test_time_period': self.time_period, \
            'test_stage_id':self.stage_id}