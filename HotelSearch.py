from APIFunctions import build_url, get_result
import FlightLowFareSearch

base_url = 'https://api.sandbox.amadeus.com/v1.2/hotels/search-airport?'
location = FlightLowFareSearch.destination
check_in = FlightLowFareSearch.arrive_by[:10]
check_out = FlightLowFareSearch.return_date
radius = '30'
max_rate = '60'
number_of_results = '1'

query_parameters = [('apikey', 't7q7kkgRGApdJFDr40W2pGVVAdk7mt7V'),
					('location', location),
					('check_in', check_in),
					('check_out', check_out), 
					('radius', radius), 
					('max_rate', max_rate), 
					('number_of_results', number_of_results)]

hotel = get_result(build_url(base_url, query_parameters))

def get_hotel_name(hotel):
	return hotel["results"][0]["property_name"]

def get_hotel_address(hotel):
	return hotel["results"][0]["address"]["line1"] + ', ' + hotel["results"][0]["address"]["city"] + ', ' + hotel["results"][0]["address"]["region"] + ' ' + hotel["results"][0]["address"]["postal_code"] + ' ' + hotel["results"][0]["address"]["country"]

def get_total_price(hotel):
	return '$' + hotel["results"][0]["total_price"]["amount"]

def get_daily_rate(hotel):
	return '$' + hotel["results"][0]["min_daily_rate"]["amount"]

def get_contact_info(hotel):
	return hotel["results"][0]["contacts"][0]["type"] + ': ' + hotel["results"][0]["contacts"][0]["detail"] + '; ' + hotel["results"][0]["contacts"][1]["type"] + ': ' + hotel["results"][0]["contacts"][0]["detail"]

def get_amenities(hotel):
	return [i["amenity"] for i in hotel["results"][0]["amenities"]]

def get_descriptions(hotel):
	return hotel["results"][0]["rooms"][0]["descriptions"]

def get_room_type(hotel):
	return hotel["results"][0]["rooms"][0]["room_type_info"]["room_type"]

def get_bed_type(hotel):
	return hotel["results"][0]["rooms"][0]["room_type_info"]["number_of_beds"] + ' ' + hotel["results"][0]["rooms"][0]["room_type_info"]["bed_type"]