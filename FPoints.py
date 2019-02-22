import sys

if len(sys.argv)<=2:
	print('No enough parameters.')
	exit(1)

if sys.argv[1].upper() in ('N', 'NORTH'):		# 1st parameter: N/E/S/W
	handIndex=0
elif sys.argv[1].upper() in ('E', 'EAST'):
	handIndex=1
elif sys.argv[1].upper() in ('S', 'SOUNTH'):
	handIndex=2
elif sys.argv[1].upper() in ('W', 'WEST'):
	handIndex=3
else:
	print('Please specify N/E/S/W as the 1st parameter!')
	exit(2)
	
try: 											# parameter: minimum points
	min = int(sys.argv[2])
except:
	print('Error at the 2nd parameter, the minimum points!')
	exit(3)

try: 											# parameter: maximum points, optional
	max = int(sys.argv[3])
except:
	max = 99	
	
EoF = False
try:
	line = input()								# 1st line
except EOFError:
	EoF = True
	
while not EoF:
	l = line.strip().split(',')					# str ==> list
	if len(l)==52:
		h = l[handIndex*13 : handIndex*13+13]	# get one hand, N/E/S/W
		point = 0
		for i in range(13):						# count points
			card=(int(h[i])-1)%13				# 0=A, 1=K, 2=Q, 3=J
			if card < 4:
				point += 4-card
		if point>=min and point<=max:			# print hand in point range
			print(line.strip())
	try:
		line = input()							# read next line
	except EOFError:
		EoF = True	
		
exit(0)		