from django.shortcuts import render
from django.http import HttpResponse
from .models import t1

# Create your views here.
def index3(request):
    #return HttpResponse('Home -> Ipmitool Page')
    return render(request, 'ipmitool/ipmitool_form.html')


def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def index(request):
    tlists = t1.objects.all()
    return render(request, 'ipmitool/t1form.html',
                  {'tlists':tlists  }
                 )



def index4(request):

    return index(request)


"""
from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request, 'books/search_results.html',
                      {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')



import pyipmi
import pyipmi.interfaces

# Supported interface_types for ipmitool are: 'lan' , 'lanplus', and 'serial-terminal'
interface = pyipmi.interfaces.create_interface('ipmitool', interface_type='lan')

connection = pyipmi.create_connection(interface)

connection.target = pyipmi.Target(0xb2)
connection.target.set_routing([(0x20,0)])

connection.session.set_session_type_rmcp('10.0.0.1', port=623)
connection.session.set_auth_type_user('admin', 'admin')
connection.session.establish()

connection.get_device_id()
"""

# How to convert it to a function call?
#
#

# Data from SMCIPMI Tool User Guide
# 3.6.1 ipmi sensor

#Example Output:
#Getting SDR data ...
#Getting sensors ...

#Status | Sensor              | Reading  | Low Limit | High Limit |
#------ | ---------           | -------  | --------- | ---------- |
#OK     | (7) CPU1 Temp       |-----Low  | --------- | ---------- |
#OK     | (8) CPU2 Temp       |-----Low  | --------- | ---------- |
#OK     | (9) System Temp     |63C/145F  |   -5C/23F |   75C/167F |
#OK     | (10) CPU1 Vcore     | 0.92 V   |    0.82 V |     1.35 V |
#OK     | (11) CPU2 Vcore     | 0.88 V   |    0.82 V |     1.35 V |
#OK     | (12) +5V            | 5.12 V   |    4.48 V |     5.53 V |
#OK     | (13) +5VSB          | 5.12 V   |    4.48 V |     5.53 V |
#OK     | (14) +12V           | 12.19 V  |     10.7V |     13.25V |
#OK     | (15) -12V           | -11.99 V |  -12.58 V |   -11.22 V |
#OK     | (16) +3.3V          | 3.26 V   |    2.92 V |     3.64 V |
#OK     | (17) +3.3VSB        | 3.24 V   |    2.92 V |     3.64 V |
#OK     | (18) VBAT           | 3.21 V   |    2.92 V |     3.64 V |
#OK     | (19) Fan1           | 4320 RPM |   675 RPM |  34155 RPM |
#       | (20) Fan2           | 0 RPM    |   675 RPM |  34155 RPM |
#OK     | (21) Fan3           | 4320 RPM |   675 RPM |  34155 RPM |
#OK     | (22) Fan4           | 4185 RPM |   675 RPM |  34155 RPM |
#       | (23) Fan5           | 0 RPM    |   675 RPM |  34155 RPM |
#       | (24) Fan6           | 0 RPM    |   675 RPM |  34155 RPM |
#       | (25) Fan7           | 0 RPM    |  675 RPM  |  34155 RPM |
#       | (26) Fan8           | 0 RPM    |  675 RPM  |  34155 RPM |
#OK     | (27) P1-DIMM1A Temp | 47C/117F |   -5C/23F |   75C/167F |
#       | (28) P1-DIMM1B Temp | N/A      |   -5C/23F |   75C/167F |
#OK     | (29) P1-DIMM2A Temp | 48C/118F |   -5C/23F |   75C/167F |
#       | (30) P1-DIMM2B Temp | N/A      |   -5C/23F |   75C/167F |
#OK     | (31) P1-DIMM3A Temp | 46C/115F |   -5C/23F |   75C/167F |
#       | (32) P1-DIMM3B Temp | N/A      |   -5C/23F |   75C/167F |
#OK     | (33) P2-DIMM1A Temp | 38C/100F |   -5C/23F |   75C/167F |
#       | (34) P2-DIMM1B Temp | N/A      |   -5C/23F |   75C/167F |
#OK     | (35) P2-DIMM2A Temp | 37C/99F  |   -5C/23F |   75C/167F |
#       | (36) P2-DIMM2B Temp | N/A      |   -5C/23F |   75C/167F |
#OK     | (37) P2-DIMM3A Temp | 37C/99F  |   -5C/23F |   75C/167F |
#       | (38) P2-DIMM3B Temp | N/A      |   -5C/23F |   75C/167F |





