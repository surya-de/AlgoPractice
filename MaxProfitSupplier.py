import heapq
from typing import List

def find_profit(inventory: List[int], order: int) -> int:
	store = [-stocks for stocks in inventory]
	heapq.heapify(store)
	profit = 0

	for _ in range(order):
		item = -heapq.heappop(store)
		profit += item
		item -= 1
		heapq.heappush(store, -item)
	
	return profit

if __name__ == '__main__':
	inventory = [10, 10]
	order = 5
	print(find_profit(inventory, order))