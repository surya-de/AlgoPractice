from collections import defaultdict

'''
	Create a Graph
'''

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

def printGraph(s):
	print(s.graph)

def bfs(grid, start, end):
	print('start traversal')
	path = []
	traversedNodes = set()   
	traversingNodes = []
	traversingNodes.append(start)
	while traversingNodes:
		currNode = traversingNodes.pop(0)
		print(currNode)
		path.append(currNode)
		for edges in grid.graph[currNode]:
			if edges not in traversedNodes:
				if edges == end:
					path.append(end)
					return path
				traversingNodes.append(edges)
				traversedNodes.add(edges)



if __name__ == '__main__':
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(0, 3)
	g.addEdge(1, 4)
	g.addEdge(4, 5)
	g.addEdge(3, 6)
	g.addEdge(2, 5)
	g.addEdge(5, 6)

	printGraph(g)

	print(bfs(g, 0, 6))