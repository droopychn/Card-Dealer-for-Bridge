import sys
from random import shuffle

if len(sys.argv)<=1:
	num = 1
else:
	try: 
		num = int(sys.argv[1])
	except ValueError:
		print('!error number!')
		exit(1)
	
l=list(range(1,53))				# card No.1-52
for i in range(num):	
	shuffle(l)
	s=str(l)
	s=s[1:len(s)-1]				# remove '[' and ']'
	print(s)
	
exit(0)