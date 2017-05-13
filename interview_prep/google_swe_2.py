
# receive image as 2d array of pixel (r, g, b) values
# 6*12
# iterate over 2d array
# 	for each block to be converted:
# 		find average color
# 		find ascii representation for that color
# 		print ascii value to std out
# 		if EOL print return
# [
# 	[(r, g, b), (r, g, b), (r, g, b), (r, g, b), (r, g, b), (r, g, b)]
# 	[(r, g, b), (r, g, b), (r, g, b), (r, g, b), (r, g, b), (r, g, b)],
# 	[(r, g, b), (r, g, b), (r, g, b), (r, g, b), (r, g, b), (r, g, b)],
# 	[(r, g, b), (r, g, b), (r, g, b), (r, g, b), (r, g, b), (r, g, b)],
# 	[(r, g, b), (r, g, b), (r, g, b), (r, g, b), (r, g, b), (r, g, b)]
# ]

colors = [ ' ', '.', '=', '#' ]
# 255/4 = 66 + 128 + 191 + 255


def averageRGB(array):
	colorHash = {}
	colorHash[0] = colorHash[1] = colorHash[2] = 0
	for row in array:
		for column in row:
			colorHash[0] += column[0]
			colorHash[1] += column[1]
			colorHash[2] += column[2]
	totalValues = len(array) * len(array[0])
	average = [int(colorHash[0]/totalValues), int(colorHash[1]/totalValues), int(colorHash[2]/totalValues)]
	return average

# level = 28
# endSize = 4
# 63.75 + 128 + 191 + 255
# 0
#
# level = 82
#endSize = 4
#66 + 128 + 191 + 255
#1
#level // (255/ endSize)
#1

def findBrightnessIndex(level, endSize):
      # level: 0..255
      # index: 0..(endSize-1)
	return level // (255/ endSize)

def getASCIIImage(image):
	rowSize = 12 #height
	colSize = 6 #width
	for i in xrange(0, len(image), rowSize):
		for j in xrange(0, len(image[0]), colSize):
			subArray = image[i:i+rowSize][j:j+colSize]
			averageColor = averageRGB(subArray) #(r, g, b)
			averageBrightness = int(avg(averageColor))
			colorIndex = findBrightnessIndex(averageBrightness, len(colors))
			print colors[colorIndex],
		print








