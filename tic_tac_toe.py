board=["","","","","","","","","",""]

def printBoard(board):
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print(' ' + board[1] + '  | ' + board[2] + '  | ' + board[3])
    print('-----------')
    print(' ' + board[4] + '  | ' + board[5] + '  | ' + board[6])
    print('-----------')
    print(' ' + board[7] + '  | ' + board[8] + '  | ' + board[9])
printBoard(board)
pos=["1","2","3","4","5","6","7","8","9"]
def win(a):
    flag=0
    #hor horizontal ckeck
    if((board[1]==a and board[2]==a and board[3]==a) or 
       (board[4]==a and board[5]==a and board[6]==a) or 
       (board[7]==a and board[8]==a and board[9]==a)):
        flag=1
    # vetrical check
    elif((board[1]==a and board[4]==a and board[7]==a) or
         (board[2]==a and board[5]==a and board[8]==a) or
         (board[3]==a and board[6]==a and board[9]==a)):
        flag=1
    # diagonal ckeck
    elif((board[1]==a and board[5]==a and board[9]==a) or
         (board[3]==a and board[5]==a and board[7]==a)):
        flag=1
    else:
        flag=0
    return flag

        
def printBoard(board):
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print(' ' + board[1] + '  | ' + board[2] + '  | ' + board[3])
    print('-----------')
    print(' ' + board[4] + '  | ' + board[5] + '  | ' + board[6])
    print('-----------')
    print(' ' + board[7] + '  | ' + board[8] + '  | ' + board[9])
printBoard(board)
def player1(n):
    posx=int(input("enter the position of x"))
    board[posx]=n
    pos.remove(str(posx))
    printBoard(board)
    if(win(n)==1):
        return 1
    else:
        return 0
        
def player2(m):
    poso=int(input("enter the position of o"))
    board[poso]=m
    pos.remove(str(poso))
    printBoard(board)
    if(win(n)):
        return 1
    else:
        return 0
        
n=input("enter p1")
m=input("enter p2")
while(len(pos)>0):
    temp=player1(n)
    if(temp==1):
        print("player 1 wins")
        break
    else:
        if(len(pos)==0):
            print("match tie")
    if(len(pos)>0):
        temp1=player2(m)
        if(temp1==1):
            print("player 2 wins")
            break
        else:
            if(len(pos)==0):
                print("match tie")

