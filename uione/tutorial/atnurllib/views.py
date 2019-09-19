from django import template
from django.shortcuts import render
from pprint import pprint
from io import BytesIO
from bs4 import BeautifulSoup as bs
import urllib.request
import json
# for whatever reason, failed to install pycurl
#import pycurl

#import ssl
#import base64
register = template.Library()



"""
Initial view:
https://127.0.0.1:8091
onclick JSON View
https://127.0.0.1:8091/view?p=json

"""
# https://127.0.0.1:8091
def redfishv1(request):
    # remember this format
    if (request.path=='/redfish/v1/'):
        test1 =  ':8091/refdish/v1'
        Loadfromfile = True
        if (Loadfromfile):
            with open('rmm.txt') as f:
                json_str = json.load(f)
            f.close()
            pData = json.loads(json_str)
        else:
            pData = GetURI('https://10.3.0.7:8091/redfish/v1')
            return render(request, 'atnurllib/atnrmmjson.html',
                         {'bodytext': "Bodytext",
                          'emptytext': True,
                          'rmmdics' : pData,
                          'val_1' : request.path,
                         })
    else:
        test1 = ':8091/'
        Loadfromfile = True
        if (Loadfromfile):
            with open('rmm.txt') as f:
                json_str = json.load(f)
            f.close()
            pData = json.loads(json_str)
        else:
            pData = GetURI('https://10.3.0.7:8091/redfish/v1')
            html = "ATN url lib example"
            return render(request, 'atnurllib/atnrmm.html',
                         {'bodytext': "Bodytext",
                          'emptytext': True,
                          'rmmdics' : pData,
                          'val_1' : request.path,
                         })




"""
(not implemented in AS4610)
Function def redfishv1ChassisRackThermalZones1(request):
"""
def redfishv1ChassisRackThermalZones(request):
    Loadfromfile = False
    if (Loadfromfile):
        with open('rmmmsg.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1/ThermalZones')

        # how to process "path?p=/redfish/v1/Chassis/Rack ?

    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "B o d y text",
                   'emptytext': True,
                   'rmmdics' : pData
                   })

"""
(not implemented in AS4610)
Function redfishv1ChassisRackThermalZones1(request):
"""
def redfishv1ChassisRackThermalZones1(request):
    Loadfromfile = False
    if (Loadfromfile):
        with open('rmmmsg.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1/ThermalZones/1')

        # how to process "path?p=/redfish/v1/Chassis/Rack ?

    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "Bodytext",
                   'emptytext': True,
                   'rmmdics' : pData
                   })


"""
(not implemented in AS4610)
Function redfishv1ChassisRackMBPs(request):
"""
def redfishv1ChassisRackMBPs(request):
    Loadfromfile = False
    if (Loadfromfile):
        with open('rmmmsg.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1/Chassis/Rack/MBPs')

        # how to process "path?p=/redfish/v1/Chassis/Rack ?

    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "Bodytext",
                   'emptytext': True,
                   'rmmdics' : pData
                   })

"""
(not implemented in AS4610)
Function redfishv1ChassisRackMBPs1(request):
"""
def redfishv1ChassisRackMBPs1(request):
    Loadfromfile = False
    if (Loadfromfile):
        with open('rmmmsg.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1/Chassis/Rack/MBPs/1')

        # how to process "path?p=/redfish/v1/Chassis/Rack ?

    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "Bodytext",
                   'emptytext': True,
                   'rmmdics' : pData
                   })

"""
(not implemented in AS4610)
Function redfishv1ChassisDrawer1(request):
"""
def redfishv1ChassisDrawer1(request):
    Loadfromfile = False
    if (Loadfromfile):
        with open('rmmmsg.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1/Chassis/Drawer1')

        # how to process "path?p=/redfish/v1/Chassis/Rack ?

    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "Bodytext",
                   'emptytext': True,
                   'rmmdics' : pData
                   })






























