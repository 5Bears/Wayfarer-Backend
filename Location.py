import json
import urllib.parse
import urllib.request
from APIFunctions import build_url, get_result
from uuid import getnode as get_mac

mac = hex(get_mac())
base_url = 'https://www.googleapis.com/geolocation/v1/geolocate?'

def format_mac(mac):
	return mac[2] + mac[3] + ':' + mac[4] + mac[5] + ':' + mac[6] + mac[7] + ':' + mac[8] + mac[9] + ':' + mac[10] + mac[11] + ':' + mac[12] + mac[13]

query_parameters = [('key', 'AIzaSyCEFLuWX5CR7WXS5ELgT5dq3JwMDKL1pbc'),
					('wifiAccessPoints', [('macAddress)', format_mac(mac))])]

print(format_mac(mac))
print(build_url(query_parameters, base_url))
print(get_result(build_url(query_parameters, base_url)))