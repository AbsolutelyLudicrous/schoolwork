#!/usr/bin/env python3

"""

	Ah fuck, quick-and-dirty solution time.

	Rationale:
		Iterate through the inputted full expression forwards and insert a brack/paren at every valid location.
		Loop backwards through the list and do the same again.
		set() the output to remove duplicates.

"""

debug=True

fullex=input(" > ")	# the full expression to be parsed

validexp=[]	# list of valid expressions

for currchar in range(0,len(fullex),1):	# we hjave to use C-style loops because some expressions will contain multiple of the same cahracter, so we can't just do a for-each and a .index()
	if debug:print("Current chracter being evaluated: ",fullex[currchar])
	if fullex[currchar] is "(":
		if debug:print("Current character is an opening paren, searching for closing paren")
		for posafterparen in range(currchar,fullex.index(")"),1):
			foo=list(fullex).insert(currchar,"]")
			if debug:print(foo)
			validexp.append(list(fullex).insert(currchar,"]"))

print(validexp)
