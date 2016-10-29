import requests
import json

"""Step 3: They send me a string (needle) which maps to an array of strings. 
I need to tell the API where the needly is in the array """

TOKEN = '3723a7f63a07b1c07d836f4e4f95037a'
CHALLENGE_ENDPOINT= 'http://challenge.code2040.org/api/haystack'
VALIDATE_HAYSTACK_ENDPOINT = 'http://challenge.code2040.org/api/haystack/validate'



def get_needle(dictionary):
	needle = dictionary['needle']
	haystack = dictionary['haystack']
	return haystack.index(needle);

def dictionary_from_api():
	my_json = {'token': TOKEN}

	r = requests.post(CHALLENGE_ENDPOINT, data = my_json)

	if(r.status_code == requests.codes.ok):
		jsonResponse = json.loads(r.content)
		return jsonResponse

def validate_needle():
	
	needle_from_haystack = get_needle(dictionary_from_api())
	my_json = {'token': TOKEN, 'needle': needle_from_haystack}	
	r = requests.post(VALIDATE_HAYSTACK_ENDPOINT, data = my_json)
	if(r.status_code == requests.codes.ok):
		print "API says: " + r.content

if __name__ == "__main__":
	validate_needle()