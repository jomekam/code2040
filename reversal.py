import requests

"""Step 2: Reverse a string. While I simply put the characters onto a stack,
this is a more efficient way to not allocate space and I still only walk through
the string once"""

TOKEN = '3723a7f63a07b1c07d836f4e4f95037a'
CHALLENGE_ENDPOINT= 'http://challenge.code2040.org/api/reverse'
VALIDATE_REVERSE_ENDPOINT = 'http://challenge.code2040.org/api/reverse/validate'


def reverse(string):
	reversed_string = ""
	string_length = len(string)
	if(string_length == 0 or string is None):
		return reversed_string
	if(string_length == 1):
		return string

	#Reverse it using list splicing, python
	return string[::-1]

def string_from_api():
	my_json = {'token': TOKEN}

	r = requests.post(CHALLENGE_ENDPOINT, data = my_json)

	if(r.status_code == requests.codes.ok):
		print "Initial Post Result: " + r.content
		return r.content

def validate_reversal():
	reversed_string = reverse(string_from_api())
	my_json = {'token': TOKEN, 'string': reversed_string }	
	r = requests.post(VALIDATE_REVERSE_ENDPOINT, data = my_json)
	if(r.status_code == requests.codes.ok):
		print "Reversed Post Result: " + reversed_string
		print "Later Post Result: " + r.content

if __name__ == "__main__":
	validate_reversal()