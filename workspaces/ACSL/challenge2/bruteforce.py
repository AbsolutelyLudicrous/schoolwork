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

