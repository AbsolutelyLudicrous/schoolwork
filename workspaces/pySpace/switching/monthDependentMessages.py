import time

def getMonth():
	month = time.strftime("%B")
	return month

def monthSwitch(month):
	if month is 'September':
		return 'It is Septembre, my dudes'
	elif month is 'July':
		return 'That isn\'t quite right.'
	else:
		return month

mon = getMonth()
output = monthSwitch(mon)
print(output)
