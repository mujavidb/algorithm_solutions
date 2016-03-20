#3.3
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Stack:
	def __init__(self):
		self.top = None
		self.length = 0

	def push(self, value):
		new_top = Node(value)
		new_top.next = self.top
		self.top = new_top
		self.length +=1

	def pop(self):
		if self.top:
			popped = Node(self.top.value)
			self.top = self.top.next
			self.length -=1
			return popped
		return None

	def printStack(self):
		a = self.top
		listo = []
		while a:
			listo.append(a.value)
			a = a.next
		print listo

class SetofStacks():
	def __init__(self, maxLength):
		self.max = maxLength
		self.top = None
		self.stacks = []

	def push(self, value):
		if not self.stacks:
			a = Stack()
			self.stacks.append(a)
		if self.stacks[-1].length == self.max:
			new = Stack()
			self.stacks.append(new)
		self.stacks[-1].push(value)
		self.top = value

	def pop(self):
		value = self.stacks[-1].pop()
		if not value:
			self.stacks.pop()
			value = self.stacks[-1].pop()
		self.top = self.stacks[-1].top
		return value

	def printSoS(self):
		for stack in self.stacks:
			stack.printStack()

sos = SetofStacks(4)
sos.push(5)
sos.push(7)
sos.push(5)
sos.push(5)
sos.push(5)
sos.push(5)
sos.push(5)
sos.push(5)
sos.push(5)
sos.push(5)
sos.push(5)
sos.push(5)
sos.pop()
sos.pop()
sos.pop()
sos.pop()
sos.pop()
sos.pop()
sos.pop()
sos.printSoS()