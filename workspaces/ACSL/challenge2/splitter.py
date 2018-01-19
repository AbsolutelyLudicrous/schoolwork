#!/usr/bin/env python3

"""

	Parses and splits the expression.
	Meant to be imported as a module.

"""

debug=True

def detectCompleted(fullex):
	return "[]" if ("[" in fullex and "]" in fullex) else "()"

def detectInternExtern(fullex):
	#method to detect if we have an external or an engulfed expression
	#returns the type of expression, intern or extern, and the completed subexpression
	parsefor = detectCompleted(fullex)
	if debug:print("Detected completed grouper: ", parsefor)
	compsubexp = fullex[fullex.index(parsefor[0]):fullex.index(parsefor[1])+1]	#string representing the completed subexpression
	if debug:print("Completed subexp detected as: ",compsubexp)
	return [
		("extern" if not ("[" in compsubexp and "]" in compsubexp) else "intern"),
		compsubexp]

if __name__=="__main__":
	#test cases
	exes=[
		"[2 + 3 * 8 - 3 ) ] + 6",
		"[ ( 2 - 5 ) + 6",
		"[ ( 5 + 5 - 2 ] * 5"]
	print("Test cases: ",exes)
	print("Testing completion filterer")
	for x in exes:print(detectCompleted(x))
	print("Testing internal/external detecter")
	for x in exes:print(detectInternExtern(x))
