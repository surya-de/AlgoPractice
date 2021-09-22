class Solution:
	def slowestKey(self, releaseTimes, keysPressed):
		dur = releaseTimes[0]
		finalKey = keysPressed[0]

		for i in range(1, len(releaseTimes)):
			key = keysPressed[i]
			localDur = releaseTimes[i] - releaseTimes[i - 1]
			
			if localDur > dur:
				finalKey = key
				dur = localDur

			if localDur == dur:
				if ord(key) >= ord(finalKey):
					finalKey = key
					dur = localDur

		return finalKey

if __name__ == '__main__':
	#releaseTimes = [12,23,36,46,62]
	#keysPressed = "spuda"
	releaseTimes = [12,23,36,46,62,78,100]
	keysPressed = 'spudaea'

	s = Solution()
	print(s.slowestKey(releaseTimes, keysPressed))