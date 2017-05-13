class TreeNode:
	def __init__(self, value, args*):
		self.value = value
		self.children = [ x for x in args[1:]]


# Create a function to calculate the height of an n-ary tree.
def getTreeHeight(root):
	if not root:
		return -1
	return max([getTreeHeight(x) for x in root.children]) + 1

def getMaxLength(root):