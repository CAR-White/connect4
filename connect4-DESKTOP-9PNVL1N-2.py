board = [[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],
         [],[],[],[],[],[],[],
         [],[],[],[],[],[],[],
         [],[],[],[],[],[],[],
         [],[],[],[],[],[],[]
]
counter1 = "r"
counter2 = "y"



def count():
    
    cant_add = True
    possible = [0,1,2,3,4,5,6]
    
    while cant_add:
      red = int(input("choose a co-ordinate to add a counter:"))

      if red not in possible:
          print("this is not a valid co-ordinate try again")

      elif red in possible and board[red] != []:
          print("this is not a valid co-ordinate try again")

      else:
        cant_add = False
    return red
    
    
def addplay1():
   position = count()
   row = position + 35
   
   for i in range(row,0,-7):
        if board[i] == []:
            board[i].append(counter1)
            break
        pass
   #return board 

def addplay2():
   position = count()
   row = position + 35
   
   for i in range(row,0,-7):
        if board[i] == []:
            board[i].append(counter2)
            break
        pass
   #return board 


def row_check():
    row = False
    j = 0 
    while j < 36:
        for i in range(4):
            if board[j+i] == board[j+i+1] == board[j+i+2] == board[j+i+3] == ["r"]:
                row = True
                break
            else:
                pass
        j+=7
    return row

def diag_check1():
    diag1 = False
    j = 0
    while j<=14:
        for i in range(4):
            if board[j+i] == board[j+i+8] == board[j+i+16] == board[j+i+24] == ["r"]:
                diag1 = True
                break
        j+=7
    return diag1

def diag_check2():

    diag2 = False
    j = 0
    while j<=14:
        for i in range(3,7,-1):
            if board[j+i] == board[j+i+6] == board[j+i+12] == board[j+i+6] == ["r"]:
                diag2 = True
                break
        j+=7
    return diag2
    
def col_check():
    col = False
    j = 0
    while j < 6:
        for i in range(0,35,7):
            if board[j+i] == board[j+i+7] == board[i+j+14] == board[i+j+21] == ["r"]:
                col = True
                break
            else: 
                pass
        j+=1
    return col

          
def main():
    gamestate = True

    while gamestate:
        print(addplay1())
        if row_check() == True:
            gamestate = False
            return "player 1 wins"
        if diag_check1() == True:
            gamestate = False
            return "player 1 wins"
        if diag_check2 == True:
            gamestate = False
            return "player 1 wins"
        board_appear()
        
        print(addplay2())
        if row_check() == True:
            gamestate = False
            return "player 2 wins"
        if diag_check1() == True:
            gamestate = False
            return "player 2 wins"
        if diag_check2 == True:
            gamestate = False
            return "player 2 wins"
        board_appear()

def board_appear():
    k = 0
    while k<=35:
            print(board[k+0],board[k+1],board[k+2],board[k+3],board[k+4],board[k+5],board[k+6])
            k+=7
    

main()


   



