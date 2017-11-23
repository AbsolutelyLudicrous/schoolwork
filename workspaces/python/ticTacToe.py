#!/usr/bin/python2

import numpy

board=numpy.zeros((3,3))	#gives us a 3x3 board of zeroes

def testcases():
	if __name__ == '__main__':
		grid=[	[0,0,0],
			[1,1,1],
			[1,2,1]	]
		displayBoard(grid)
		print(checkVictory(grid))

		grid=[	[1,0,0],
			[2,1,1],
			[1,2,1]	]
		displayBoard(grid)
		print(checkVictory(grid))

		grid=[	[0,2,0],
			[2,1,1],
			[1,2,1]	]
		displayBoard(grid)
		print(checkVictory(grid))

def displayBoard(bo):
	print(bo[0])
	print(bo[1])
	print(bo[2])

def checkVictory(bo):
	for i in range(1,len(bo)):#cycle through the horizontally bits of bo
		if sum(bo[i]) == len(bo[i]) or sum(bo[i]) == 2*len(bo[i]):#on the horizontal, return true if every bit is set to the same value
			return True
		for j in range(0,len(bo[0])):#cycle through the vertically bits of bo
			if sum(bo[i][j]) == len(bo[i][j]) or sum(bo[i][j]) == 2*len(bo[i][j]):
				return True
	return False

			
testcases()
