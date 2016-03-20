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