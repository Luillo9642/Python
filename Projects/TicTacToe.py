#For Tic Tac Toe
def winner(board):
    #Verify horizontal wins
    for x in range(3):
        if(board[x][0] == board[x][1] == board[x][2] != "   "):
            return True
    #Verify vertical wins
    for x in range(3):
        if(board[0][x] == board[1][x] and board[1][x] == board[2][x] != "   "):
            return True
    #Verify diagonal wins
    for x in range(3):
        if(board[0][0]==board[1][1]==board[2][2] != "   " or board[2][0]==board[1][1]==board[0][2] != "   "):
            return True
    return False



def printNewBoard():
	for x in range(3):
		print ("|   |   |   |")



def updateBoard(board, move):
	board[move[1]][move[2]] = move[0]
	for x in range(3):
		print ("|" + board[x][0] + "|" + board[x][1] + "|" + board[x][2] + "|")
	return board



def player(turn):
	if(turn%2 == 0):
		return " o "
	return " x "



def validMove(board, move):
		valid = True
		#For out of range inputs (all numbers except 1,2 and 3):
		if(move[1] < 0 or move[1] > 2):
			print("Row out of range")
			valid = False
		if(move[2] < 0 or move[2] > 2):
			print("Column out of range")
			valid = False
		#If the player inputs a move in where there is already a symbol in it:
		try:
			if(board[move[1]][move[2]] != "   "):
				print("Spot already taken")
				valid = False
		except:
			return valid
		return valid



def TicTacToe():
	printNewBoard()
	board = [["   ", "   ", "   "],
         	 ["   ", "   ", "   "],
         	 ["   ", "   ", "   "]]
	n = "Keep going."
	turn = 1
	while(turn < 10):
		move = [" ", 0,0]
		move[0] = player(turn)
		while(True):
			try:
				x = input("Which row?  *Has to be from 1-3* ")
				y = input("Whic column?  *Has to be from 1-3* ")
				move[1] = int(x) - 1
				move[2] = int(y) - 1
				if(validMove(board, move)):
						break
			except ValueError:
				print ("Try Again.  Remember: The numbers are from 1-3 and you cannot put your symbol(wether x or o) on top of another.")
		board = updateBoard(board, move)
		if(winner(board) == True):
			n = "GAME END.  Player"+move[0]+"wins."
		print (n)
		turn += 1
		if(n == "GAME END.  Player"+move[0]+"wins."):
			return n
		while(turn == 10):
			n = "GAME OVER"
			return n

TicTacToe()