#AUTHOR: JIDE OMEKAM
import json
import dateutil.parser
from datetime import timedelta, datetime
from interface_methods import connect, make_dictionary


"""Step 4: Given a prefix value that is a string, and a second value, an array of string,
return the array containing only the strings that do not start with that prefix """

TOKEN = '3723a7f63a07b1c07d836f4e4f95037a'
CHALLENGE_ENDPOINT= 'http://challenge.code2040.org/api/dating'
VALIDATE_DATE_ENDPOINT = 'http://challenge.code2040.org/api/dating/validate'



def check_date (dictionary):

	#Grab data from API and use string parsing appropriately
	dictionary_dt = dictionary['datestamp']
	interval = dictionary['interval']
	date_parsed = str(dateutil.parser.parse(dictionary_dt))

	#Parse the interval of seconds and change it into Hour:Minute:Seconds
	#so you can intuitively know how to add

	#Reverse this list in case your seconds converts beyond hours, and
	#into days
	time_to_add = str(timedelta(seconds = interval)).split(", ")[::-1]
	add_time = time_to_add[0]
	#In the event that you have a day to add
	time_to_add_date = None
	if(len(time_to_add) > 1):
		time_to_add_date = time_to_add[1]

	#Grab the time zone, current time, and T to indicate time
	time_zone = dictionary_dt[len(dictionary_dt)-1]
	date = date_parsed.split(" ")[0]
	curr_time = date_parsed.split(" ")[1].split("+")[0]
	T = 'T'


	#Employ understanding of datetime objects to parse and add appropriately
	d1 = datetime.strptime(add_time, "%H:%M:%S")
	dt1 = timedelta(hours = d1.hour, minutes = d1.minute, seconds = d1. second)
	d2 = datetime.strptime(curr_time, "%H:%M:%S")
	dt2 = timedelta(hours = d2.hour, minutes = d2.minute, seconds = d2. second)
	fin = dt1 + dt2
	final_extra = str(fin).split(", ")[::-1]

	#Now you have decomposed your dates, and your time. And you want to
	#add the nessary times back together
	#Grab total amount of extra days
	date_two = 0
	if (time_to_add_date is not None):
		date_two += int(time_to_add_date.split(" ")[0])
	if(len(final_extra) > 1):
		date_two += int(final_extra[1].split(" ")[0])

	#Now you have your days and time you need to add
	date_split = date.split("-")
	year = date_split[0]
	month = date_split[1]
	day = date_split[2]


	#Add days appropriately
	date_one = datetime(int(year), int(month), int(day))
	if(date_two > 0):
		date_one  += timedelta(days = date_two)

	final_time = final_extra[0].split(":")
	i = 0

	#Format correctly and return
	for x in final_time:
		if(len(x) == 1):
			final_time[i] = "0" + x
	i+=1

	
	return str(date_one).split(" ")[0] +T+ final_extra[0]+ time_zone
	

#See interface_methods.py for clarity
def dictionary_from_api():
	return json.loads(connect(my_json = make_dictionary(), endpoint = CHALLENGE_ENDPOINT))


def validate_date():
	connect(my_json = make_dictionary('datestamp', 
		check_date(dictionary_from_api())),
		endpoint = VALIDATE_DATE_ENDPOINT) 



if __name__ == "__main__":
	validate_date()

