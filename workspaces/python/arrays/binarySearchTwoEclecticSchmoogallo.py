#!/usr/bin/python3

"""
	Hoepfully we won't run out of stack frames this time
"""

def binSearch(arr,obj):
	#arr - the array we're searching
	#obj - the item we're searching for
	solved = False
	retValue = 0
	

	while not solved:
		midpoint = int(len(arr)/2)
		if arr[midpoint] is obj:
			solved = True
			retValue = midpoint
		elif arr[midpoint] > obj:
			del arr[:midpoint]
		elif arr[midpoint] < obj:
			del arr[midpoint:]
		else:
			return "Something's fucky"
	
	return retValue

print(binSearch([2,7,9,10],10))
