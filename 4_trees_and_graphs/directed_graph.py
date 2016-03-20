def add_vertex(graph, start, end):
	if start != end:
		if graph.has_key(start):
			if end not in graph[start]:
				graph[start] += end
		else:
			graph[start] = [end]

def find_path(graph, start, end, path=[]):
    path += [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: 
            	return newpath
    return None

def find_shortest_path(graph, start, end, path=[]):
    path =+ [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

graph = {}
add_vertex(graph, "A", "B")
add_vertex(graph, "A", "E")
add_vertex(graph, "B", "K")
add_vertex(graph, "B", "C")
add_vertex(graph, "C", "D")
add_vertex(graph, "C", "B")
add_vertex(graph, "C", "E")
add_vertex(graph, "D", "B")
add_vertex(graph, "D", "E")
add_vertex(graph, "D", "A")
add_vertex(graph, "D", "C")
add_vertex(graph, "E", "K")

print graph
print find_path(graph, "E", "K")
