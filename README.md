# Card-Dealer-for-Bridge
Deal cards for bridge game

try to use by commands:  "python Dealer.py | PrintHands.py" or "python Dealer.py 50 | F2Suits.py | PrintHands.py"

Cards are numbered from 1 to 52. 
Spades: #1-13; Hearts: #14-26; Diamonds: #27-39; Clubs: #40-52. Sequencing from A to 2 in each suit.

Dealer.py - Shuffle cards and send to stdout. Optional 1st parameter as number of boards to deal.

PrintHands.py - Print boards from stdin (by line). North: position 1-13; East: pos 14-26; South: pos 27-39; West: pos 40-52.

F2Suits.py - Filter out hands having 55+ 2 suits. 1st parameter: N/E/S/W, default to South.

FLong6.py - Filter out hands having 6+ long suit. 1st parameter: N/E/S/W, default to South.

FPoints.py - Filter out hands in point range. 1st parameter: N/E/S/W; 2nd: low limit of points; 3rd: hight limit, optional.

FShapeNT.py - Filter out blanced hands, 4432, 4333, 5332, 6322 (C/D suit). 1st parameter: N/E/S/W, default to South.

FShort.py, FVoid.py - Filter out short/void. 1st parameter: N/E/S/W, default to South.



Just1Board.py - Differenct from other programs here, this one simply deal and show 1 board, without collaboration with others.
