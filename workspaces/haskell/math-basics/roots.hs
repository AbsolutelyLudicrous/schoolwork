{-
	find the roots of a quadratic function using the quadratic formula
-}

roots a b c =
	(( -b + sqrt((b^2)-(4*a*c)))/(2*a),	{- this comma is essential, with out it, we're essentially trying to return two values or something else that ghci doesn't like -}
	 ( -b - sqrt((b^2)-(4*a*c)))/(2*a))
