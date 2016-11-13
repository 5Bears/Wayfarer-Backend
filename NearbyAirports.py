from APIFunctions import build_url, get_result
from Location import get_latitude, get_longitude

base_url = 'https://api.sandbox.amadeus.com/v1.2/airports/nearest-relevant?'

latitude = 37.7749				#Replace with function call get_latitude
longitude = -122.4194			#Replace with function call get_longitude

query_parameters = [	('apikey', 't7q7kkgRGApdJFDr40W2pGVVAdk7mt7V'),
						('latitude', latitude),
						('longitude', longitude)]

airports = get_result(build_url(base_url, query_parameters))

def nearby_airports(airports):
	list_of_airports = []
	for i in airports:
		if i["distance"] < 80:
			list_of_airports.append(i["airport"])
	return list_of_airports