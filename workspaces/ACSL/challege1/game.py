#!/usr/bin/env python3

import player as pl

debug=True

args=input(">").split(" ")
if debug:
	print("Arguments: ",args," with type ", type(args))

total=int(args[0])
dealer=pl.player(args[1:3])
player=pl.player(args[4:6])
stack=args[6:]

while total < 100:
	total+=int(player.getHighestCard())
	del(
		player.cards[
			player.cards.index(player.getHighestCard())
		]
	)
	if total > 99:
		print(total,"player")
		break

	total+=int(dealer.getHighestCard())
	del(
		dealer.cards[
			dealer.cards.index(dealer.getHighestCard())
		]
	)
	if total > 99:
		print(total,"dealer")
		break
