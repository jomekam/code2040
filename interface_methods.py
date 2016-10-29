#AUTHOR: JIDE OMEKAM
import requests
TOKEN = '3723a7f63a07b1c07d836f4e4f95037a'


#Because I am connecting to an API at each stage,
#it was necessary to extract this common method
def connect(my_json, endpoint):
	r = requests.post(endpoint, json = my_json)
	if(r.status_code == requests.codes.ok):
		print "API Says: " + r.content
		return r.content


def make_dictionary(key = None, value = None):
	dictionary = { 'token': TOKEN}
	if key is None or value is None:
		return dictionary
	dictionary[key] = value
	return dictionary