# Print a two dimensional array in spiral order
# e.g. array = [
# 	[1,2,3,4],
# 	[5,6,7,8],
# 	[9,10,11,12],
# 	[13,14,15,16]
#]
# print spiral(array) # 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
# 1. Print top row
# 2. Rotate the list
# 3. Repeat

def spiral(matrix):
    if not matrix:
    	return ""
    
    # join top row into a string
    top_row =  " ".join([str(item) for item in matrix[0]])
    
    # reverse all remaining rows of the matrix
    reversed_rows = [ reversed(row) for row in matrix[1:]]
    
    # create tuples of new rows from columns in all rows
    rotated_columns = zip(*reversed_rows)

    return top_row + " " + spiral(rotated_columns)

matrix = [
[1,2,3,4],
[12,13,14,5],
[11,16,15,6],
[10,9,8,7],
]

print spiral(matrix)