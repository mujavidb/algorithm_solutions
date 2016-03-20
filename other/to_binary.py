def to_bin(n):
   result = ""
   shift = 31
   while shift >= 0:
      d = n >> shift
      if d & 1:
         result += '1'
      else:
         result += '0'
      print str(shift) + " - " + str(d)
      shift -=1
   print result

to_bin(13)