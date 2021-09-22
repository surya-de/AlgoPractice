'''
	In questions like rotate array, try to find a cycle pattern.
'''

def rotate(nums, k):
	L = len(nums)
	for i in range(0, len(nums)):
		idx = (i + k) % L
		temp = nums[idx]
		nums[idx] = nums[i]


if __name__ == '__main__':
	inp = [1,2,3,4,5,6,7]
	k = 3
	rotate(inp, k)