#tic tac toe game with AI to play against 

#TODO:
#if neither can win, end game early

import random 
gameCounter = 0
winCount = {}
player, player1, player2, computer, mode = 0,0,0,0,0

def printBoard(board):
    print
    for i in range(9):
        if i%3 == 0 or i == 8:
            print "   |   |"
        elif i%3 == 1:
            print '', board[i-1],'|', board[i], '|', board[i+1]
        elif i<8:
            print "___|___|___"
    print
    
def clearBoard(): #sets up a board of all empty spaces
    return[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
def turn(player, board):
    while True:
        move = raw_input("Where would you like to move, player " + player + "? ")
        try:                            #in case a noninteger is input
            move = int(move)
        except:
            print "Please enter an integer"
            continue
        if move >= 1 and move <=9:      #make sure number is in range of board
            if board[move - 1] == ' ':      #if empty slot
                board[move - 1] = player    #set slot to that player
                break
            else:
                print "That slot is not available"
        else:
            print "Number not in range (1-9)"
    printBoard(board)

def AI(computer, player, board, mode):
    print "Computer's move:"
    unused = []                 #list of slots available
    for i in range(len(board)): 
        if board[i] == ' ':     #if empty add to available    
            unused.append(i)
    for move in unused:
        board[move] = computer      #try each move, if it wins, leave that and print it
        if computer == win(board):  
            printBoard(board)
            return
        else:
            board[move] = ' '       #if not, put the blank back            
    if mode[0] == 'h':              #only check for defense if on hard mode
        for move in unused:             #otherwise, see if the player could win, has to have its own loop so it tries all wins first
            board[move] = player
            if player == win(board):
                board[move] = computer
                printBoard(board)
                return
            else:                   
                board[move] = ' '
    rand = random.randrange(len(unused)-1) #if no move will win, choose a random empty slot
    board[unused[rand]] = computer
    printBoard(board)
    
def win(board):
    winner = ''
    for i in range(3):
        n = 3*(i+1) - 1 #used for row calculations, makes (0,1,2) into (2, 5, 8)
        if board[i] != ' ':
            if board[i] == board[i+3] and board[i+3] == board[i+6]: #checks column wins
                winner = board[i]
        if board[n] != ' ':
            if board[n] == board[n - 1] and board[n - 1] == board[n - 2]: #checks rows for wins
                winner = board[n]
    if board[4] != ' ': 
        if board[0] == board[4] and board[4] == board[8]: #left diagonal
            winner = board[4]
        elif board[2] != ' ' and board[2] == board[4] and board[4] == board[6]: #right diagonal 
            winner = board[4]
    return winner
    
    
#GAMEPLAY OPTIONS
def PVPgame():
    global winCount, player1, player2
    board = clearBoard() #initialize board as empty
    #get symbols
    if gameCounter == 0:
        player1 = raw_input("What symbol would you like to play as? ")[0] #the [0] is in case they enter more than 1 character
        while True: #to make sure that each player has a unique character
            player2 = raw_input("What symbol would you like to play as? ")[0]
            if player2 != player1:
                break
        winCount={player1 : 0, player2 : 0}
    #show board labels
    print "Use the numbers on this chart to specify which space you would like to move to"
    printBoard([1,2,3,4,5,6,7,8,9]) #use to show the options for spaces
    #play game
    for i in range(9): 
        if i%2 == 0:
            turn(player1, board)
        else:
            turn(player2, board)
        winner = win(board) 
        if winner != '':
            print "Player " + winner + " wins!"
            winCount[winner] += 1      
            break
        if i == 8:
            print "You've tied!"

def AIgame():
    global winCount, player, computer, mode
    board = clearBoard() #initialize board as empty            
    #set symbols 
    if gameCounter == 0:
        player = raw_input("Would you like to be X or O? ")[0] #the [0] is in case they enter more than 1 character
        if player == 'X':
            computer = 'O'
        else:               #as long as whatever was entered is not X, it can play against X
            computer = 'X'
        winCount = {player : 0, computer : 0}
        while True:
            mode = raw_input("Would you like to play easy or hard mode? ").lower()
            if mode == "easy" or mode == "hard" or mode == 'e' or mode == 'h':
                break
    #show board labels
    print "Use the numbers on this chart to specify which space you would like to move to"
    printBoard([1,2,3,4,5,6,7,8,9]) #use to show the options for spaces
    #play game
    for i in range(9):
        if i%2 == 0:
            turn(player, board)
        else:
            AI(computer, player, board, mode)
        winner = win(board)
        if winner != '':
            winCount[winner] += 1    
            if winner == player:
                print "Player wins!"
            else:
                print "Computer wins!"
            break
        if i == 8:
            print "You've tied!"
    
#GAMEPLAY
print "Welcome to Tic Tac Toe!"
while True:
    useAI = raw_input("Would you like to play against another player or the computer? ").lower() #.lower to make comparing easier
    if useAI == "computer" or useAI == 'c' or useAI == "player" or useAI == 'p':
        break
again = 'y'
while again == "yes" or again == 'y':
    if useAI == "computer" or useAI == 'c':
        AIgame()
    else:
        PVPgame()
    again = raw_input("Rematch? ").lower() 
    gameCounter += 1
    players = winCount.keys()
    print "You have played " + str(gameCounter) + " games!"
    for p in players:               
        if p == computer:
            print "Computer has won " + str(winCount[p]) + " games!"
        else:
            print "Player " + p + " has won " + str(winCount[p]) + " games!"
