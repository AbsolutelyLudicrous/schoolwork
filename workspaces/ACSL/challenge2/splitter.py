#!/usr/bin/env python3

"""

	Parses and splits the expression.
	Meant to be imported as a module.

"""

debug=True

def filterCompletes(fullex):
	#method to filter out any complete expressions, subexpressions which cannot be modified.
	parsefor = "\[*\]" if ("[" in fullex and "]" in fullex) else "\(*\)"
	if debug:
		print("Detected completed grouper: ", parsefor)

if __name__=="__main__":
	#test cases
	exes=[
		"[2 + 3 * 8 - 3 ) ] + 6",
		"[ ( 2 - 5 ) + 6",
		"[ ( 5 + 5 - 2 ] * 5"]
	print("Test cases: ",exes)
	for x in exes:print(filterCompletes(x))
