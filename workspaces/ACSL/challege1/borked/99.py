#!/usr/bin/env python3

debug=True

def turn():
	"""
		This method handles each individual "turn" in ACSL99
		This will be called until the total is over 100
	"""
	global stack
	global total
	global first
	global secon
	#OH YEAH, FUCK FUNCTIONAL PROGRAMMING; IT IS TIME TO DIRECTLY MANIPULATE SOME VALUES
	current = []	#the current player/dealer's card stack we're operating on
	if debug:
		print("Current card stack is: ",stack)
		print("Current total score is: ",total)
		print("Current \"active\" card stack is: ",first)
		print("Current \"on-deck\" card stack is: ",secon)
	for car in first:
		#this hideous if-ladder gets all our character cards into number values
		if car is 2 or car is 3 or car is 4 or car is 5 or car is 6 or car is 7 or car is 8:
			current.append(car)
		if car is 9:	#nine
			current.append(0)
		if car is "T":	#ten
			current.append(10)
		if car is "J":	#jack
			current.append(11)
		if car is "Q":	#queen
			current.append(12)
		if car is "K":	#king
			current.append(13)
		if car is "A":					#| ace
			if ((total+14) > 99) and (total < 99):	#| hey, same!
				current.append(1)
			if ((total+14) < 99) or (total > 99):
				current.append(14)
			# you may notice an edge case here
			# "What happens if the point total is 99 and we play an Ace?"
			# That's intentional.
			# It's undefined in the spec, so I've left it undefined here.
	if (((sorted(first)[len(first)-1])) is not 10):
		total+=((sorted(first)[len(first)-1]))
	if (((sorted(first)[len(first)-1])) is 10):
		total-=10
	
	first,secon =secon,first	#swaps the player and delaer's cards; if we don't do this I have to add a condition to detect who's list we're operating on

stack=input(">")	#full input, as described in spec
stack=stack.split(" ")
total=stack.pop(0)	#our initial total
if debug:
	print("Getting initial total as ",total)
first=stack[0:3];del stack[0:3]	#player's cards
secon=stack[0:3];del stack[0:3]	#delaer's cards
#after popping the dealer's and player's cards off the stack, the remaining stack is just the face-down cards in the middle
# I say "pop", pop doesn't work over ranges, so we have to just copy and delte it ourself
if debug:
	print("Got player's stack as ",first)
	print("Got dealer's stack as ",secon)
	print("Remaining stack is ",stack)
	print("Current card total is ",total)

if debug:
	print("Finished input reception;")
	print("Now moving on to turn-cycling phase.")

isCurrentlyPlayer=True	#is the active card stack the player's?
while int(total) < 100:
	turn()
	isCurrentlyPlayer = not isCurrentlyPlayer	#"flip" who's playing

if isCurrentlyPlayer:
	print(total,"player")
else:
	print(total,"dealer")
