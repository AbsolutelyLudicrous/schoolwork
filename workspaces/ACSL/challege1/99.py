#!/usr/bin/env python3

debug=True

stack=input(">")	#full input, as described in spec
total=stack.pop(0)	#our initial total
if debug:
	print("Getting initial total as ",total)
player=stack.pop(range(0-2))	#player's cards
dealer=stack.pop(range(0-2))	#delaer's cards
#after popping the dealer's and player's cards off the stack, the remaining stack is just the face-down cards in the middle
if debug:
	print("Got player's stack as ",player)
	print("Got dealer's stack as ",dealer)
	print("Remaining stack is ",stack)
