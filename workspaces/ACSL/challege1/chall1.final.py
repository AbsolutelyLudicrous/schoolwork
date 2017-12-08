#!/usr/bin/env python3

"""

	Finally get around to throwing the whole thing together

"""

import chall1Encoder as enc
import chall1Looper as loo

out=[]
for i in range(0,5):
	f=input(">")
	if f != "$":
		out.append(
			enc.alpha[loo.loop(
			enc.encode(f))+1]
		)
	else:
		break

print(out)
