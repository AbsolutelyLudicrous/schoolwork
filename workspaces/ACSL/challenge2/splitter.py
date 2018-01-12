#!/usr/bin/env python3

debug=True

def filterCompletes(fullex):
	brack=bool((fullex.indexOf("[") != -1) && (fullex.indexOf("]") != -1))	#true if there are both opening and closing brackets
	paren=bool((fullex.indexOf("(") != -1) && (fullex.indexOf(")") != -1))	#true if there are both opening and closing parens
