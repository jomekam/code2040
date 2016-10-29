#AUTHOR: JIDE OMEKAM
import requests
import json
from interface_methods import connect, make_dictionary


"""Step 4: Given a prefix value that is a string, and a second value, an array of string,
return the array containing only the strings that do not start with that prefix """

CHALLENGE_ENDPOINT= 'http://challenge.code2040.org/api/prefix'
VALIDATE_PREFIX_ENDPOINT = 'http://challenge.code2040.org/api/prefix/validate'

#Walks through a given list of words, and checks if one is
#a substring of another
def get_non_prefix(dictionary):
	prefix = dictionary['prefix']
	string_list = dictionary['array']
	non_prefix_list = []
	for word in string_list:
		if( prefix not in word):
		  	non_prefix_list.append(word)
	return non_prefix_list
	

def dictionary_from_api():
	return json.loads(connect(my_json = make_dictionary(), endpoint = CHALLENGE_ENDPOINT))


def validate_prefix():
	connect(my_json = make_dictionary('array', get_non_prefix(dictionary_from_api())),
		endpoint = VALIDATE_PREFIX_ENDPOINT) 

if __name__ == "__main__":
	validate_prefix()

