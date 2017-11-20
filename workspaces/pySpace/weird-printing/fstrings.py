#!/usr/bin/env python3

import os

formatted=f"{distro} is the best GNU/Linux Software Distribution!"
distro=os.system("uname -a")

print(formatted)

#that code should work but fuck it
#only works in py3.6 but fuck solus

#distro=str(os.system("uname -a"))
#print(distro + " is the best GNU/Linux Software Distribution!")
