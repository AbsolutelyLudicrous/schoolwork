#!/usr/bin/env python3
"""
	configuration file for the C3 walker array
	contains just the 1/0s array
"""
N=None
board=(
	(N,2,2,2,2,2,2,2,2,N),
	(2,0,0,0,0,1,1,0,0,2),
	(2,1,1,0,0,0,1,1,1,2),
	(2,1,0,0,0,0,1,0,1,2),
	(2,1,1,0,1,0,1,1,0,2),
	(2,0,1,0,0,0,1,1,0,2),
	(2,1,1,0,1,0,1,1,1,2),
	(2,1,1,1,0,0,1,1,0,2),
	(2,1,0,0,0,0,1,1,1,2),
	(N,2,2,2,2,2,2,2,2,N)
)	#the 2s serve to indicate that 0) the walker should wrap around and 1) as padding
