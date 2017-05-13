# Please use this Google doc to code during your interview. To free your hands for coding, we recommend that you use a headset or a phone with speaker option.


# bit.ly/   goo.gl/ 


# http://www.google.com?q=Alan+Parson -> http://bit.ly/a435dr


# http://bit.ly/a435dr
# http://www.google.com?q=Alan+Parson


# http://www.google.com?q=Alan+Parson -> a435dr
# http://bit.ly/a435dr -> a435dr -> http://www.google.com?q=Alan+Parson


# architechture
# what
# how


# alphaneumeric string a-z, A-Z, 0-9
# six chars

# http://www.google.com?q=Alan+Parson
# a435dr
# if exists:
# 	use new key a435dr to get new shortened_version
# if not exists:
# 	persist


# Sites
# id | real_url | shortened_version
# id | http://www.google.com?q=Alan+Parson | a435dr


# http://bit.ly/a435dr
# shortened_version == "a435dr"
# if found:
# 	redirect_to http://www.google.com?q=Alan+Parson
# if not found:
# 	redirect error_page

def generateShortVersion():
	arrays = {}
	arrays[0] = ["a", "b", "c", ..., "z"]
	arrays[1] = ["A", "B", "C", ..., "Z"]
	arrays[2] = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]
	final_string = ""
	for i in range(6):
		randomArray = rand(0,2)
		randomChar = rand(0, len(arrays[randomArray]) - 1)
		newChar = arrays[randomArray][randomChar]
		final_string += newChar
	return final_string

# randArray = 2
# randChar = 8
# newChar = 7
# final_string = "f7"

# CLEANER (POST-INTERVIEW)
from random import choice
def generateShortVersion():
	lowers = ["a", "b", "c", ..., "z"]
	uppers = ["A", "B", "C", ..., "Z"]
	numbers = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]
	arrays = [lowers, upperse, numbers]
	return [choice(choice(arrays)) for i in range(6)]




