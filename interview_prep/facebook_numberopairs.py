#Facebook 2016 hackathon question

def numberOfPairs( a,  k):
    hashmap = {}
    counter = 0
    repeats = []
    for x in a:
        if not hashmap.has_key(k - x):
            hashmap[x] = x
        else:
            if x not in repeats:
            	counter+=1
            	repeats.append(x)
    print counter

numberOfPairs([1,3,46,1,3,9], 47)
numberOfPairs([6,6,3,9,3,5,1], 12)
numberOfPairs([1,4,5,6,2,4,5,7,8], 13)
