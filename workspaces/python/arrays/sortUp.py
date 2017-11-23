#!/usr/bin/python3

"""

	Sort an array, upwards

	Yo, this code is super slow. You should probably use an actual sorting method, instead of this barely held togather crap.
	So why did I do things this way?
	
	.88b  d88.    .d88b.    d8888b.   db    db   db         .d8b.    d8888b.   d8888b.   d8888b.    .d88b.     d888b    d8888b.    .d8b.    .88b  d88.   .88b  d88.   d888888b   d8b   db    d888b  
	88'YbdP`88   .8P  Y8.   88  `8D   88    88   88        d8' `8b   88  `8D   88  `8D   88  `8D   .8P  Y8.   88' Y8b   88  `8D   d8' `8b   88'YbdP`88   88'YbdP`88     `88'     888o  88   88' Y8b 
	88  88  88   88    88   88   88   88    88   88        88ooo88   88oobY'   88oodD'   88oobY'   88    88   88        88oobY'   88ooo88   88  88  88   88  88  88      88      88V8o 88   88      
	88  88  88   88    88   88   88   88    88   88        88~~~88   88`8b     88~~~     88`8b     88    88   88  ooo   88`8b     88~~~88   88  88  88   88  88  88      88      88 V8o88   88  ooo 
	88  88  88   `8b  d8'   88  .8D   88b  d88   88booo.   88   88   88 `88.   88        88 `88.   `8b  d8'   88. ~8~   88 `88.   88   88   88  88  88   88  88  88     .88.     88  V888   88. ~8~ 
	YP  YP  YP    `Y88P'    Y8888D'   ~Y8888P'   Y88888P   YP   YP   88   YD   88        88   YD    `Y88P'     Y888P    88   YD   YP   YP   YP  YP  YP   YP  YP  YP   Y888888P   VP   V8P    Y888P  

"""

import sys

def testCases():
	if __name__ is not "__main__":
		print('Testing sort checker:')
		print(isSorted([1,2,3,4,5,6]),	", should return true")	
		print(isSorted([3,8,27,59]),	", should return true")
		print(isSorted([1,2,-30,5,6]),	", should return false")
		#
		print('Testing finding of lowest number above a threshold:')
		print(findLowestAboveMin([1,2,3,4,5],4),	", should return 5")
		print(findLowestAboveMin([1,2,3,4,5],2),	", should return 3")
		print(findLowestAboveMin([1,2,3,4,5],-3),	", should return 1")
		#
		print('Testing indexing of above-theshold numbers:')
		print(findIndexAboveMin([1,2,3,4,5],4),	", should return 4")
		print(findIndexAboveMin([1,2,3,4,5],2),	", should return 2")
		print(findIndexAboveMin([1,2,3,4,5],-3),	", should return 0")
		#
		print('Testing sorting')
		print(sort([9,8,7,6,5]),	"should return 5,6,7,8,9")
		print(sort([5,3,8,6,6,1]),	"should return 1,2,5,6,6,8")
	else:
		print('Why would you try to debug this .py from another file')

def isSorted(arr):
	#tests if an array is sorted in (worst case) O(n) or (best case) O(position of first unsorted element)
	for i in range(1,len(arr)):
		if arr[i] >= arr[i-1]:
			pass
		else:
			return False
	return True

def findLowestAboveMin(arr,smallest):
	#returns the lowest number in an array above a certain threshold
	ret=sys.maxsize
	for i in arr:
		if i < ret and i > smallest:
			ret = i
	return ret

def findIndexAboveMin(arr,smallest):
	#returns the index of the lowest number in an array above a certain threshold
	ret=-1
	for i in range(0,len(arr)):
		if arr[i] < arr[ret] and arr[i] > smallest:
			ret = i
	return ret

def sort(arr):
	#actually sort the array
	#TODO infintititite loop schmoogaloo
	ret=[0]
	for i in range(1,len(arr)+1):
		ret.append(findLowestAboveMin(arr,(arr[i-1])))
	if not isSorted(arr):
		sort(arr)
	ret=ret[1:]
	return ret

testCases()
