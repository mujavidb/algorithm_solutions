#Write a method to decide if two strings are anagrams or not.

def anaCheck(string1, string2):
	h1 = {}
	h2 = {}
	for x in string1:
		if not h1.has_key(x):
			h1[x] = 0
		else:
			h1[x] += 1
	for x in string2:
		if not h2.has_key(x):
			h2[x] = 0
		else:
			h2[x] += 1
	if h1 == h2:
		return True
	else:
		return False

print anaCheck("love", "voler")