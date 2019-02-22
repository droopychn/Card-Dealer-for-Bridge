import sys

if len(sys.argv)<=1:
	handIndex=2									# default to South
elif sys.argv[1].upper() in ('N', 'NORTH'):		# 1st parameter: N/E/S/W
	handIndex=0
elif sys.argv[1].upper() in ('E', 'EAST'):
	handIndex=1
elif sys.argv[1].upper() in ('S', 'SOUNTH'):
	handIndex=2
elif sys.argv[1].upper() in ('W', 'WEST'):
	handIndex=3
else:
	handIndex=2									# default to South
	
EoF = False
try:
	line = input()								# 1st line
except EOFError:
	EoF = True
	
while not EoF:
	l = line.strip().split(',')					# str ==> list
	if len(l)==52:
		h = l[handIndex*13 : handIndex*13+13]	# get one hand, N/E/S/W
		shape = [0, 0, 0, 0]
		for card in h:
			shape[(int(card)-1)//13] += 1
		diamond = shape[2]						# save # of diamonds and clubs before sorting
		club = shape[3]
		shape.sort(reverse=True)
			
		if shape in [[4,3,3,3], [4,4,3,2], [5,3,3,2]] or shape==[6,3,2,2] and (diamond==6 or club==6):	
			print(line.strip())					# output hand in correct shape
		
	try:
		line = input()							# read next line
	except EOFError:
		EoF = True	
		
exit(0)		