###############################
# BITWISE LEARNINGS ###########
###############################


# DIFFERENCE BETWEEN X AND X-1

# Consider a number x. 
# Now think about the binary representation of (x-1). 
# (x-1) will have all the bits same as x, except for the
# rightmost 1 in x and all the bits to the right of the rightmost 1. 
# 
# Let x = 4 = (0b100)
# x - 1 = 3 = (0b011)
# Let y = 6 = (0b110)
# y - 1 = 5 = (0b101)
# 
# The binary representation of (x-1) can be obtained by 
# flipping all the bits to the right of rightmost 1 in x
# and also including the rightmost 1.


# POWERS OF TWO HAVE ONLY ONE BIT SET (&)

# Properties for numbers which are powers of 2, is that they 
# have one and only one bit set. If the number is neither zero nor 
# a power of two, it will have 1 in more than one place. So if x 
# is a power of 2 then x & (x-1) will be 0.
# 
# Let x = 4 = (0b100) 
# x - 1 = 3 = (0b011)
# x & (x-1) = (0b000)


# REMOVING THE RIGHTMOST 1 IN BINARY (&)

# By understanding the above two rules, we can use these to convert
# the rightmost 1 into a 0.
#
# Let x = 12 = (0b1100) 
# x - 1 = 11 = (0b1011)
#  x & (x-1) = (0b1000)
#  
# Notice above that the operation x & (x-1) removed the 1
# in the 4s column of the binary number.


# CHECK IF THE i_th BIT IS SET USING AND (&)

# Since we know that powers of two only have one bit set.
# We can use the AND operator in conjunction with 2^i to confirm
# if the i_th bit is set.
# 
# Let i = 4 //Check if the 4th bit is set
# Let n = 18 = 0b10010
# x = (1<<i) = 0b10000
# 	   n & x = 0b10000
# By checking if n & x is falsy we can confirm if the i_th bit is set.


# SETTING RIGHT-ADJECT BITS TO 1s (OR, >>)

# We can set bits that are right-adjacent to 1s to 1. We do this
# be first shifting a number by some bits and ORing it against the original.
# 
# Let x 	   = 0b10001000
# x << 1 	   = 0b01000100
# x | (x << 1) = 0b11001100 //After ORing, we have doubled the ones
# x = x | (x << 1)
# x | (x << 2) = 0b11111111 //By left shifting by 2, we quadruple the ones
# 
# Using the following principle we can set all bits in an integer to 1
# by applying the following. This is for 16-bit integers, but can be
# expanded to include 32 and 64 bit integers.
# 
# N = N| (N>>1);
# N = N| (N>>2);
# N = N| (N>>4);
# N = N| (N>>8);













