#C O N N E C T  F O U R
def newBoardPrint():
def firstMoveBoardPrint(move):
def nextMoveBoardPrint(move, previousBoard):
	
i = 0
while(i < 8):
	print ("|___|___|___|___|___|___|___|")
	i += 1
megaList = [ [], [], [], [], [], [], []]
def newBoardPrint():
	y=0
	while(y<6):
		x=0
		while(x<7):
			print("| _"),
			x +=1
		print ("|")
		y +=1

def firstMoveBoardPrint(move):
	print ("+•••+•••+•••+•••+•••+•••+•••+")
	y=1
	while(y<7):
		x=1
		while(x<8):
			print("| _"),
			x +=1
		print ("|")
		y +=1
	print ("+•••+•••+•••+•••+•••+•••+•••+")

def firstMoveBoardPrint(move):
	print ("+•••+•••+•••+•••+•••+•••+•••+")
	y=1
	while(y<7):
		x=1
		while(x<8):
			if (y == 6 and x == move):
				print("| x"),
			else:
				print("| _"),
			x +=1
		print ("|")
		y +=1
	print ("+•••+•••+•••+•••+•••+•••+•••+")


'''previousBoard = [[" ", "X", "O", " ", " ", " ", " "],
					[" ", "X", "O", " ", " ", " ", " "],
					[" ", "X", "O", " ", " ", " ", " "],
					[" ", "X", "O", " ", " ", " ", " "],
					[" ", "X", "O", " ", " ", " ", " "],
					[" ", "X", "O", " ", " ", " ", " "],]

'''
def nextMoveBoardPrint(move, previousBoard):
	print ("+•••+•••+•••+•••+•••+•••+•••+")
	y=1
	while(y<7):
		x=1
		while(x<8):
			if (y == 6 and x == move):
				print("| x"),
			else:
				print("| _"),
			x +=1
		print ("|")
		y +=1
	print ("+•••+•••+•••+•••+•••+•••+•••+")









	