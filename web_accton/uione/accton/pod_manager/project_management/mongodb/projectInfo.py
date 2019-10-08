from datetime import datetime,timezone,timedelta

def get_time_now():
    dt = datetime.utcnow()
    dt = dt.replace(tzinfo=timezone.utc)
    tzutc_8 = timezone(timedelta(hours=8))
    local_dt = dt.astimezone(tzutc_8)
    return str(local_dt).split('.')[0]

class Bug_Issue_Information():
    def __init__(self,data):
        self.user = data["user"]
        self.project = data["project"]
        self.start_time = data["start_time"]
        self.end_time = data["end_time"]
        self.status = "Submitted"
        self.submit_time = get_time_now()
        self.TRR_ID = data["TRR_ID"]
        self.module = data["module"]
        self.code = data["code"]
        self.bios = data["bios"]
        self.diag = data["diag"]
        self.cpld = data["cpld"]
        self.onie = data["onie"]
        self.SW = data["S/W"]
        self.HW = data["H/W"]
        self.test_type = data["test_type"]
        self.test_phase = data["test_phase"]
        self.boot = data["boot"]
        self.profile_name = data["profile_name"]

    def to_json(self):
        return {'user':self.user,\
                'project':self.project,\
                'start_time':self.start_time,\
                'end_time':self.end_time,\
                'submit_time':self.submit_time,\
                'status':self.status, \
                'TRR_ID':self.TRR_ID, \
                'module':self.module, \
                'code':self.code, \
                'bios':self.bios, \
                'diag':self.diag, \
                'cpld':self.cpld, \
                'onie':self.onie, \
                'S/W':self.SW, \
                'H/W':self.HW, \
                'test_type':self.test_type, \
                'test_phase':self.test_phase, \
                'boot':self.boot, \
                'profile_name':self.profile_name}

class Bug_Issue_Comment():
    def __init__(self,user,project,TRR_ID,description):
        self.user = user
        self.TRR_ID = TRR_ID
        self.project = project
        self.description = description
        self.submit_time = self.get_time_now()
        
    def get_time_now(self):
        dt = datetime.utcnow()
        dt = dt.replace(tzinfo=timezone.utc)
        tzutc_8 = timezone(timedelta(hours=8))
        local_dt = dt.astimezone(tzutc_8)
        return str(local_dt).split('.')[0]

    def to_json(self):
        return {'user':self.user,\
                'TRR_ID':self.TRR_ID,\
                'project':self.project,\
                'description':self.description,\
                'submit_time':self.submit_time}

class Bug_Issue():
    def __init__(self,user,project,TRR_ID,issue,mail):
        self.user = user
        self.TRR_ID = TRR_ID
        self.project = project
        self.issue = issue
        self.submit_time = self.get_time_now()
        self.mail = mail
        
    def get_time_now(self):
        dt = datetime.utcnow()
        dt = dt.replace(tzinfo=timezone.utc)
        tzutc_8 = timezone(timedelta(hours=8))
        local_dt = dt.astimezone(tzutc_8)
        return str(local_dt).split('.')[0]

    def to_json(self):
        return {'user':self.user,\
                'TRR_ID':self.TRR_ID,\
                'project':self.project,\
                'issue':self.issue,\
                'mail':self.mail,\
                'submit_time':self.submit_time}

class Main_Project_Information():
    def __init__(self,user,cust_model,project_name,description,customer):
        self.user = user
        self.cust_model = cust_model
        self.project_name = project_name
        self.submit_time = self.get_time_now()
        self.status = 'Submitted'
        self.description = description
        self.customer = customer
        # self.modelPart_no = modelPart_no
        # self.PL = PL
        # self.PCBA = PCBA
        # self.customer = customer
        # self.OEMCode = OEMCode
        
    def get_time_now(self):
        dt = datetime.utcnow()
        dt = dt.replace(tzinfo=timezone.utc)
        tzutc_8 = timezone(timedelta(hours=8))
        local_dt = dt.astimezone(tzutc_8)
        return str(local_dt).split('.')[0]

    def to_json(self):
        return {'user':self.user,\
                'cust_model':self.cust_model,\
                'project_name':self.project_name,\
                'description':self.description, \
                'submit_time':self.submit_time, \
                'customer':self.customer}