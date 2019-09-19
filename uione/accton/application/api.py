#import urllib2, json
import urllib, json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context # disabled SSL authentication

# ----- common function : RESFull -----
'''
url    [String] : IP for device. EX : https://127.0.0.1
port   [String] : port for device
cmd    [String] : command
head   [String] : HTTP header. EX : key1:val1,key2:val2,key3:val3
'''
def get_data(url: object, port, cmd, head):
	ret_data = []
	uri =  url + ":" + port + '/redfish/v1/' + cmd
	#print uri
	req = urllib2.Request(uri)
	if  head != '' :
		head_data = head.split(',')
		for head_data in head_data:
			b_str = head_data.split(':')
			req.add_header(b_str[0], b_str[1]) 

#	try :
		response = urllib2.urlopen(req)
# jlo comment out for compile 12/23/2017
#	except urllib2.URLError, e:
#	    ret_status = e.reason
#	    return ret_status

	#print response.getcode()
# jlo comment out for compile
#	ret_data = response.read()

#	return json.loads(ret_data)
#	return { ': get_data()' }

def get_rack_power():
	data_list = []

	ret = get_data('https://192.168.11.195', '8091', 'Chassis/Rack/powerZones', '')	
	if type(ret).__name__ == "error" :
		msg = {'ret_msg': ret}
		return msg
	elif type(ret).__name__ == "str" :
		if ret == "Resource not found" :
			msg = {'ret_msg': ret}
			return msg

	if ret['Members@odata.count'] == 0 :
		msg = {'ret_msg': "No information"}
		return msg

	for i in range(0, ret['Members@odata.count'] , 1):
		power_id = ret['Members'][i]['@odata.id'].split('/')[-1]
		ret = get_data('https://192.168.11.195', '8091', 'Chassis/Rack/powerZones/'+ power_id, '')
		data = {'Id': ret['Id'], 'Description': ret['Description'], 'PowerConsumedWatts': ret['PowerConsumedWatts']}
		data_list.append(data)
		
	return data_list

def get_rack_thermal():
	data_list = []
	ret = get_data('https://192.168.11.195', '8091', 'Chassis/Rack/ThermalZones', '')
	if type(ret).__name__ == "error" :
		msg = {'ret_msg': ret}
		return msg
	elif type(ret).__name__ == "str" :
		if ret == "Resource not found" :
			msg = {'ret_msg': ret}
			return msg

	if ret['Members@odata.count'] == 0 :
		msg = {'ret_msg': "No information"}
		return msg

	for i in range(0, ret['Members@odata.count'] , 1):
		thermal_id = ret['Members'][i]['@odata.id'].split('/')[-1]
		ret = get_data('https://192.168.11.195', '8091', 'Chassis/Rack/ThermalZones/'+ thermal_id, '')
		data = {'Id': ret['Id'], 'Description': ret['Description'], 'PowerConsumedWatts': ret['PowerConsumedWatts']}
		data_list.append(data)
		
	return data_list



