# Given an array of randomly arranged lower case letters, uppercase letters, and numbers, sort the array such that all lower case letters come before all uppercase letters, come before all numbers. The classes of characters do not need to be in order in their respective sections.

def sort_alpha(string):
    new_string = ""
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    for x in lower:
        if x in string:
            new_string += x
    for y in upper:
        if y in string:
            new_string += y
    for z in numbers:
        if z in string:
            new_string += z
    print new_string

sort_alpha("abcDEG783sbgh8493Bbsdwe")