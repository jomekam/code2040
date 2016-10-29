import requests
import json

"""Step 4: Given a prefix value that is a string, and a second value, an array of string,
return the array containing only the strings that do not start with that prefix """

TOKEN = '3723a7f63a07b1c07d836f4e4f95037a'
CHALLENGE_ENDPOINT= 'http://challenge.code2040.org/api/prefix'
VALIDATE_PREFIX_ENDPOINT = 'http://challenge.code2040.org/api/prefix/validate'

#Return an array
def get_non_prefix(dictionary):
	prefix = dictionary['prefix']
	string_list = dictionary['array']
	non_prefix_list = []
	for word in string_list:
		if( prefix not in word):
		  	non_prefix_list.append(word)
	return non_prefix_list
	

def dictionary_from_api():
	my_json = {'token': TOKEN}
	r = requests.post(CHALLENGE_ENDPOINT, data = my_json)

	if(r.status_code == requests.codes.ok):
		jsonResponse = json.loads(r.content)
		return jsonResponse

def validate_prefix():
	
	non_prefix_list = get_non_prefix(dictionary_from_api())
 	my_json = {'token': TOKEN, 'array': non_prefix_list}

	r = requests.post(VALIDATE_PREFIX_ENDPOINT, json = my_json)
	if(r.status_code == requests.codes.ok):
		print "API says: " + r.content

if __name__ == "__main__":
	validate_prefix()

