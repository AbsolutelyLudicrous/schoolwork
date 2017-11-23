# What the hell am I learning?

---

## Tuples

+ Tuples are just arrays which you can cram anything, even other tuples, into.

+ Tuples can have multiple data types.

+ Tuples are defined with parens, e.g.: `("a","b","c",5,80975,1.324,("this", "is", "a", "tuple", "inside", "a", "tuple"))`

---

## Lists

+ Lists exist, they are defined with brackets, e.g.: `[1,2,3]`

+ The empty list is just `[]`

+ When building lists, use the cons operator, `:` because it makes you look cool. 

+ The cons operator tacks values on to the front of a list.

	GHCi, version 8.0.1: http://www.haskell.org/ghc/  :? for help
	Prelude> [1,4,8,2,3,3457]
	[1,4,8,2,3,3457]
	Prelude> 5:4:3:2:1:[]
	[5,4,3,2,1]
	Prelude> 
