board = [[" "],[" "],[" "],[" "],[" "],[" "],[" "],
         [" "],[" "],[" "],[" "],[" "],[" "],[" "],
         [" "],[" "],[" "],[" "],[" "],[" "],[" "],
         [" "],[" "],[" "],[" "],[" "],[" "],[" "],
         [" "],[" "],[" "],[" "],[" "],[" "],[" "],
         [" "],[" "],[" "],[" "],[" "],[" "],[" "]
]
counter1 = "r"
counter2 = "y"



def count():
    
    cant_add = True
    possible = [0,1,2,3,4,5,6]
    
    while cant_add:
      red = int(input("choose a number for columns in range 0-6 to add a counter:"))

      if red not in possible:
          print("this is not a valid column try again")

      elif red in possible and board[red] != [" "]:
          print("this is not a valid column try again")
      else:
        cant_add = False
    return red
    
    
def addplay1():
   print("player1")
   position = count()
   row = position + 35
   
   for i in range(row,-1,-7):
        if board[i] == [" "]:
            board[i] = ["r"]
            break
        pass
   #return board 

def addplay2():
   print("player 2")
   position = count()
   row = position + 35
   
   for i in range(row,0,-7):
        if board[i] == [" "]:
            board[i] = ["y"]
            break
        pass
   #return board 


def row_check(a: list[str]):
    row = False
    j = 0 
    while j <= 35:
        for i in range(4):
            if board[j+i] == board[j+i+1] == board[j+i+2] == board[j+i+3] == a:
                row = True
                break
            else:
                pass
        j+=7
    return row

def diag_check1(a:list[str]):
    diag1 = False
    j = 0
    while j<=14:
        for i in range(4):
            if board[j+i] == board[j+i+8] == board[j+i+16] == board[j+i+24] == a:
                diag1 = True
                break
        j+=7
    return diag1

def diag_check2(a:list[str]):

    diag2 = False
    j = 0
    while j<=14:
        for i in range(3,7,1):
            if board[j+i] == board[j+i+6] == board[j+i+12] == board[j+i+18] == a:
                diag2 = True
                break
        j+=7
    return diag2
    
def col_check(a:list[str]):
    col = False
    j = 0
    while j <= 6:
        for i in range(0,15,7):
            if board[j+i] == board[j+i+7] == board[i+j+14] == board[i+j+21] == a:
                col = True
                break
            else: 
                pass
        j+=1
    return col

def draw():
    drawstate = False
    b = 0
    for i in board:
        if i != [" "]:
            b+=1
        pass
    if b == 42:
        drawstate = True
    return drawstate

          
def main():
    gamestate = True

    while gamestate:
        addplay1()
        if row_check(["r"]) == True:
            gamestate = False
            print("player 1 wins")
            break
        elif col_check(["r"]) == True:
            gamestate = False
            print("player 1 wins")
            break
        elif diag_check1(["r"]) == True:
            gamestate = False
            print("player 1 wins")
            break
        elif diag_check2(["r"]) == True:
            gamestate = False
            break
        elif draw() == True:
            print("draw")
            gamestate = False
            break

        else:
            print(board_appear2())
            
        
        addplay2()
        if row_check(["y"]) == True:
            gamestate = False
            print("player 2 wins")
            break
        elif col_check(["y"]) == True:
            gamestate = False
            print("player 1 wins")
            break
        elif diag_check1(["y"]) == True:
            gamestate = False
            print("player 2 wins")
            break
        elif diag_check2(["y"]) == True:
            gamestate = False
            print("player 2 wins")
            break
        elif draw() == True:
            print("draw")
            gamestate = False
            break

        else:
         print(board_appear2())

    print(board_appear2())
    return "game over"


def board_appear():
    k = 0
    while k<=35:
            print(board[k+0],board[k+1],board[k+2],board[k+3],board[k+4],board[k+5],board[k+6])
            k+=7
    

def board_appear2():
    i = 0
    k=0
    while i < 42:
        for j in range(0,7):
            print("   #####     ",end="")
        print("")

        for j in range(0,7):
            print("  #     #    ",end="")
        print("")

        for j in range(0,7):
            print(f" #   {board[k+j][0]}   #   ",end="")
        print("")

        for j in range(0,7):
            print("  #     #    ",end="")
        print("")
        
        for j in range(0,7):
            print("   #####     ",end="")
        print("")
        i+=7
        k+=7
        



print(main())


   


#board[i].append(counter2)