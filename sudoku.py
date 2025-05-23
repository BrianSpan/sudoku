"""Another example of Sudoku solving using brute force backtracking"""

#Enable if you want a graphic display of the calculation
DISPLAYPROGRESS=True

#Sample data
"""
board=[3,9,0,  0,5,0,  0,0,0,
       0,0,0,  2,0,0,  0,0,5,
       0,0,0,  7,1,9,  0,8,0,
       
       0,5,0,  0,6,8,  0,0,0,
       2,0,6,  0,0,3,  0,0,0,
       0,0,0,  0,0,0,  0,0,4,
       
       5,0,0,  0,0,0,  0,0,0,
       6,7,0,  0,0,5,  0,4,0,
       1,0,9,  0,0,0,  2,0,0]
"""
board=[0,7,0,  6,2,9,  3,0,0,
       3,0,0,  0,5,0,  0,0,0,
       0,0,0,  0,7,0,  0,0,1,
       
       4,0,7,  0,0,0,  0,1,3,
       0,0,0,  2,0,0,  0,8,7,
       0,8,0,  0,9,0,  0,0,4,
       
       0,3,2,  0,8,6,  0,0,0,
       5,0,0,  4,0,0,  0,0,2,
       0,0,4,  9,0,2,  0,0,8]


########
# Functions
########

#Check if guess will word in the square
def isvalid(board,location,guess):
    if not isvalidrow(board,location,guess):
        return(False)
    if not isvalidcol(board,location,guess):
        return(False)
    if not isvalidbox(board,location,guess):
        return(False)
    return(True)

#Helper validation functions
def isvalidrow(board,location,guess)->bool:
    #test if already in row
    rowstart=(location//9)*9
    for testlocation in range(rowstart,rowstart+9):
        if board[testlocation]==guess:#finding the number is invalid
            return False
    return(True)


def isvalidcol(board,location,guess)->bool:
    #test if in column
    colstart=location%9
    for testlocation in range(colstart,81,9):
        if board[testlocation]==guess:#finding the number is invalid
            return False
    return(True)

def isvalidbox(board,location,guess)->bool:
    #test if in box
    #the math is a little messy
    colstart=location%9
    threerows=27
    colsinbox=3
    boxstart=((location//threerows)*threerows) \
             +((colstart//colsinbox)*colsinbox)
    for i in range(9):
        testlocation=boxstart+((i//3)*9)+(i%3)
        if board[testlocation]==guess:#finding the number is invalid
            return False
    return(True)


#display functions
def printgrid(board)->None:
    #When complete, display in terminal
    for line in range(9):
        if line%3==0 and line!=0:
            print()
        startofline=line*9
        #join() would not work because I want an extra space between groups of 3
        print (*[str(board[square])
                 +(' ' if (square+1)%3==0 else '')
                 for square in range(startofline,startofline+9)
                ])

def pygamedraw(board:list)->None:
    startx:int=10 #horizontal pos of where we start to draw
    starty:int=10 #vertical pos of where we start to draw
    charwidth:int=25 #how wide is cell
    charheight:int=35 #how tall is cell

    screen.fill((0,0,0))#black
    textcolor=(255,255,255)#white
    for i in range(81):
        text=str(board[i]) if board[i]!=NOTFILLED \
             else '.'
        #calculate position    and the gap between sets
        x=startx+((i%9)*charwidth)     +(charwidth*((i%9)//3))
        y=starty+((i//9)*charheight)   +(charheight*((i//27)))
        out=font.render(text,True,textcolor)
        screen.blit(out,(x,y))
    pygame.display.flip()
    sleep(0.01) #change depending on your machine speed

#Main function
def ssolve(board):
    try:
        #find first NOTFILLED location
        location=board.index(NOTFILLED)
    except:
        #all solved
        return True
    
    #see if any digit works
    for guess in range(1,10):
        if isvalid(board,location,guess):
            board[location]=guess
            if DISPLAYPROGRESS:
                pygamedraw(board)
            if ssolve(board):
                return(True)

        #if no guesses work, fail and recurse to previous
        board[location]=NOTFILLED
        
    #We have no solution
    return(False)    


############
# Main program
############
#Constant for readability
NOTFILLED=0

if DISPLAYPROGRESS:
    import pygame
    from time import sleep
    
    pygame.init()
    screen=pygame.display.set_mode((290,400))
    font=pygame.font.SysFont("DejaVuSansMono-Bold.ttf",56)
    pygame.display.set_caption('Sudoku Progress')
if (ssolve(board)):
    print('Solved!')
    printgrid(board)
else:
    print("This board does not have a valid solution")
