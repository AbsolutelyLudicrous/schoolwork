main = do
	c <- readFile "examplefile.txt"
	putStrLn (show (c))
