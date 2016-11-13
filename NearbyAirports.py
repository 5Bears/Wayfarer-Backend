from APIFunctions import build_url, get_result

base_url = 'https://api.sandbox.amadeus.com/v1.2/airports/nearest-relevant?'

latitude = 37.7749
longitude = -122.4194

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