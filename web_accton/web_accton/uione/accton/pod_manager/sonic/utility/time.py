import pytz
from datetime import datetime, timezone

def get_time_expression(past_seconds):
    past_seconds = int(past_seconds)
    if(past_seconds > 86400):
        return str(int(past_seconds/86400)) + "day"
    elif(past_seconds > 3600):
        return str(int(past_seconds/3600)) + "hour"
    elif(past_seconds > 60):
        return str(int(past_seconds/60)) + "minute"
    else:
        return str(int(past_seconds)) + "second"

def substract_time_by_now(time):
    tz = pytz.timezone('Asia/Shanghai')
    now = datetime.now(tz).replace(tzinfo=None)
    past_time = now - time
    return past_time.seconds

def change_time_mode(time_string):
    return time_string.replace('T',' ').split('.')[0]