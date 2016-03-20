#Given an image represented by an NxN matrix, where
#each pixel in the image is 4 bytes, write a method 
#to rotate the image by 90 degrees. Can you do this in place?

def rotate(image):
    if not matrix:
    	return ""
    
    # reverse all remaining rows of the matrix
    reversed_rows = [ reversed(row) for row in matrix ]
    
    # create tuples of new rows from columns in all rows
    rotated_columns = zip(*reversed_rows)

    for i in len(rotated_columns): rotated_columns[i] = list(rotated_columns[i])

    return rotated_columns

matrix = [
	[1,2,3,4],
	[12,13,14,5],
	[11,16,15,6],
	[10,9,8,7],
]

print rotate(matrix)