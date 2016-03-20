class Node():
	def __init__(self, value):
		self.value = value
		self.next = None

def addNode(root, value):
	if not root.next:
		root.next = Node(value)
	else:
		current = root
		while current.next:
			current = current.next
		current.next = Node(value)

def printList(root):
	while root:
		print " " + str(root.value),
		root = root.next
	print

def reverseLL(root):
	array = []
	while root:
		array.append(root.value)
		root = root.next
	new = Node(array.pop())
	while array:
		addNode(new, array.pop())
	return new

root = Node(5)
addNode(root, 6)
addNode(root, 7)
addNode(root, 8)
addNode(root, 9)
addNode(root, 10)
printList(root)
root = reverseLL(root)
printList(root)