def friend_circles(relationships):
	visited = set()

	def dfs(node):
		for neighbor, connected in enumerate(relationships[node]):
			print((neighbor, connected))
			if connected and neighbor not in visited:
				visited.add(neighbor)
				print(visited)
				dfs(neighbor)

	ans = 0
	for i in range(len(relationships)):
		print('external node- ', i)
		if i not in visited:
			dfs(i)
			ans += 1

	return ans

if __name__ == '__main__':
	relationships = [[int(x) for x in input().split()] for _ in range(int(input()))]
	
	print(friend_circles(relationships))