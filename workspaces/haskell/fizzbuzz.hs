fb :: Integer -> String
fb n	| n `mod` 5  == 0 = "Fizz"
	| n `mod` 3  == 0 = "Buzz"
	| otherwise       = show n

main :: IO ()
main = print $ map fb [1..100]
