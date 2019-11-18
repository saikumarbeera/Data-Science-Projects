"""
This module takes a single input file and returns the final x, y positions with the coins collected
First line has the board dimensions, the second line has the intial starting postion
Third line has the movements in N, E, W, S
Fourth line has the restricted x, y positions

The module returns [-1,-1,0] if there are any file validation failures

"""

__author__ = "Saikumar Beera"

def fCalculcation (vDirections, vMoves, x, y, rx, ry) :
    """This function does the edge validiation, calculation of the 
    valid moves and the total coins collected. 
    The function returns the x , y and total coins collections
    """
    if x > rx or y > ry:
        return (-1, -1, 0)
    vValidStack = []
    for  d in vDirections:
        x, y = x+d[0], y+d[1]
        if [x,y] not in vValidStack:
            vValidStack.append([x,y])
            
        if [x,y] in vMoves:
            x, y = x-d[0], y-d[1]
            vValidStack.pop()
            continue
        if  x > rx or x < 0 or  y > ry or y < 0 :
            x, y = x-d[0], y-d[1]
            vValidStack.pop()
            continue
    return [x, y, len(vValidStack)]
    


    

def pacman(inputFile):
    """ Use this function to format your input/output arguments. Be sure not to change the order of the output arguments. 
    Remember that code organization is very important to us, so we encourage the use of helper fuctions and classes as you see fit.
    
    Input:
        1. input_file (String) = contains the name of a text file you need to read that is in the same directory, includes the ".txt" extension
           (ie. "input.txt")
    Outputs:
        1. final_pos_x (int) = final x location of Pacman
        2. final_pos_y (int) = final y location of Pacman
        3. coins_collected (int) = the number of coins that have been collected by Pacman across all movements
    """

    with open (inputFile) as f:
        plines = f.read().splitlines()
        
    
    pCoins = 0
    # Directions stored
    lDirections = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    
    board_x, board_y = list(map(int, plines[0].split(' ')))
    initial_x, initial_y = list(map(int, plines[1].split(' ')))
    iDirections = list(plines[2])
    iMoves = list(plines[3:])
    
    # Our transfromations
    
    vMoves = []
    vDirections = []
    
    
    for i in range(len(iMoves)):
        vMoves.append(list(map(int, iMoves[i].split(' '))))
    
    for j in range(len(iDirections)):
        if iDirections[j]=='N':
            vDirections.append(lDirections[2])
        if iDirections[j]=='S':
            vDirections.append(lDirections[1])
        if iDirections[j]=='E':
            vDirections.append(lDirections[3])
        if iDirections[j]=='W':
            vDirections.append(lDirections[0])

    return fCalculcation(vDirections, vMoves, initial_x, initial_y, board_x, board_y)
    
    



    