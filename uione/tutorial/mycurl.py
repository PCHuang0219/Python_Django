import pycurl
import json
from io import BytesIO
#import libaccton

buffer = BytesIO()
c = pycurl.Curl()
#c.setopt(c.URL, 'http://www.google.com')
c.setopt(c.URL, 'https://10.3.0.7:8091/redfish/v1')
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.SSL_VERIFYPEER, False)
c. perform()
# c.close()

body = buffer.getvalue().decode('iso-8859-1')
"""
json_str == p_data.py
{'@odata.id': '/redfish/v1/$metadata#ServiceRoot',

 'UUID': 'f13fbf02-      '}
"""


"""
Function: Loadrmm(): 
"""
def Loadrmm():
    with open('rmm.txt') as f: 
        json_str = json.load(f)
    f.close()
    p_data = json.loads(json_str)
    return p_data


"""
if the value equals to {'@odata.id':  I need to add a hypterlink
"""
def printpdata(p):
    for index in p:
        print(index)
    for index in p:
        print('i + index')
        print(index.key, index.value)
    return p

"""
if the value equals to {'@odata.id':  I need to add a hypterlink
"""
def ifhyperlink(p):
    if '@odata.id' in p:
        return True
    else:
        return False



"""
Function GetURI(uri)
"""
def GetURI(uri):
    buffer = BytesIO()
    c = pycurl.Curl()
    # c.setopt(c.URL, 'http://www.google.com')
    #c.setopt(c.URL, 'https://10.3.0.7:8091/redfish/v1')
    c.setopt(c.URL, uri)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.SSL_VERIFYPEER, False)
    c.perform()

    body = buffer.getvalue().decode('iso-8859-1')
    # c.close()
    #pData = body
    return body




    """
    json_str == p_data.py
    {'@odata.id': '/redfish/v1/$metadata#ServiceRoot',

     'UUID': 'f13fbf02-      '}
    """