"""
Function redfishv1messageRegistry(request):
"""
def redfishv1MessageRegistry(request):
    Loadfromfile = False
    if (Loadfromfile):
        with open('rmmmsg.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1/MessageRegistry')

        # how to process "path?p=/redfish/v1/Chassis/Rack ?

    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "Bodytext",
                   'emptytext': True,
                   'rmmdics' : pData
                   })

"""
Function redfishv1EventServiceSubscriptions(request):
"""
def redfishv1EventServiceSubscriptions(request):
    Loadfromfile = False
    if (Loadfromfile):
        with open('rmmmsg.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1/EventService/Subscriptions')

        # how to process "path?p=/redfish/v1/Chassis/Rack ?

    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "Bodytext",
                   'emptytext': True,
                   'rmmdics' : pData
                   })

"""
Function redfishv1EventService(request):
"""
def redfishv1EventService(request):
    Loadfromfile = False
    if (Loadfromfile):
        with open('rmmmsg.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1/EventService')

        # how to process "path?p=/redfish/v1/Chassis/Rack ?

    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "Bodytext",
                   'emptytext': True,
                   'rmmdics' : pData
                   })


"""
Function redfishv1ManagersRMCNetworkProtocol(request):
"""
def redfishv1ManagersRMCNetworkProtocol(request):
    Loadfromfile = False
    if (Loadfromfile):
        with open('rmmmsg.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1/Managers/RMC/NetworkProtocol')

        # how to process "path?p=/redfish/v1/Chassis/Rack ?

    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "Bodytext",
                   'emptytext': True,
                   'rmmdics' : pData
                   })

"""
Function redfishv1Managers(request):
"""
def redfishv1ManagersRMC(request):
    Loadfromfile = False
    if (Loadfromfile):
        with open('rmmmsg.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1/Managers/RMC')

        # how to process "path?p=/redfish/v1/Chassis/Rack ?

    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "Bodytext",
                   'emptytext': True,
                   'rmmdics' : pData
                   })



"""
Function redfishv1Managers(request):
"""
def redfishv1Managers(request):
    Loadfromfile = False
    if (Loadfromfile):
        with open('rmmmsg.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1/Managers')

        # how to process "path?p=/redfish/v1/Chassis/Rack ?



    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "Bodytext",
                   'emptytext': True,
                   'rmmdics' : pData
                   })

"""
Function redfishv1ChassisRackPowerZones1ActionsPowerZoneRequestStateChange(request):
"""
def redfishv1ChassisRackPowerZones1ActionsPowerZoneRequestStateChange(request):
    Loadfromfile = False
    if (Loadfromfile):
        with open('rmmmsg.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1/Chassis/Rack/PowerZones/1/Actions/PowerZone.RequestStateChange')

        # how to process "path?p=/redfish/v1/Chassis/Rack ?

    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "Bodytext",
                   'emptytext': True,
                   'rmmdics' : pData
                   })


"""
Function redfishv1ChassisRackPowerZones1Actions(request):
"""
def redfishv1ChassisRackPowerZones1Actions(request):
    Loadfromfile = False
    if (Loadfromfile):
        with open('rmmmsg.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1/Chassis/Rack/PowerZones/1/Actions')

        # how to process "path?p=/redfish/v1/Chassis/Rack ?

    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "Bodytext",
                   'emptytext': True,
                   'rmmdics' : pData
                   })

"""
Function redfishv1ChassisRackPowerZones1(request):
"""
def redfishv1ChassisRackPowerZones1(request):
    Loadfromfile = False
    if (Loadfromfile):
        with open('rmmmsg.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1/Chassis/Rack/PowerZones/1')

        # how to process "path?p=/redfish/v1/Chassis/Rack ?

    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "Bodytext",
                   'emptytext': True,
                   'rmmdics' : pData
                   })

"""
Function redfishv1ChassisRackPowerZones(request):
"""
def redfishv1ChassisRackPowerZones(request):
    Loadfromfile = False
    if (Loadfromfile):
        with open('rmmmsg.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1/Chassis/Rack/PowerZones')

        # how to process "path?p=/redfish/v1/Chassis/Rack ?

    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "Bodytext",
                   'emptytext': True,
                   'rmmdics' : pData
                   })

