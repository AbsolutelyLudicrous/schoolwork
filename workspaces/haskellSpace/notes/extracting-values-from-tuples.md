Use a combination of fst and snd to extract the character 'a'

out of the tuple ((1,'a'),"foo").

---

`fst` is "first", `snd` is "second";
they get used for copying values out of tuples

using these, we can pull the character `'a'`out of `((1, 'a'), "foo")` with the following:

` snd ( fst ( 1, 'a' ), "foo") `

which pulls the second value out of the sub-tuple which was returned by `fst`

e.g.:

` fst ( 1, 'a' ), "foo" ` gets evalled to `( 1, 'a' )`,
which we then use `snd` to pull the second value out of
