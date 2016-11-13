from APIFunctions import build_url, get_result

base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
address = '355 Roseland Place Union NJ'

query_parameters = [('address', address),
					('key', 'AIzaSyBlfi7_RqUEGq7yO39DvAbu2TYy4PEnszo')]

location = get_result(build_url(base_url, query_parameters))

def get_latitude(location):
	return location["results"][0]["geometry"]["location"]["lat"]

def get_longitude(location):
	return location["results"][0]["geometry"]["location"]["lng"]