#p92
class Node:
    def __init__(self, value = 0):
        self.value = value
        self.right = None
        self.left = None

def bst_add(root, value):
    if root is not None:
        if root.value > value:
            if root.left is None:
                root.left = Node(value)
            else:
                bst_add(root.left, value)
    	elif root.value < value:
            if root.right is None:
                root.right = Node(value)
            else:
                bst_add(root.right, value)

def bst_loop_add(root, value):
    current = root
    while current is not None:
        if current.value > value:
            if current.left is None:
                current.left = Node(value)
                return
            else:
                current = current.left
        elif current.value < value:
            if current.right is None:
                current.right = Node(value)
                return
            else:
                current = current.right

def bfs_print(root):
    queue = [root]
    nodes = []
    while queue:
        current = queue.pop(0)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        nodes.append(current.value)
    print " ".join([str(x) for x in nodes])

def bfs_print_levels(root):
    level = [root]
    while level:
        nextlevel = []
        for node in level:
            print node.value,
            if node.left:
                nextlevel.append(node.left)
            if node.right: 
                nextlevel.append(node.right)
        print
        level = nextlevel

def average_levels(root):
    level = [root]
    while level:
        nextlevel = []
        for node in level:
            if node.left:
                nextlevel.append(node.left)
            if node.right: 
                nextlevel.append(node.right)
        values = [ float(x.value) for x in level]
        print sum(values) / len(values)
        level = nextlevel

def io_print(root):
    if not root:
        return
    io_print(root.left)
    print str(root.value) + " ",
    io_print(root.right)   

def io_print_stack(node):
    stack = []
    while stack or node != None:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print str(node.value) + " ",
            node = node.right

def pre_print(root):
    if not root:
        return
    print str(root.value) + " ",
    io_print(root.left)
    io_print(root.right)   

def post_print(root):
    if not root:
        return
    io_print(root.left)
    io_print(root.right)    
    print str(root.value) + " ",

def height(node):
    if node is None:
        return -1
    else:
        return max(height(node.left), height(node.right)) + 1

#doesn't work but logic checks out
def balanced(node):
	return (node is None) or \
			(balanced(node.left) and \
			balanced(node.right) and \
			abs(height(node.left) - height(node.right)) <= 1)

def bstify(array, node):
	if not array:
		return
	mid = len(array)/2
	bst = Node(array.pop(mid))
	bstify(array[:mid], bst.left)
	bstify(array[mid:], bst.right)

a = Node(10)
bst_add(a, 15)
bst_add(a, 3)
bst_add(a, 13)
bst_add(a, 12)
bst_add(a, 8)
bst_add(a, 4)

# bfs_print(a)
# bfs_print_levels(a)
average_levels(a)
# new = bstify([1,2,3,4,5,6,7,8,9,10], Node())
# io_print(new)
# print
# print height(new)







