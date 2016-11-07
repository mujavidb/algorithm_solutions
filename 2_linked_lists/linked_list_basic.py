class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList():
	def __init__(self):
		self.first = None
		self.size = 0

	def insert(self, value):
		if not self.first:
			self.first = Node(value)
		else:
			a = self.first
			while a.next:
				a = a.next
			a.next = Node(value)
		self.size += 1

	def insertMulti(self, multi):
		for x in multi:
			self.insert(x)

	def printList(self):
		a = self.first
		while a:
			print a.value
			a = a.next
		print
	
	def removeDups(self): #2.1
		a = self.first
		while a:
			b = a
			val = a.value
			while b.next:
				if b.next.value == val:
					if b.next.next:
						b.next = b.next.next
					else:
						b.next = None
				else:
					b = b.next
			a = a.next
	
	def deleteVal(self, value):
		if self.first.value == value:
			self.first = self.first.next
		else:
			a = self.first
			while a.next and a.next.value != value:
				a = a.next
			if a.next.next:
				a.next = a.next.next
			else:
				a.next = None

	def rebuildAround(self, pivot): #2.4
		a = self.first
		less = []
		more = []
		while a:
			less.append(a.value) if a.value < pivot else more.append(a.value)
			a = a.next

		rebuild = LinkedList()
		rebuild.insertMulti(less)
		rebuild.insert(pivot)
		rebuild.insertMulti(more)

		self.first = rebuild.first

	def isPalindrome(self):
		values = []
		a = self.first
		while a:
			values.append(a.value)
			a = a.next
		for i in range(len(values)/2):
			if values[i] != values[-1 * (i + 1)]: 
				return False
		return True

sll = LinkedList()
sll.insertMulti([8,7,8])
sll.printList()
# sll.removeDups()
# sll.printList()
# # sll.rebuildAround(7)
# sll.printList()
# print sll.isPalindrome()
