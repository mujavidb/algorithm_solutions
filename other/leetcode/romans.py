def romanToInt(s):
    rom = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
    total = 0
    for i in range(len(s)):
        if i == len(s) - 1:
            total += rom[s[i]]
        else:
            if rom[s[i]] >= rom[s[i+1]]:
                total += rom[s[i]]
            else:
                total -= rom[s[i]]
    return total

def intToRoman(self, num):
    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10]