# Take greedy approach 
# Sort the list based on per unit

class Solution:
	def maximumUnits(self, boxTypes, truckSize):
		boxTypes = sorted(boxTypes, key = lambda x : x[1], reverse = True)
		maxUnit = 0

		for boxes in boxTypes:
			temp = min(boxes[0], truckSize)
			truckSize -= temp
			maxUnit += temp * boxes[1]

			if truckSize == 0:
				break

		return maxUnit



if __name__ == '__main__':
	boxTypes = [[1, 3], [2, 2], [3, 4]] 
	truckSize = 4

	s = Solution()
	print(s.maximumUnits(boxTypes, truckSize))