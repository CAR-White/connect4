"""board = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0]
]"""
board = [[],[],[],[],[],[],[],
         [],[],[],[],[],[],[],
         [],[],[],[],[],[],[],
         [],[],[],[],[],[],[],
         [],[],[],[],[],[],[],
         [],[],[],[],[],[],[]
]

board2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2"]

"""
def row_sol():
    row = "no row victory"
    j = 0 
    while j < 36:
        for i in range(4):
            if board[j+i] == board[j+i+1] == board[j+i+2] == board[j+i+3] == ["r"]:
                row = "row victory"
                break
            else:
                pass
        j+=7
            
    return row"""
        

def diag_sol1():
    diag1 = False
    j = 0
    while j<=14:
        for i in range(4):
            if board[j+i] == board[j+i+8] == board[j+i+16] == board[j+i+24] == ["r"]:
                diag1 = True
                break
        j+=7
    return diag1

def diag_sol2():
    diag2 = False
    j = 0
    while j<=14:
        for i in range(3,7,-1):
            if board[j+i] == board[j+i+6] == board[j+i+12] == board[j+i+6] == ["r"]:
                diag2 = True
                break
        j+=7
    return diag2
    
    
    
            
            
    


    #if board[14] == board[22] == board[30] == board[38] == "r":
        
"""
i = 0
while i < 28:
        print("   #####        #####        #####        #####        #####        #####        #####")


        print("  #     #      #     #      #     #      #     #      #     #      #     #      #     #")


        print(f" #   {board2[i]}   #    #   {board2[i+1]}   #    #   {board2[i+2]}   #    #   {board2[i+3]}   #    #   {board2[i+4]}   #    #   {board2[i+5]}   #    #   {board2[i+6]}   #")



        print("  #     #      #     #      #     #      #     #      #     #      #     #      #     #")


        print("   #####        #####        #####        #####        #####        #####        #####  \n")
        i+=7
"""


i = 0
k=0
while i < 28:
    for j in range(0,7):
        print("   #####     ",end="")
    print("")

    for j in range(0,7):
        print("  #     #    ",end="")
    print("")

    for j in range(0,7):
        print(f" #   {board2[k+j][0]}   #   ",end="")
    print("")

    for j in range(0,7):
        print("  #     #    ",end="")
    print("")
    
    for j in range(0,7):
         print("   #####     ",end="")
    print("")
    i+=7
    k+=7
    


