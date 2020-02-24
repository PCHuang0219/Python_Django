from django.shortcuts import render

# Create your views here.
from application import api 

def mainpage(request): 	
	print(request.user)
	print(request.user.id)
	return render(request, 'main_page.html')

def login(request): 
	return render(request, 'login.html')


# http://127.0.0.1:8000/overview
def overview(request): 
	return render(request, 'overview.html')

def components(request): 
	return render(request, 'components.html')

def components16(request):
	return render(request, 'components16.html')

def system(request):
	return render(request, 'system.html')

def page(request):
	return render(request, 'page.html',
				  {"power_zone": 'Power Zone Value',
				   "thermal_zone" : 'Thermal Value'})

"""           
def page(request): 
return render(request, 'page.html',
  {
	  "power_zone" : api.get_rack_power() ,
	  "thermal_zone" : api.get_rack_thermal()
  })
"""

def switches(request): 
	return render(request, 'switches.html')

def racks(request): 
	return render(request, 'racks.html')

def storage(request): 
	return render(request, 'storage.html')

def nvme(request): 
	return render(request, 'nvme.html')

def blades(request): 
	return render(request, 'blades.html')
