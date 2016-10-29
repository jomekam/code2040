# code2040
API Challenge CODE2040

#AUTHOR: JIDE OMEKAM

interface_methods:
	This class is where I abstract methods that can and are used across different classes,
	by doing so, I am abstracting repetitive post requests and dictionary creation code
	This make things cleaner, and better, in the event that I need to narrow down bugs

	Also, there is one token, so I don't need to copy and paste it into every file
	r.status_code was just to ensure that I got back a response

Disclaimer: While it was reasonable to assume that the inputs given were valid from the API from the scope of this challenge, it should be noted that edge cases for null, length 0, bad format, etc. could have been check, but I was told that it was a reasonable assumption to make

See comments in other files for the other respective classes