# You are given a scrambled input sentence. Each word
# is scrambled independently, and the results are concatenated. So: 

# 'hello to the world' 
# might become: 
# 'elhloothtedrowl' 

# You have a dictionary with all words in it. Unscramble the sentence.

dictionary = ["hello", "my", "name", "is", "romulus", "remus", "fun"]

# create a dictionary for reach value in the dictionary(array)
# parse string: 
# add each char to a dict
# if dict equals some dict in the dictionary dicts:
# 	then add to result
# 	create new dictionary

def unscramble(string, dictionary):
	def getTotals(string):
		total = {}
		for y in string:
			if total.has_key(y):
				total[y] += 1
			else:
				total[y] = 0
		return total
	all_totals = []
	for word in dictionary:
		all_totals.append(getTotals(word))
	output = []
	current = ""
	for char in string:
		current += char
		currentTotals = getTotals(current)
		for iTotal in range(len(all_totals)):
			if currentTotals == all_totals[iTotal]:
				output.append(dictionary[iTotal])
				current = ""
				break
	return output

print unscramble("hlloeymamensi", dictionary)



