#Given an image represented by an NxN matrix, where
#each pixel in the image is 4 bytes, write a method
#to rotate the image by 90 degrees counter-clockwise. Can you do this in place?

def rotate(image):
    if not matrix:
    	return []
    reversed_rows = [row[::-1] for row in matrix]
    rotated_columns = zip(*reversed_rows)
    for i in range(len(rotated_columns)):
        rotated_columns[i] = list(rotated_columns[i])
    return rotated_columns

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]

print rotate(matrix)
