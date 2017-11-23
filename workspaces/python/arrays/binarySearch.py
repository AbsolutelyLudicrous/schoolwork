#!/usr/bin/python3
"""
	Binarily search an array

	Why do only have *binary* searches?
	Why not nonbinary searches?
	Down with the gender binary, is all i'm saying.
"""

def binSearch(arr,obj):
	mid = int((len(arr))/2)
	if arr[mid] is obj:
		print(arr,mid)
		return arr[mid]
	elif arr[mid] < obj:
		print(arr,mid)
		arr = arr[0:mid]
		return binSearch(arr,obj)
	elif arr[mid] > obj:
		print(arr,mid)
		arr = arr[mid:]
		return binSearch(arr,obj)
	else:
		print("What the fuck?")

print(binSearch([0,1,2,3,4,5,6],2))
print(binSearch([10,11,12,13,14,18],11))

