import json
import urllib.parse
import urllib.request

def build_url(url, query):
	return url + urllib.parse.urlencode(query)

def get_result(url: str):
	try:
		response = urllib.request.urlopen(url)
		json_text = response.read().decode(encoding = 'utf-8')
		return json.loads(json_text)
	except urllib.request.HTTPError as e:
		return str(e)