# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(word):
	return all(word[i] == word[-1 - i] for i in range(int(len(word)/2)))

highest = 0
for i in range(10,1000):
	for j in range(10,1000):
		if is_palindrome(str(i*j)) and i*j > highest:
			highest = i*j
print(highest)