# Given a string, return the string with duplicate characters removed

def remove_dups(string):
    chars = ""
    for x in string:
        if x not in chars:
            chars += x
    print chars

def remove_dups_fast(string):
    hashmap = {}
    chars = ""
    for x in string:
        if not hashmap.has_key(x):
            hashmap[x] = True
            chars += x
    print chars

remove_dups("StringOfThingsToSay")
remove_dups_fast("StringOfThingsToSay")