"""

	Enterprise-grade switcherooing
	TODO errors on non-standard input

"""

var = input("enter a letter ")

def switch(inp):
	default = 'Not supported, TODO'
	return {
		'a':'Fuckin\' a',
		'b':'Entered b',
		'c':'Entered c',
		'd':'Entered d',
		'e':'Entered e'
	}.get(inp, default)
print(var)
out = switch(var)
print(out)
