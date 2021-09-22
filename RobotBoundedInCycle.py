class Solution:
	def isRobotBounded(self, instructions: str):
		dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
		start = 0
		x = y = 0

		for inst in instructions:
			if inst == 'L':
				start = (start + 3) % 4

			elif  inst == 'R':
				start = (start + 1) % 4

			else:
				x += dir[start][0]
				y += dir[start][1]

		if ((x == 0 and y == 0) or (start != 0)):
			return True


if __name__ == '__main__':
	s = Solution()
	instr = 'GGLLGG'
	print(s.isRobotBounded(instr))