"""
Function redfishv1ChassisRack(request):
"""
def redfishv1ChassisRack(request):
    Loadfromfile = False
    if (Loadfromfile):
        with open('rmmmsg.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1/Chassis/Rack')

        # how to process "path?p=/redfish/v1/Chassis/Rack ?

    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "Bodytext",
                   'emptytext': True,
                   'rmmdics' : pData
                   })





def redfishv1Chassis(request):
    Loadfromfile = False
    if (Loadfromfile):
        with open('rmmmsg.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1/Chassis')

        # how to process "path?p=/redfish/v1/Chassis/Rack ?



    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "Bodytext",
                   'emptytext': True,
                   'rmmdics' : pData
                   })


def redfishv1_OK(request):
    Loadfromfile = False
    if (Loadfromfile):
        with open('rmm.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1')

        # how to process "path?p=/redfish/v1/Chassis/Rack ?



    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "Bodytext",
                   'emptytext': True,
                   'rmmdics' : pData
                   })



def index(request):
    Loadfromfile = True
    if (Loadfromfile):
        with open('rmm.txt') as f:
            json_str = json.load(f)
        f.close()
        pData = json.loads(json_str)
    else:
        pData = GetURI('https://10.3.0.7:8091/redfish/v1')

    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': "Bodytext",
                   'emptytext': True,
                   'rmmdics' : pData
                   })




def GetURI(uri):
    buffer = BytesIO()
    c = pycurl.Curl()
    # c.setopt(c.URL, 'http://www.google.com')
    #c.setopt(c.URL, )
    c.setopt(c.URL, uri)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.SSL_VERIFYPEER, False)
    c.perform()

    body = buffer.getvalue().decode('iso-8859-1')
    pData = json.loads(body)
    # c.close()
    #pData = body
    return pData




# This one works well, the next step is to parse
# json to a table hierarchy for html tag to process
def index14(request):
    #with open('rmm.txt') as f:
    with open('rmmmsg.txt') as f:
        json_str = json.load(f)

    f.close()
    pdata = json.loads(json_str)
    #a = pdata['UUID']
    a = 'body text field'
    html = "ATN url lib example"
    return render(request, 'atnurllib/atnrmm.html',
                  {'bodytext': a,
                   'emptytext': True,
                   'rmmdics' : pdata
                   })

def index12(request):
    response = urllib.request.urlopen('https://192.168.2.117:8091/redfish/v1', data=None, cafile = None, capath=None, \
                                      cadefault=False, context=None )
    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.set_ciphers('ECDHE+AESGCM:!ECDSA')
    ctx.get_ciphers()  # OpenSSL 1.0.x



def index11(request):
    response = urllib.request.urlopen('https://192.168.2.117:8091/redfish/v1', data=None, cafile = None, capath=None, \
                                      cadefault=False, context=None )
    # < urlopen error[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed(_ssl.c: 645) >
    #
    # Request Method:     GET
    # Request URL:        http: // 127.0.0.1: 8000 /
    # Django Version:     2.0
    # Exception Type:     URLError
    # Exception Value:    < urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed(_ssl.c: 645) >
    # Exception Location: / usr / lib / python3.5 / urllib / request.py in do_open, line 1256
    # Python Executable:  / home / jlo / Pyroot / uione / uienv / bin / python
    # Python Version:     3.5.2
    # Python Path:        ['/home/jlo/Pyroot/uione/tutorial',
    #                      '/home/jlo/Pyroot/uione/uienv/lib/python3.5/site-packages/ipmisim-0.7-py3.5.egg',
    #                      '/home/jlo/Pyroot/uione/uienv/lib/python3.5/site-packages/pyghmi-1.0.30-py3.5.egg',
    #                      '/home/jlo/Pyroot/uione/uienv/lib/python3.5/site-packages/pycrypto-2.6.1-py3.5-linux-x86_64.egg',
    #                      '/usr/lib/python35.zip',
    #                      '/usr/lib/python3.5',
    #                      '/usr/lib/python3.5/plat-x86_64-linux-gnu',
    #                      '/usr/lib/python3.5/lib-dynload',
    #                      '/home/jlo/Pyroot/uione/uienv/lib/python3.5/site-packages',
    #                      '/home/jlo/Pyroot/uione/uienv/lib/python3.5/site-packages/IPython/extensions']
    # Server time: Mon, 15 Jan 2018 11: 44:33 + 0000

    html = response.read()

    #print(html)

    return render(request, 'atnurllib/atnurllib.html',
                  {'bodytext': html})



