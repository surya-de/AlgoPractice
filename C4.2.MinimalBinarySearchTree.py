# Input is a sorted arroy
# Output needs to be a minimal binary searach tree

class Tree:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def createMinimalBST(arr, start, end):
	if end < start:
		return None

	mid = (start + end) // 2
	node = Tree(arr[mid])

	node.left = createMinimalBST(arr, start, mid - 1)
	node.right = createMinimalBST(arr, mid + 1, end)

	return node

def printTree(node, flag, lvl):
	if node:
		print(node.val, flag, lvl)
		printTree(node.left, 'L', lvl + 1)
		printTree(node.right, 'R', lvl + 1)

if __name__ == '__main__':
	inp = [2, 6, 8, 10, 15, 20, 25]
	bst = createMinimalBST(inp, 0, len(inp) - 1)
	printTree(bst, 'ROOT', 0)