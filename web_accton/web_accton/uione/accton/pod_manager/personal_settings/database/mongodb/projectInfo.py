from datetime import datetime,timezone,timedelta

def get_time_now():
    dt = datetime.utcnow()
    dt = dt.replace(tzinfo=timezone.utc)
    tzutc_8 = timezone(timedelta(hours=8))
    local_dt = dt.astimezone(tzutc_8)
    return str(local_dt).split('.')[0]

class Bug_Issue_Information():
    def __init__(self,user,project,start_time,end_time,TRR_ID):
        self.user = user
        self.project = project
        self.start_time = start_time
        self.end_time = end_time
        self.status = "Submitted"
        self.submit_time = get_time_now()
        self.TRR_ID = TRR_ID

    def to_json(self):
        return {'user':self.user,\
                'project':self.project,\
                'start_time':self.start_time,\
                'end_time':self.end_time,\
                'submit_time':self.submit_time,\
                'status':self.status, \
                'TRR_ID':self.TRR_ID}

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
    def __init__(self,user,project,TRR_ID,issue):
        self.user = user
        self.TRR_ID = TRR_ID
        self.project = project
        self.issue = issue
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
                'issue':self.issue,\
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