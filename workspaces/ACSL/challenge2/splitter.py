#!/usr/bin/env python3

"""

	Parses and splits the expression.
	Meant to be imported as a module.

"""

debug=True

def filterCompletes(fullex):
	#method to filter out any complete expressions, subexpressions which cannot be modified.
	parsefor = "[]" if ("[" in fullex and "]" in fullex) else "()"
	if debug:
		print("Detected completed grouper: ", parsefor)
	return None

def detectInternExtern(fullex):
	#method to detect if we have an external or an engulfed expression
	parsefor = "[]" if ("[" in fullex and "]" in fullex) else "()"
	if debug:print("Detected completed grouper: ", parsefor)
	compsubexp = fullex[fullex.index(parsefor[0]):fullex.index(parsefor[1])+1]	#string representing the completed subexpression
	if debug:print("Completed subexp detected as: ",compsubexp)
	return None

if __name__=="__main__":
	#test cases
	exes=[
		"[2 + 3 * 8 - 3 ) ] + 6",
		"[ ( 2 - 5 ) + 6",
		"[ ( 5 + 5 - 2 ] * 5"]
	print("Test cases: ",exes)
	print("Testing completion filterer")
	for x in exes:print(filterCompletes(x))
	print("Testing internal/external detecter")
	for x in exes:print(detectInternExtern(x))
