{-|
	determines if a number is signifigant
	meant to be run with ghci, or any interactive repl

	yeah, prelude has the same function, but i need the haskelling practice
-}

issignum x = 
	if x < 0 
		then -1
		else if x > 0 
			then 1
			else 0
