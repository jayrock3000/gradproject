'''
The two algorithms you're looking at for maze generation:
1. Recursive Backtracking
2. Prim's Algorithm
'''
#################################################################################
# Function for console printout of maze

def printMaze(maze):
    for row in maze:
        print(row)

#################################################################################
# Function creates the initial maze, completely filled with walls

def generateFilledMaze(sizeX, sizeY):
    maze = []

    # Size XY represents CLEAR spaces
    # Extend so walls can go in-between
    trueSizeX = 2*sizeX + 1
    trueSizeY = 2*sizeY + 1

    for i in range(trueSizeY):
        row = []
        for j in range(trueSizeX):
            # Handle first and last rows
            if i == 0 or i == (trueSizeX-1):
                row.append(1)
                continue

            # Check if it's a clear cell
            if j%2 != 0 and i%2 != 0:
                row.append(0)
                continue
            
            # Walls otherwise
            else:
                row.append(1)
        maze.append(row)

    return maze


#################################################################################
# Function handles reverse backtracking
# Knock out walls while exploring randomly


def removeWalls(maze, sizeX, sizeY):
    import random
    frontier = []
    visited = []

    # pick start point at random (adjusted for walls)
    randX = 2 * random.randint(1, sizeX) - 1
    randY = 2 * random.randint(1, sizeY) - 1

    print(f"randX is {randX}")
    print(f"randY is {randY}")

    # Mark starting position
    maze[randX][randY] = 2

    while frontier:
        pass

    return maze

def navigate():
    pass

#################################################################################
# Section handles creation of maze

'''
maze = [
    [1,9,5,0,1,1,1,1], 
    [1,1,1,1,1,1,1,1], 
    [1,1,1,1,1,1,1,1], 
    [1,1,1,0,1,1,1,1], 
    [1,1,1,1,1,1,1,1], 
    [1,0,1,1,1,1,1,1], 
    [1,1,1,1,1,1,1,1], 
    [1,1,1,1,1,1,1,1], 
    ]
'''

x = 10
y = 10
aMaze = generateFilledMaze(x, y)

printMaze(aMaze)

aMaze = removeWalls(aMaze, x, y)

printMaze(aMaze)
