"""

	Simple program for fizzing your buzz

"""
# E N T E R P R I S E L E V E L V A R I A B L E D E C L A R A T I O N
fizz='fizz'
buzz='buzz'

for num in range(1,100):
	if num % 3 is 0:
		print(fizz)
	if num % 5 is 0:
		print(buzz)
	if not (num % 3 is 0) and not (num % 5 is 0):
		print(num)
