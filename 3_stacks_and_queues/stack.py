#non-array implementation
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Stack:
	def __init__(self):
		self.top = None

	def push(self, value):
		new_top = Node(value)
		new_top.next = self.top
		self.top = new_top

	def pop(self):
		if self.top:
			popped = Node(self.top.value)
			self.top = self.top.next
			return popped
		return None

	def peek(self):
		return self.top.value

	def __str__(self):
		a = self.top
		listo = ""
		while a:
			listo += str(a.value) + " "
			a = a.next
		return listo

myStack = Stack()
myStack.push(5)
myStack.push(6)
myStack.push(7)
myStack.push(8)
# myStack.printStack()
myStack.pop()
# myStack.printStack()
print myStack