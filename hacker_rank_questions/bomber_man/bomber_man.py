#!/bin/python

import sys


# list where index == the amount of seconds until bomb explodes
time_to_explosion = [ [], [], [] ]

# set keeping track of whether a bomb exists at tuple (i, j)
has_bomb = set()



############################################################
# Input/Output of bombfield matrix:                        #
#                                                          #
# Matrix is passed in as strings, convert them to a matrix #
# to make changing assignment easier                       #
############################################################


def to_matrix(grid):
    rows = len(grid)
    cols = len(grid[0])
    matrix = list()
    for i in range(0, rows):
        matrix.append(list())
        for j in range(0, cols):
            matrix[i].append(grid[i][j])
    return matrix

def to_string(grid):
    ret = list()
    for i in range(0,len(grid)):
        string = ""
        for j in range(0, len(grid[0])):
            string += str(grid[i][j])
        ret.append(string)
    return ret



#########################################################
# Processing the passed in bombfield:                   #
#                                                       #
#     for each i,j in grid:                             #
#         if it's "0", it's a bomb and should be        #
#         recorded as such --> its going off in 3 secs! #
#########################################################

def process_initial_bombfield(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == "0":
                has_bomb.add((i,j))
                time_to_explosion[2].append((i,j))



##################################################
# Planting all bombs:                            #
#                                                #
#     for every i,j combination not in has_bomb: #
#         plant that bomb!                       #
#         add i,j to has_bomb set                #
##################################################

def plant_all_bombs(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if (i,j) not in has_bomb:
                plant_bomb(grid, i, j) # plant_bomb adds to has_bomb set


###########################################################################
# Planting a bomb at i, j:                                                #
#                                                                         #
#     1. switch the representation of cell i, j to "0"                    #
#     2. record the time the bomb will explode to n+3 (n == current_time) #
###########################################################################
    
def plant_bomb(grid, i, j):
    grid[i][j] = "0"
    time_to_explosion[2].append((i,j)) # this bomb will go off in three seconds
    has_bomb.add((i,j))         # keep track that bomb is at this cell


########################################################################
# Exploding all the bombs!                                             #
#                                                                      #
#     for every (i,j) tuple at time_to_explosion[0]:                   #
#         explode!                                                     #
#         copy lists at time_to_explosion[i] to time_to_explosion[i-1] #
#         make sure that time_to_explosion[3] is an empty list!        #
########################################################################

def explode_all_bombs(grid):
    print grid
    for coordinate in time_to_explosion[0]:
        explode_bomb(grid, coordinate[0], coordinate[1]) # time_to_explosion[0] is a list of tuples
    time_to_explosion.pop(0)                             # done with all the bombs at 0, bombs at 1 are now at 0
    time_to_explosion.append(list())                     # append an empty list at 2


################################################################################
# Explosion at i, j:                                                           #
#     1. change cell at i, j to "."                                            #
#     2. update time_to_explosion[i, j] to None                                #
#     3. if they exist, repeat steps 1 and 2 for (i +/- 1, j) and (i, j +/- 1) #
################################################################################
    
def explode_bomb(grid, i, j):
    if (i,j) in has_bomb:       # bomb might have been destroyed by another bomb
        _explode_bomb(grid, i, j)   # _explode_bomb will do bounds checks
        _explode_bomb(grid, i+1, j)
        _explode_bomb(grid, i-1, j)
        _explode_bomb(grid, i, j+1)
        _explode_bomb(grid, i, j-1)

def _explode_bomb(grid, i, j):
    if _is_legal_indices(grid, i, j):
        grid[i][j] = "."
        if (i,j) in has_bomb:   # make sure we don't have phantom bombs but there might be better way to do this
            has_bomb.remove((i,j))

def _is_legal_indices(grid, i, j):
    if i >= 0 and i < len(grid):
        if j >= 0 and j < len(grid[i]):
            return True
    return False

# bomberMan plants a bomb every two seconds, starting at time == 0
def time_to_plant(time):
    return time % 2 == 0 



def bomberMan(n, grid):
    # Complete this function
    grid = to_matrix(grid)
    process_initial_bombfield(grid)
    curr_time = 0
    while curr_time is not n:
        explode_all_bombs(grid)
        if time_to_plant(curr_time):
            plant_all_bombs(grid)
        curr_time += 1
    return to_string(grid)



if __name__ == "__main__":
    r, c, n = raw_input().strip().split(' ')
    r, c, n = [int(r), int(c), int(n)]
    grid = []
    grid_i = 0
    for grid_i in xrange(r):
        grid_t = str(raw_input().strip())
        grid.append(grid_t)
    result = bomberMan(n, grid)
    print "\n".join(map(str, result))