def index010(request):
    #req = urllib.request.Request('https://arstechnica.com', headers=headers)

    # response = urllib.request.urlopen('https://www.google.com', data = None, 0, cafile = None, capath=None, cadefault=False, context=None)
    #                                                                            ^
    #                                                                            SyntaxError: positional argument follows keyword argument

    # response = urllib.request.urlopen('https://www.google.com', data=None, 0)
    # SyntaxError: positional argument follows keyword argument

    #response = urllib.request.urlopen('https://www.google.com', data=None)
    # this one OK

    response = urllib.request.urlopen('https://www.google.com', data=None, cafile = None, capath=None, \
                                      cadefault=False, context=None )
    # this one OK

    #response = urllib.request.urlopen(URL)
    # this one OK

    html = response.read()
    print(html)

    return render(request, 'atnurllib/atnurllib.html',
                  {'bodytext': html})

"""
The Python 3 urllib is made up of the following modules:

    urllib.request
    urllib.error
    urllib.parse
    urllib.rebotparser
"""

# This function is OK
def index009(request):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"

    req = urllib.request.Request('https://arstechnica.com', headers=headers)

    response = urllib.request.urlopen(req)
    html = response.read()
    print(html)


    return render(request, 'atnurllib/atnurllib.html',
                  {'bodytext': html})


def index008(request):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"

    req = urllib.request.Request('https://arstechnica.com', headers=headers)

    # This will leads to an error:
    # urlopen() takes from 1 to 3 positional arguments but 4 were given
    # pay attention, you passed req, not literal string url
    response = urllib.request.urlopen(req, None, 30 ,0)
    html = response.read()
    print(html)

    return render(request, 'atnurllib/atnurllib.html',
                  {'bodytext': html})


def index007(request):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"

    req = urllib.request.Request('https://arstechnica.com', headers=headers)

    # This will leads to an error: 'bytes' object has no attribnute 'read'
    response = urllib.request.urlopen(req).read()
    html = response.read()
    print(html)

    return render(request, 'atnurllib/atnurllib.html',
              {'bodytext': html})

# This one use urllib.request.Request to get req handle
# then call urlopen().read() to open the html page
def index006(request):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"

    req = urllib.request.Request('https://arstechnica.com', headers=headers)
    html = urllib.request.urlopen(req).read()
    print(html)

    return render(request, 'atnurllib/atnurllib.html',
                  {'bodytext': html})

# it works well
def index005(request):
    URL = 'http://www.google.com'
    response = urllib.request.urlopen(URL)
    html = response.read()

    return render(request, 'atnurllib/atnurllib.html',
                  {'bodytext': html})


def index004(request):
    URL = "https://192.168.2.117:8091/redfish/v1"
    URL = "http://www.google.com"

    # You know this one, wrong URL
    # HTTP Error 404: Not Found
    # URL = "http://www.google.com/tw/"

    # you can access google.com but can not access ptt.cc
    # HTTP Error 403: Forbidden
    # URL = "http://www.ptt.cc/index.html"
    # How about https://www.ptt.cc/index.html ?
    # same, maybe because you don't have the header?
    # URL = "https://www.ptt.cc/index.html"

    # this one works, it redirect to https://online.citi.com/US/login.do
    # but it seems to me the return data is wrong, too long.
    # URL = "https://www.citibank.com"
    # URL = "https://online.citi.com/US/login.do"


    # this one works, of cause
    # URL = "http://www.google.com.tw"
    # URL = "http://www.google.com.tw/"

    # this one works too, by design by google.
    # you need more customers connects to your web site
    URL = "https://www.google.com.tw"

    # Let's start parse this web html and format it back to the orginal web
    # layout, use US version is good enough.
    # Try to avoide language related errors
    URL = "https://www.google.com"

    #req = request.urlopen(URL, data=None, [timeout, ] *, cafile=None, capath=None, cadefault=False, context=None)¶
    response = urllib.request.urlopen(URL)

    # google.com reading html and display looks good
    html = response.read()


    return render(request, "atnurllib/atnurllib.html",
                  {'bodytext' : html})
    #return render(request, "atnurllib/atnurllib.html",
    #              {'bodytext': 'done'})


