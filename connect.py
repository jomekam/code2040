#AUTHOR: JIDE OMEKAM
from interface_methods import connect, make_dictionary

CONNECT_START = 'https://github.com/jomekam/code2040'
CHALLENGE_ENDPOINT = "http://challenge.code2040.org/api/register"

"""Step 1: Connect to CODE2040 challenge endpoint and send the required data in 
JSON format. """

#Main line function for python files
if __name__ == "__main__":
	#See interface_methods.py for more on how connect works to the given API
	connect(my_json = make_dictionary('github', CONNECT_START), 
		endpoint = CHALLENGE_ENDPOINT)
	
