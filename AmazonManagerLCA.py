from typing import Tuple

class Node:
	def __init__(self, val, children = None):
		if children is None:
			children = []

		self.val = val
		self.children = children


def subtree_max_avg(root: Node):
	#res = (float('-inf'), None)
	global_avg = float('-inf')
	final_node = None

	def dfs(node: Node) -> Tuple[int, int]:
		nonlocal global_avg, final_node
		child_sum , child_count = 0, 0
		total_sum, total_count = 0, 0

		for child in node.children:
			if child is None:
				return (0, 0)
			child_sum, child_count = dfs(child)
			
			child_sum = child.val + child_sum
			child_count = 1 + child_count
			
			total_sum += child_sum
			total_count += child_count
			
			local_avg = total_sum / total_count

			if local_avg > global_avg:
				global_avg = local_avg
				final_node = child

		return  child_sum, child_count

		#rec = [dfs(c) for c in node.children if c]
		#s = node.val + sum(t[0] for t in rec)
		#n = 1 + sum(t[1] for t in rec)
		#res = max(res, (s / n, node))
		#return s, n

	dfs(root)

	return final_node.val

def print_tree(node):
	if not node:
		return None

	print('Node- ', node.val)

	for child in node.children:
		print(child.val)

	for child in node.children:
		print_tree(child)
		

def build_tree(nodes, f):
	val = next(nodes)
	num = int(next(nodes))
	children = [build_tree(nodes, f) for _ in range(num)]
	return Node(f(val), children)


if __name__ == '__main__':
	root = build_tree(iter(input().split()), int)
	print_tree(root)
	#res = subtree_max_avg(root)
	#print (res)