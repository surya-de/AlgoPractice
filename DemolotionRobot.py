from collections import deque
FLAG = False

def distanceTraversed(lot):
	ROWS = len(lot)
	COLS = len(lot[0])


	def getneighbors(coord):
		row, col = coord

		for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
			r = row + dx
			c = col + dy

		if 0 <= r< ROWS and 0 <= c < COLS:
			yield(r, c)

	def bfs(start):
		print('bfs start')
		queue = deque([start])
		r, c = start
		lot[r][c] = 0
		dist = 0

		while len(queue) > 0:
			dist += 1

			n = len(queue)

			for _ in range(n):
				node = queue.popleft()

				for r, c in getneighbors(node):
					if lot[r][c] == 9:
						FLAG = True
						print(dist) 
						return dist

					if lot[r][c] == 0:
						continue

					queue.append((r,c))

					lot[r][c] = 0

	d = bfs((0, 0))
	print(FLAG)

	if FLAG == True:
		return d

	else:
		return -1

if __name__ == '__main__':
	lot = [[1, 0, 0], [1, 0, 0], [1, 9, 1]]
	print(distanceTraversed(lot))