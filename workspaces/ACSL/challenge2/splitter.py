#!/usr/bin/env python3

"""

	Parses and splits the expression.
	Meant to be imported as a module.

"""

debug=True

if __name__="__main__":
	#test cases
	exes=[
	"[2 + 3 * 8 - 3 ) ] + 6",
	"[ ( 2 - 5 ) + 6",
	"[ ( 5 + 5 - 2 ] * 5"]

def filterCompletes(fullex):
	#method to filter out any complete expressions, subexpressions which cannot be modified.
	parsefor = "\[*\]"				#regex for anything inside two brackets
		if ("[" in fullex and "]" in fullex)	#...if we have completed brackets
		else "\(*\)"				#or if we don't
	if debug:
		print("We are parsing the full expression for ", parsefor)