def index003(request):
    TOP_LEVEL_URL = "https://192.168.2.117:8091/redfish/v1"
    request = urllib.request(TOP_LEVEL_URL)
    base64string = base64.b64encode('%s:%s' % ("root", "onl"))
    request.add_header("Authorization", "Basic %s" % base64string)
    result = urllib.urlopen(request)
    return render(request, "atnurllib/atnurllib.html",
                  {'bodytext' : result})


def index002(request):
    # create a password manager
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

    # Add the username and password.
    # If we knew the realm, we could use it instead of None.
    TOP_LELEV_URL = "https://192.168.2.117:8091/redfish/v1"
    password_mgr.add_password(None, TOP_LELEV_URL, "root", "onl")

    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib.request.build_opener(handler)

    # use the opener to fetch a URL
    opener.open(TOP_LELEV_URL)

    # Install the opener.
    # Now all calls to urllib.request.urlopen use our opener.
    #urllib.request.install_opener(opener)

    #response = urllib.request.urlopen(TOP_LEVEL_URL)
    #html_cont = response.read()
    #soup = bs(html_cont, 'html.parser', from_encoding = 'utf-8')

    urls = "Default body text"
    #urls = soup.prettify()

    return render(request, "atnurllib/atnurllib.html",
                  {'bodytext' : urls})


def index001(request):
    #URL = "https://redfish.dmtf.org/redfish/mockups/v1/840"
    URL = "http://www.ibm.com"
           #https://redfish.dmtf.org/redfish/ mockups/v1/840
    #user_agent = {'User-agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.52 Safari/537.17'}
    response = urllib.request.urlopen(URL)
    html_cont = response.read()
    soup = bs(html_cont, 'html.parser', from_encoding = 'utf-8')

    urls = "Default body text"
    #urls = soup.find_all('body')
#    urls = soup.find('body')
    #bug code below, why?
    #urls = print(soup.prettify())

    # OK, so much text, something is NG
    # texts has so much html code inside.
    # urls = soup

    # OK, but half of the page, its lots of text, within the concept of line
    # and spacing.
    #
    #urls = soup.get_text()  #ok, but half page of text

    #
    #  the line below doesn't work, it prints verbatim.
    # it prints exactly like the line below.
    urls = "<table> <thead><th>ID</th><th>name</th></thead><tbody><tr><td>No 1</td><td>James</td></tr></tbody>"

    # my job is to print redfish thing.
    # How can I proceed?
    # I can either get a redfish thing or use node.js build a redfish server
    #
    #urls = urls.prettify()

    #for link in soup.findAll('a'):
    #    print (link['href'])

    return render(request, "atnurllib/atnurllib.html",
                  {'bodytext' : urls})


# Sample code No 2
#
# from django.shortcuts import render
# import urllib.request
# from bs4 import BeautifulSoup as bs
#
#  Create your views here.
# def index(request):
#     URL = "https://redfish.dmtf.org/redfish/mockups/v1"
#     response = urllib.request.urlopen(URL)
#     html_cont = response.read()
#     soup = bs(html_cont, 'html.parser', from_encoding = 'utf-8')
#
#     urls = "Default body text"
#     urls = soup.find_all('body')
#
#     return render(request, "atnurllib/atnurllib.html",
#                   {'bodytext' : urls})


# Sample code No 1
#
# from django.shortcuts import render
#
# Create your views here.
# def index(request):
#     return render(request, "atnurllib/atnurllib.html")
