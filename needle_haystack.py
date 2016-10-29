#AUTHOR: JIDE OMEKAM

import json
from interface_methods import connect, make_dictionary


"""Step 3: They send me a string (needle) which maps to an array of strings. 
I need to tell the API where the needly is in the array """

CHALLENGE_ENDPOINT= 'http://challenge.code2040.org/api/haystack'
VALIDATE_HAYSTACK_ENDPOINT = 'http://challenge.code2040.org/api/haystack/validate'


#Returns the index of the given index in a list.
#Haystack was a key to a given list
#Needle was what you needed to find within that list
def get_needle(dictionary):
	return dictionary['haystack'].index(dictionary['needle']);

#See interface_methods.py for clarity 
def dictionary_from_api():
	return json.loads(connect(my_json = make_dictionary(), endpoint = CHALLENGE_ENDPOINT))

	 
def validate_needle():
	connect(my_json = make_dictionary('needle', get_needle(dictionary_from_api())),
		endpoint = VALIDATE_HAYSTACK_ENDPOINT) 


if __name__ == "__main__":
	validate_needle()