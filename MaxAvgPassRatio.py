'''
	Greedy and Max heap approach
'''
import heapq

class Solution:
	def maxAverageRatio(self, classes, extraStudents):
		store = []
		for student_pass, student_total in classes:
			gain = ((student_pass / student_total) - ((student_pass + 1) / (student_total + 1)), student_pass, student_total)
			heapq.heappush(store, gain)

		print(store)

		for _ in range(extraStudents):
			_, student_pass, student_total = heapq.heappop(store)
			print(_)
			student_pass += 1
			student_total += 1
			gain = ((student_pass / student_total) - ((student_pass + 1) / (student_total + 1)), student_pass, student_total)
			heapq.heappush(store, gain)
		
		total_gain = sum([student_pass / student_total for _, student_pass,student_total in store]) / len(store)

		return total_gain


if __name__ == '__main__':

	#classes = [[2,4],[3,9],[4,5],[2,10]]
	#extraStudents = 4

	classes = [[1,2],[3,5],[2,2]]
	extraStudents = 2
	s = Solution()
	print(s.maxAverageRatio(classes, extraStudents))