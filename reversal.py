#AUTHOR: JIDE OMEKAM

from interface_methods import connect, make_dictionary


"""Step 2: Reverse a string. While I simply put the characters onto a stack,
this is a more efficient way to not allocate space and I still only walk through
the string once"""

CHALLENGE_ENDPOINT= 'http://challenge.code2040.org/api/reverse'
VALIDATE_REVERSE_ENDPOINT = 'http://challenge.code2040.org/api/reverse/validate'


def reverse(string):
	#Reverse it using list splicing, python
	return string[::-1]

#See interface_methods.py for clarity
def string_from_api():
	return connect(my_json = make_dictionary(), endpoint = CHALLENGE_ENDPOINT)

	
def validate_reversal():
	connect(my_json = make_dictionary('string', reverse(string_from_api())), 
		endpoint = VALIDATE_REVERSE_ENDPOINT)



if __name__ == "__main__":
	validate_reversal()