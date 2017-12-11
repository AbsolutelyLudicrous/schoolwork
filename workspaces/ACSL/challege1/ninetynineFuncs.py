#!/usr/bin/env python3

"""

	The ACSL2017 challenge 1.
	(Why doesn't ACSL 0-index their challenges?)

	Invoked from the command line, e.g. "./99.py 75 7 3 8 8 7 T 5 9 A 6" or "./99.py 80 9 T 7 8 K A 3 5 Q T"

	This design decision was on purpose, it means it'll be easier to test the script.
	Run ./test on any POSIX system for the test cases

	This file contains the functions associated with the main 99 program.

"""

from sys import argv

global total	#total point count
global player	#player's ordered card stack
global dealer	#dealer's ordered card stack
debug=True

def parse(args):
	passback=(()()())	#empty list of lists that we're going to be returning
	passback[1]=args[1];del args[1]	#pops the initial total off of the arguments and pushes it to the return LoL.
	passback[2]=args[:(len(args)/2)]	#| the former half of the args list is added to passback
	passback[3]=args[(len(args)/2):]	#| similar, except with former half
	if debug:				#| I actually am kinda proud of this solution, it allows for any odd number of inputs to work
		print("Returning LoL formatted args as", passback)
	return passback

def cards(car):
	"""
		function for converting card face values into real integer values
	"""
	global total	#slightly unsafe, but we need it for when Ace is input
	if car is 2 or car is 3 or car is 4 or car is 5 or car is 6 or car is 7 or car is 8:
		return car
	if car is 9:	#nine
		pass	#god I wish that were me
	if car is "T":	#ten
		return -10
	if car is "J":	#jack
		return 11
	if car is "Q":	#queen
		return 12
	if car is "K":	#king
		return 13
	if car is "A":					#| ace
		if ((total+14) > 99) and (total < 99):	#| hey, same!
			return 1
		if ((total+14) < 99) or (total > 99):
			return 14
		# you may notice an edge case here
		# "What happens if the point total is 99 and we play an Ace?"
		# That's intentional.
		# It's undefined in the spec, so I've left it undefined here.
	if debug:
		print("Reached end of cards function with returning a value, panic!")
