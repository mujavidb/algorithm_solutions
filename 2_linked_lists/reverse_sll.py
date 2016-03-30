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
		print str(root.value) + " ",
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

#O(n) recursive possible
#O(n) with two pointers possible

def linearReverse(root):
	if root.next:
		head = root
		current = root.next
		while current:
			temp = current
			root.next = current.next
			current = root.next
			temp.next = head
			head = temp
		return head

root = Node(5)
addNode(root, 6)
addNode(root, 7)
addNode(root, 8)
addNode(root, 9)
addNode(root, 10)
printList(root)
fun = linearReverse(root)
printList(fun)