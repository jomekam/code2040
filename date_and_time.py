import requests
import json
import dateutil

"""Step 4: Given a prefix value that is a string, and a second value, an array of string,
return the array containing only the strings that do not start with that prefix """

TOKEN = '3723a7f63a07b1c07d836f4e4f95037a'
CHALLENGE_ENDPOINT= 'http://challenge.code2040.org/api/dating'
VALIDATE_DATE_ENDPOINT = 'http://challenge.code2040.org/api/dating/validate'

#Return an array
def check_date (dictionary):
	datetime = dictionary['datestamp']
	interval = dictionary['interval']
	date_parsed =dateutil.parser.parse(datetime)
	print date_parsed.relativedata(seconds =interval).normalized()
	#http://dateutil.readthedocs.io/en/stable/relativedelta.html

def dictionary_from_api():
	my_json = {'token': TOKEN}

	r = requests.post(CHALLENGE_ENDPOINT, data = my_json)

	if(r.status_code == requests.codes.ok):
		jsonResponse = json.loads(r.content)
		return jsonResponse

def validate_date():
	
	datestamp = check_date(dictionary_from_api())
 	my_json = {'token': TOKEN, 'datestamp': datestamp}
	r = requests.post(VALIDATE_DATE_ENDPOINT, data = my_json)
	print r.content
	if(r.status_code == requests.codes.ok):
		print "API says: " + r.content

if __name__ == "__main__":
	validate_date()