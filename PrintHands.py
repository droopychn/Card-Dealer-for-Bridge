def oneHand(h):
	h.sort()
	hand = ['S:','H:','D:','C:']
	cards = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
	for i in h:
		hand[(i-1)//13] += cards[(i-1)%13]
	for i in range(4):
		hand[i] = hand[i].ljust(16)
	return hand
	
def showNS(hand):
	blank16 = ' '*16
	for i in range(4):
		hand[i] = blank16 + hand[i] + blank16
	return hand
	
def showEW(east, west):
	blank16 = ' '*16
	hand = ['']*4
	for i in range(4):
		hand[i] = west[i] + blank16 + east[i]
	return hand

def printHand(h):
	for i in range(4):
		print(h[i])
		

handNum = 0
EoF = False
try:
	line = input()												# 1st line
except EOFError:
	EoF = True
	
while not EoF:
	l = line.strip().split(',')								# str ==> list
	if len(l)==52:
		handNum += 1
		print('----- #', handNum, '-----')
		for i in range(52):									# list of str ==> list of int
			l[i] = int(l[i])
		printHand(showNS(oneHand(l[0:13])))
		printHand(showEW(oneHand(l[13:26]), oneHand(l[39:52])))
		printHand(showNS(oneHand(l[26:39])))
	try:
		line = input()										# read next line
	except EOFError:
		EoF = True	
exit(0)