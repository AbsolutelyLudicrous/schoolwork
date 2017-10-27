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
	for i in range(1,len(bo)):
		for j in range(0,len(bo[0])):
			if bo[i][j] == bo[i-1][j]:
				return True
			if bo[j][i] == bo[j-1][i]:
				return True

			
testcases()
