#!/usr/bin/env python3

"""

	Compliment to the encoder
	Performs the looping steps

"""

debug=True
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"	#| I forgot that Python allows indexing on strings in the last one
					#| We don't have to 1-index this time
looploc=0	#1-indexing was fucking us
def loop(inc):
	global looploc	#https://i.imgur.com/CuE5C8U.png , https://i.imgur.com/2ZxdAwh.png
	if debug:	#praise be to stackoverflow, thank you https://stackoverflow.com/questions/10588317/python-function-global-variables
		print("Calling looper method")
		print("Got loop location as ",looploc)
		print("Got incrementer as ",inc)
	looploc+=inc
	if debug:
		print("looploc after incrementation is ",looploc)
	if looploc>=26:
		looploc%=26
		if debug:
			print("looploc overran, looping")
			print("new looploc is ",looploc)
	if debug:
		print("Returning looploc as ",looploc)
	return looploc
