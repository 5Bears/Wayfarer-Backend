from APIFunctions import build_url, get_result
from NearbyAirports import nearby_airports
import NearbyAirports 

base_url = "https://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?"
origins = nearby_airports(NearbyAirports.airports)
destination = 'LAX'														#Replace with variable that takes user input
departure_date = '2016-11-25'											#''	
return_date = '2016-12-1'												#''
arrive_by = '2016-11-25T16:00'											#''	
return_by = '2016-12-01T08:00'											#''
adults = '9'															#''
children = '0'															#''
infants = '0'															#''
nonstop = 'false'														#''		
max_price_per_adult = 300												#''	
max_price = str(max_price_per_adult*(int(adults) + int(children)))
number_of_results = '1'													#''	

results = []

def flights(base_url, origins, destination, departure_date, return_date, arrive_by, return_by, adults, children, infants, nonstop, max_price, number_of_results):
	for origin in origins:
		query_parameters = [('apikey', 't7q7kkgRGApdJFDr40W2pGVVAdk7mt7V'),
							('origin', origin),
							('destination', destination),
							('departure_date', departure_date), 
							('return_date', return_date), 
							('arrive_by', arrive_by), 
							('return_by', return_by), 
							('adults', adults),
							('children', children),
							('infants', infants),
							('nonstop', nonstop),
							('max_price', max_price),
							('number_of_results', number_of_results)]
		results.append(get_result(build_url(base_url, query_parameters)))
	return results

def get_price_per_adult(flight):  #flight should be an element from the list returned from the function flights (i.e. results[0] or results[1])
	return '$' + flight["results"][0]["fare"]["price_per_adult"]["total_fare"]

#outbound flight info

def get_outbound_airline(flight):
	return flight["results"][0]["itineraries"][0]["outbound"]["flights"][0]["marketing_airline"]

def get_outbound_flight_number(flight):
	return flight["results"][0]["itineraries"][0]["outbound"]["flights"][0]["flight_number"]	

def get_outbound_departure_time(flight):
	return flight["results"][0]["itineraries"][0]["outbound"]["flights"][0]["departs_at"]

def get_outbound_arrival_time(flight):
	return flight["results"][0]["itineraries"][0]["outbound"]["flights"][0]["arrives_at"]

def get_outbound_origin_terminal(flight):
	return flight["results"][0]["itineraries"][0]["outbound"]["flights"][0]["origin"]["terminal"]

def get_outbound_destination_terminal(flight):
	return flight["results"][0]["itineraries"][0]["outbound"]["flights"][0]["destination"]["terminal"]

def get_outbound_travel_class(flight):
	return flight["results"][0]["itineraries"][0]["outbound"]["flights"][0]["booking_info"]["travel_class"]

#inbound flight info

def get_inbound_airline(flight):
	return flight["results"][0]["itineraries"][0]["inbound"]["flights"][0]["marketing_airline"]

def get_inbound_flight_number(flight):
	return flight["results"][0]["itineraries"][0]["inbound"]["flights"][0]["flight_number"]	

def get_inbound_departure_time(flight):
	return flight["results"][0]["itineraries"][0]["inbound"]["flights"][0]["departs_at"]

def get_inbound_arrival_time(flight):
	return flight["results"][0]["itineraries"][0]["inbound"]["flights"][0]["arrives_at"]

def get_inbound_origin_terminal(flight):
	return flight["results"][0]["itineraries"][0]["inbound"]["flights"][0]["origin"]["terminal"]

def get_inbound_destination_terminal(flight):
	return flight["results"][0]["itineraries"][0]["inbound"]["flights"][0]["destination"]["terminal"]

def get_inbound_travel_class(flight):
	return flight["results"][0]["itineraries"][0]["inbound"]["flights"][0]["booking_info"]["travel_class"]

flights(base_url, origins, destination, departure_date, return_date, arrive_by, return_by, adults, children, infants, nonstop, max_price, number_of_results)

"""examples on how to call:

	>>> get_outbound_airline(results[0])
	UA
	>>> get_inbound_flight_number(results[0])
	414

	"""
