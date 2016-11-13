#import json
#import urllib.parse
#import urllib.request
from APIFunctions import build_url, get_result

base_url = 'https://api.sandbox.amadeus.com/v1.2/flights/inspiration-search?'

query_parameters = [	('apikey', 't7q7kkgRGApdJFDr40W2pGVVAdk7mt7V'),
						('origin', 'NYC'),
						('destination', 'LAX'),
						('departure_date', '2016-12-01--2016-12-29'),
						('one-way', 'false'),
						('duration', '1--15'),
						('direct', 'false'),
						('max_price', '400')]



