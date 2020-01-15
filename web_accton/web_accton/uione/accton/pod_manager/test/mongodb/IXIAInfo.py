from datetime import datetime,timezone,timedelta
from .testcase import Testcase
class IXIA_Information():
    def __init__(self,location,model,port_number,status,ToRack,ToDevice,owner,description,end_time="Null"):
        self.location = location
        self.model = model
        self.port_number = port_number
        self.status = status
        self.ToRack = ToRack
        self.ToDevice = ToDevice
        self.owner = owner
        self.description = description
        self.start_time = self.get_time_now()
        self.end_time = "NULL"
        
    def get_time_now(self):
        dt = datetime.utcnow()
        dt = dt.replace(tzinfo=timezone.utc)
        tzutc_8 = timezone(timedelta(hours=8))
        local_dt = dt.astimezone(tzutc_8)
        return str(local_dt).split('.')[0]

    def to_json(self):
        if self.status == "In Use":
            return {'location':self.location,\
                    'model':self.model,\
                    'port_number':self.port_number,\
                    'status':self.status,\
                    'ToRack':self.ToRack,\
                    'ToDevice':self.ToDevice,\
                    'owner':self.owner,\
                    'description':self.description,\
                    'start_time':self.start_time,\
                    'end_time':self.end_time}
        return {'location':self.location,\
                'model':self.model,\
                'port_number':self.port_number,\
                'status':self.status,\
                'ToRack':self.ToRack,\
                'ToDevice':self.ToDevice,\
                'owner':self.owner,\
                'description':self.description,\
                'start_time':self.start_time,\
                'end_time':self.end_time}

class IXIA_Schedule():
    def __init__(self,owner,card,port,start_time,end_time,cable,toDevice):
        self.owner = owner
        self.card = card
        self.port = port
        self.start_time = self.split_date('start',start_time)
        self.end_time = self.split_date('end',end_time)
        self.cable = cable
        self.toDevice = toDevice
    
    def split_date(self,time_type,date):
        if time_type == 'start':
            date = datetime.strptime(date, "%Y-%m-%d")
        elif time_type == 'end':
            date += ' 23:59:59'
            date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        return date

    def to_json(self):
        return {'owner':self.owner, \
                'card':self.card, \
                'port':self.port, \
                'start_time':self.start_time, \
                'end_time':self.end_time, \
                'cable':self.cable, \
                'toDevice':self.toDevice}

class Device_Data():
    def __init__(self,rack,location,model,platform,console,IP,user,power,status,PDU):
        self.rack = rack
        self.location = location
        self.model = model
        self.platform = platform
        self.console = console
        self.IP = IP
        self.user = user
        self.power = power
        self.status = status
        self.PDU = PDU
        self.submit_time = self.get_now_time()

    def get_now_time(self):
        dt = datetime.utcnow()
        dt = dt.replace(tzinfo=timezone.utc)
        tzutc_8 = timezone(timedelta(hours=8))
        local_dt = dt.astimezone(tzutc_8)
        return str(local_dt).split('.')[0]
    
    def to_json(self):
        return {'rack':self.rack, \
            'location':self.location, \
            'model':self.model, \
            'platform':self.platform, \
            'console':self.console, \
            'IP':self.IP, \
            'user':self.user, \
            'power':self.power, \
            'status':self.status, \
            'PDU':self.PDU, \
            'submit_time':self.submit_time}