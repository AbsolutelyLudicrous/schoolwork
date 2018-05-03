First of all, thanks a billion for taking the time to help me here.

Primarily, I don't feel like my explanation of functional vs. non-functional (imperative) programming was good enough.
Functional programming is definining a main function in terms of series of smaller functions, whereas imperative programming is more akin to a series of instructions.

---

An example of each, in which we (pretend to) bake a cake, might look like this:

Functional:
```
	makeCake (flour, eggs, icing) =
		bake(flour, eggs) + icing
```

Imperative:
```
	function makeCake(flour, eggs, icing):
		cake = None
		cake = cake + bake(flour, eggs)
		cake = cake + icing
		return cake
```

Or a more mathematical example, the Fibonacci sequence:

Functional:
```
	fib (1) = 1
	fib (2) = 1
	fib (n) = fib(n-1) + fib(n-2)
```

Imperative:
```
	function fib(n):
		if n is 1:
			return 1
		else if n is 2:
			return 1
		else:
			return (fib(n-1) + fib(n-2))
```

---

The arguments for and against functional programming boil down to the fact that functional programs have no side effects, they can not manipulate data and instead only define data in terms of other data.
Some people think that this behaviour is beautiful and leads to better code, some people think that, because the whole purpose of computing is to do things (produce side effects), functional programming unnecesarily complicates things.

---

From what I'm gathering of monads, they're a way of getting side effects in functional languages; or of performing operations in series, the way an imperative language would do things.
Probably both, given that imperative languages inherently have side effects.
