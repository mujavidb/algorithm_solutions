# Given a string, return whether it is made of a perfectly repeated string pattern.

# 1. Correctly solve the problem
# 2. Run test cases
# 3. What is the complexity?
# 4. How would you optimize this?


# 1: Brute force test increasingly larger string against test_string
def basic_check_string(test_string):
	length = 1
	string_length = len(test_string)
	max_length = string_length / 2
	while length <= max_length:
		interval = string_length / length
		for x in range(0, string_length , interval):
			if x == string_length - interval and test_string[:length] == test_string[x:x + length]:
				return True
			if test_string[:length] != test_string[x:x + length]:
				break
		length +=1
	return False


# 2: Run test cases
print basic_check_string('aaaaaaaaa')
print basic_check_string('abcabcabcabc')
print basic_check_string('abcabcadcabc')

# 3: What is the complexity?




# 4. How would you optimize this?
