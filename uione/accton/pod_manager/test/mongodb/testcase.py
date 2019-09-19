class Testcase:
    def __init__(self,test_string,index):
        self.case,self.name,self.topo = self.split_string(test_string)
        self.status = "not running"
        self.start_time = "NULL"
        self.end_time = "not finished"
        self.log_path = "not finished"
        self.result = "not finished"        
        self.index = index

    def split_string(self,test_string):
        name = test_string.split('/')[0]
        case = test_string.split('/')[1]
        topo = test_string.split('/')[2]
        return case,name,topo

    def to_json(self):
        return {'test_id':self.index,\
            'test_case':self.case,\
            'test_name':self.name,\
            'test_topo':self.topo,\
            'test_status':self.status,\
            'test_start_time':self.start_time,\
            'test_end_time':self.end_time,\
            'test_log_path':self.log_path,\
            'test_result':self.result}