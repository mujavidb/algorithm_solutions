#3456 - MMM,CD,L,VI

#3000 - MMM
#0400 - CD
#0050 - L
#0006 - VI

#004 - IV - 1,5,10
#040 - XL - 10,50,100
#400 - CD - 100,500,1000

#1010 - 


class Solution:
    def intToRoman(self, n):
        strInt = str(n)[::-1]
        result = ""
        tensCount = 1
        length = len(strInt)
        for i in range(length):
            if strInt[i] == "0":
                tensCount +=1
                continue        
            else:
                result = self.convert(strInt[i],tensCount) + result
                tensCount +=1
        return result
        
    def convert(self, number, tensCount):
        numerals = {
            "1": "I",
            "2": "II",
            "3": "III",
            "4": "IV",
            "5": "V",
            "6": "VI",
            "7": "VII",
            "8": "VIII",
            "9": "IX",
            "10": "X",
            "50": "L",
            "100": "C",
            "500": "D",
            "1000": "M"            
        }
        previousTen = numerals[str(10 ** (tensCount - 1))]
        nextTen = numerals[str(10 ** tensCount)] if tensCount < 4 else previousTen
        currentFive = numerals[str((10 ** tensCount) / 2)] if tensCount < 4 else numerals[str((10 ** (tensCount - 1)) / 2)]
        rFives = numerals[number].replace("V", currentFive)
        rOnes = rFives.replace("X", nextTen)
        rTens = rOnes.replace("I", previousTen)
        if int(number) < 10:
            return rTens
        else:
            return nextTen + rTens

a = ["1030","22", "133", "10", "456", "3409"]
b = 1
c = Solution()
for x in a:
    print c.intToRoman(x)