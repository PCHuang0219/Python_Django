class TestCaseData():
    def __init__(self,Test_name,Topo_type,Category):
        self.test_name = Test_name
        self.topo_type = Topo_type
        self.category = Category
        self.start_time = ""
        self.end_time = ""
        self.status = "not run yet"
        self.spend_time = ""
        self.output = ""
        self.result = ""
        self.log_file_path = ""
    
    def calculate_spend_time(self):
        self.spend_time = self.end_time - self.start_time
        return self.spend_time