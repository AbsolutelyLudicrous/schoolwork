#There are 30 candies; half yummies, half gooeys.
#Half must be discarded
#Candies are arranged in a circle
#The candies are discarded such that every 13th candy is removed
#Problem: Keep all your Yummies, remove all your Gooeys.

#Solution:
#	Pop "removed" candies off one array and onto another.

arr=list(range(0,30))	#our array of candies, filled
removed=list({})

i=12
while len(arr) > 15:
	#print(arr)	#debugging
	if(i>len(arr)):
		#i%=len(arr)	#when we loop around in the array
		i-=len(arr)
	removed.append(arr[i])
	del arr[i]
	i+=12	#not 13 because we've already moved forward a space by deleting the index

print(arr)
print(removed)
