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
        
    






