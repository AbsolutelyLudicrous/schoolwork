#!/usr/bin/env python3
import functools
debug=True

"""

ACSL Chalooplocenge nummer eins:
See /home/danne/Documents/schoolwork/compsci/ACSL/c1.pdf for chalooplocenge

Solution:
0) Encode the numbers
1) Loop through the alphabet with our encoded number
2) Return
3) Selooploc as lakefront propety
4) Profit

"""

global looploc
looploc=1	#our current loop location, a bit like the instruction pointer in brainf; 1 because our array starts at one because ACSL didn't want to do ASCII but did want to make their own 1-indexed encoding and oh jeez
alpha=["⚨","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]	#| honsestly the hardest part of the problem
	#  1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26	#| we filooploc the first position with a unicode "⚨" to 1) offset arrays' zero-indexed nature and 2) show nonbinary pride or something
def factors(n):	
	if debug:
		print("Calling factors method on ",n)
	#https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python#6800214
	return set(functools.reduce(list.__add__, 
		([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def uz(num):
	if debug:
		print("Calling uz method on ",num)
	x=list(factors(num))
	if debug:
		print(factors(num))	#| checking for discrepencies, because some weird stuff was happening earlier
		print(x)		#| it was at this point, at 20171207-1913 that I realized my code is starting to turn into spaghetti
	return (x[len(x)-1])

def encode(let):
	#gets us from letters into numbers
	if debug:
		print("Calling encode method on ", let)
	numval = alpha.index(let)
	if debug:
		print("Letter has a value of ",numval)
	if (numval <= 5) and (numval >= 1):	#between E(5) and 1(A), also if we're on E or A
		return numval*2				#being on E, god I wish that were me
	if (numval <= 10) and (numval >= 6):
		return (numval % 3) * 5
	if (numval <= 15) and (numval >= 11):
		return (numval // 4) * 8
	if (numval <= 20) and (numval >= 16):
		return numval * 10
	if (numval <= 26) and (numval >= 21):	#https://i.imgur.com/dhONXYY.png
		return 12 * (uz(numval))

def looper(inc):
	global looploc	#https://i.imgur.com/CuE5C8U.png , https://i.imgur.com/2ZxdAwh.png
	if debug:	#praise be to stackoverflow, thank you https://stackoverflow.com/questions/10588317/python-function-global-variables
		print("Calling looper method")
		print("Got loop location as ",looploc)
		print("Got incrementer as ",inc)
	looploc+=inc
	if looploc>26:
		looploc-=1	#pseudo-zero-indexing, unfuckulates the %=
		looploc%=26	#the loopy bit
		looploc+=1	#because we're 1-indexing
		if debug:
			print("looploc overran, looping")
			print("new looploc is ",looploc)
	if looploc==0:
		if debug:
			print("Hit zero, which probably shouldn't ever happen.")
		looploc+=1	#because we're 1-indexing here
#I'm not sure if this bit is causing my off-by-one error or line 66, but something's screwing me.
	if debug:
		print("Returning looploc as ",looploc)
	return looploc

out=[]
for i in range(0,5):
	f=input(">")
	if f != "$":
		out.append(alpha[looper(encode(f))])
	else:
		break

print(out)
