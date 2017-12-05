#!/usr/bin/env python3

f = open("foofile","a")	#the "a" indicated that we are "a"ppending to a file, which sticks ...
f.write("Baz bar foo?")	#this bit of text at the end of the file.
f.close()		#this closes the file, which is a good thing to do for some reason or something
