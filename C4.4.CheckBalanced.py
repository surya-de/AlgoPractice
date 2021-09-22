# Tree is balanced if the height of two aubtree at any node never differs by more than 1.

class Tree:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def createTree(arr, start, end):
	if end < start:
		return None

	mid = (start + end) // 2
	node = Tree(arr[mid])
	node.left = createTree(arr, start, mid - 1)
	node.right = createTree(arr, mid + 1, end)

	return node

def printTree(node, flag, lvl):
	if node:
		print(node.val, flag, lvl)
		printTree(node.left, 'L', lvl + 1)
		printTree(node.right, 'R', lvl + 1)

if __name__ == '__main__':
	arr1 = [2, 6, 8, 10, 15, 20, 25]
	bst1 = createTree(arr1, 0, len(arr1) - 1)
	printTree(bst1, 'ROOT', 0)

	print('---------------------------------')

	arr2 = [2, 6, 8, 10, 15, 20, 25, None, 35]
	bst2 = createTree(arr2, 0, len(arr2) - 1)
