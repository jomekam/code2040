import requests

TOKEN = '3723a7f63a07b1c07d836f4e4f95037a'
CONNECT_START = 'https://github.com/jomekam/code2040'
CHALLENGE_ENDPOINT = "http://challenge.code2040.org/api/register"


"""Step 1: Connect to CODE2040 challenge endpoint and send the required data in 
JSON format. """

def connect():
	my_json = {'token': TOKEN, 'github': CONNECT_START }

	r = requests.post(CHALLENGE_ENDPOINT, data = my_json)
	if(r.status_code == requests.codes.ok):
		print "API Responsed with: " + r.content


if __name__ == "__main__":
	connect()
	
