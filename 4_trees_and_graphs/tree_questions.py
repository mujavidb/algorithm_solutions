class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right = self.left = None

def getAllPaths(root):
	if not root:
		return ["None"]
	paths = [ str(root.val) + "->" + path for path in getAllPaths(root.left)]
	paths.extend([ str(root.val) + "->" + path for path in getAllPaths(root.right)])
	return paths

# create adjacency matrix
# start page
	#check if the url is end_page
		#return the url
	#get all of the links
	#search those pages
	#create an array