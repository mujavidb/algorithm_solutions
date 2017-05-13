class Graph:
	def __init__(self, graph = {}):
		self.graph = graph

	def vertices(self):
		return self.graph.keys()

	def add(self, start, end):
		if start != end:
			if self.graph.has_key(start):
				if end not in self.graph[start]:
					self.graph[start] += end
					self.add(end, start)
			else:
				self.graph[start] = [end]
				self.add(end, start)

	def find_path(self, start, end, path=[]):
	    path += [start]
	    if start == end:
	        return path
	    if not self.graph.has_key(start):
	        return None
	    for node in self.graph[start]:
	        if node not in path:
	            newpath = self.find_path(node, end, path)
	            if newpath:
	            	return newpath
	    return None

a = {
	"a" : ["c"],
	"b" : ["c", "e"],
	"c" : ["a", "b", "d", "e"],
	"d" : ["c"],
	"e" : ["c", "b"]
}

g = Graph(a)

g.add("a", "b")
g.add("b", "s")
g.add("a", "s")

print g.graph
print g.find_path('d','e')
