'''
The idea is to maintain an array of size 60, where array[i] represents number of songs of length x such that x % 60 = i (Note, we could use a hashmap but since we have a finite range, using an array would be quicker). Let's call this array modTimes.

Then there are three cases:

modTimes[0] - Number of songs whose length is exactly divisble by 60(length%60 = 0)
modTimes[30] - Number of songs whose length%60 = 30
others - modTimes[1] through modTimes[29] (Note modTimes[59] through modTimes[31] are just complementary pairs of modTimes[1] through modTimes[29])
Let's deal with cases 1 and 2 first.
Number of valid pairs for modTimes[0] and modTimes[30] is simply calculated using n*(n-1)/2
(The way we got to this - you're required to find number of pairs you can form given number of entries, ie nC2 where n is number of entries,
and nC2 eventually boils down to nC2 = n!/(2! * (n-2)!) which further simplifies to n*(n-1)/2)

Next for case 3, the number of pairs would be the product of complementary entries in modTimes, ie modTimes[i] * modTimes[60-i].
(Think of it this way, if you have n balls and m books, how many combinations of balls and books can you generate? - n times m)
'''

from collections import defaultdict

class Solution:
	def pairs(self, n):
		return n * (n - 1) / 2
	

	def numPairsDivisibleBy60(self, time):
		store = defaultdict(int)
		ret = 0

		for t in time:
			store[t % 60] += 1


		ret += self.pairs(store[0])
		ret += self.pairs(store[30])

		for i in range(1, 30):
			ret += store[i] * store[60 - i]

		print(store)

		return ret


if __name__ == '__main__':
	s = Solution()
	time = [30,20,150,100,40]
	print(s.numPairsDivisibleBy60(time))