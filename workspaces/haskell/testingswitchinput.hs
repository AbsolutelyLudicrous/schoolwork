{-
	Interactively test switch input in GHCI
-}

switch inp =
	case inp of
		(-1) -> "Negative one"
		0 -> "Zero"
		1 -> "One"
		_ -> "Neither negative-one, zero, nor one."
