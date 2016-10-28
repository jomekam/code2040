import requests

TOKEN = '3723a7f63a07b1c07d836f4e4f95037a'
REPO = 'https://github.com/jomekam/code2040'
CHALLENGE_ENDPOINT = "http://challenge.code2040.org/api/register"


"""Step 1: Connect to CODE2040 challenge endpoint and send the required data in 
JSON format. """

def connect():

	my_json = {'token': TOKEN, 'github': REPO }

	r = requests.post(CHALLENGE_ENDPOINT, data = my_json)
	
	print "API Response: " + r.content



if __name__ == "__main__":
	connect()