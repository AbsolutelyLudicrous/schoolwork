#!/usr/bin/python3

"""
	
d88888b db    db  .o88b. db   dD
88'     88    88 d8P  Y8 88 ,8P'
88ooo   88    88 8P      88,8P  
88~~~   88    88 8b      88`8b  
88      88b  d88 Y8b  d8 88 `88.
YP      ~Y8888P'  `Y88P' YP   YD

	I was recursing wrong
	Actually I was doing most things wrong
	And I stole most of this code from [this site](https://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html)

	Binarily search an array

	Why do only have *binary* searches?
	Why not nonbinary searches?
	Down with the gender binary, is all i'm saying.

"""

def binSearch(arr,obj):
	if len(arr) == 0:	#if the array is empty
		return -1
	else:
		mid = len(arr)//2	#// is the python floordiv operator
		if arr[mid] == obj:
			print(arr,mid)
			return mid
		elif obj < arr[mid]:
			print(arr,mid)
			return binSearch(arr[:mid],obj)
		elif obj > arr[mid]:
			print(arr,mid)
			return binSearch(arr[mid+1:],obj)	#that +1 is needed to prevent off-by-one errors
		else:
			#should never happen
			print("What the fuck?")

#test cases, please ignore
if __name__ == "__main__":
	print(binSearch([0,1,2,3,4,5,6],2))
	print(binSearch([10,11,12,13,14,18],11))
	print(binSearch([0,33,678,1659,63946],4))

