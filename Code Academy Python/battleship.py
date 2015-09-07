import random

board=[]

#adds 5 rows *5 to the board

for i in range(5):
    board.append(["O"]*5)

#print board game into 5*5 grid

def print_board(board):
    for row in board:
        print (" ").join(row)

print "Let's play Battleship"
print_board(board)

def random_row(board):
    return random.randint(0,len(board)-1)

def random_col(board):
    return random.randint(0,len(board[0])-1)

ship_row=random_row(board)
ship_col=random_col(board)

print "The correct row is: %d" % ship_row
print "The correct col is: %d" % ship_col

#player has only four chances to guess the ship position
for turn in range(4):
    guess_row=int(raw_input("Guess Row: "))
    guess_col=input("Guess Col: ")

    # wins
    if guess_row==ship_row and guess_col==ship_col:
        print "Congratulations you sunk my battleship! \n"
        break #end the game if guess correctly
    else:
        # if all turns have passed, game is over
        if (turn==3):
            print "Game over, you have used all your turns. \n"
            break
        # check if guess out of range
        elif (guess_row>4 or guess_row<0) or (guess_col>4 or guess_col <0):
            print "Oops, that's not even in the ocean. \n"
        elif board[guess_row][guess_col]=='X':
            print "You guessed that one already. \n"
        else:
            print "You missed my battleship!\n"
            board[guess_row][guess_col]="X"
    print "you have used %d turn(s)" %(turn+1) # turn+1 so that user see turn 1,2,3,4 instead of 0,1,2,3
    print_board(board)

print 'The correct row is: %d\n' % ship_row
print 'The correct col is: %d\n' % ship_col
