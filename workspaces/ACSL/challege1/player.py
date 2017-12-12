#!/usr/bin/env python3

debug=True

class player:
	#A single card game player

	cards=[]	#list of the player's cards
	aceValue=1	#| 
	jackValue=10	#| default values of face cards
	queenValue=10	#| can be overridden
	kingValue=10	#| 

	def __init__(self,cards=[]):
		#cards list defaults to empty
		self.cards=cards
		global debug
		if debug:
			print("Making a new card game player as ",self)

	def getCardsSum(self):
		out=[]	#temporary empty list
		for card in self.cards:	#this loop converts all face cards into actual numeric values
			if card not in range(2,9):	#if the card is not a number card
				out.append({	"T":10,			#| 
						"A":self.aceValue,	#| This is a nifty way of doing a switch statement in Python:
						"J":self.jackValue,	#| Use a dict!
						"Q":self.queenValue,	#| (I feel like I'm trying to turn Python into Haskell, but w/e)
						"K":self.kingValue	#| 
					}[card])			#| You basically make a dict of your cases and then access the value that corresponds to the case you want
			else:						#| (I'm ridiculously proud of this format, in case you couldn't tell)
				out.append(card)
		global debug
		if debug:
			print("Returning sum of ",out,", which has type ",type(out))
			types=""
			for i in out:
				types+=str(type(i))
			print("Each element in ",out," has type ",types)
		return sum(out)

	def getHighestCard(self, onlyNums=False):
	#| return the highest value card,
	#| contains optional parameters for 
	#| 	(onlyNums):	whether we only want to deal with number cards, overrides aceValue
		if onlyNums:
			global debug
			if debug:
				print("Taking the highest value of the cards, ignoring face cards.")
			out=[]	#list of numbers to be maxed
			for card in self.cards:
				if type(card) is type(1):	#if the type of the current card matches the type of this integer
					out.append(card)	#append all integers to this temporary list
			global debug
			if debug:
				print("Returning maximum value from ",out,", which has type ",type(out))
			return max(out)
		else:
			out=[]	#temporary empty list
			for card in self.cards:	#this loop converts all face cards into actual numeric values
				if card not in range(2,9):	#if the card is not a number card
					out.append({	"T":10,
							"A":self.aceValue,
							"J":self.jackValue,
							"Q":self.queenValue,
							"K":self.kingValue
						}[card])
				else:
					out.append(card)
			global debug
			if debug:
				print("Returning maximum value from ",out,", which has type ",type(out))
				types=""
				for i in out:
					types+=str(type(i))
				print("Each element in ",out," has type ",types)
			return max(out)
