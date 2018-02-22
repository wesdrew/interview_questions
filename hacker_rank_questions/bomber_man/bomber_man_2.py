#!/bin/python

import sys



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


##############################################################################
# After initial boards (at 0, 1, 2), the bomberman grid will settle          #
# into this pattern                                                          #
#     first, board i_3 at 3 + 4*k                                            #
#     then,  board i_4 at 4 + 2*k                                            #
#     finally, board i_5 at 5 + 4*k                                          #
#                                                                            #
# return a list with boards @ time_step 0, 1, 2, 3, 4, and 5. 3,4, and 5     #
# repeat, so we only keep track of the current time and use that information #
# to determine which board we should return                                  #
##############################################################################


def generate_grids(grid):
    all_grids = list()
    has_bomb = record_positions_of_bombs(grid) # returns a sorted list of bomb locations
    all_grids.append(grid)           # initial board
    all_grids.append(grid)          # board at time_step 1 is unchanged
    all_grids.append(fill_with_bombs(grid))     # bomberman plants bombs everywhere
    first_explosion = explode_bombs(fill_with_bombs(grid), has_bomb) # returns board with first explosions
    has_bomb = record_positions_of_bombs(first_explosion) # record where surviving bombs are
    all_grids.append(first_explosion)
    all_grids.append(fill_with_bombs(grid))
    second_explosion = explode_bombs(fill_with_bombs(grid), has_bomb) # record explosion of survivors
    all_grids.append(second_explosion)
    return all_grids

def record_positions_of_bombs(grid):
    has_bomb = list()            # record where bombs were
    # record the positions of the  bombs
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] is "O":
                has_bomb.append((i, j)) # add coordinates as tuple
    has_bomb.sort()
    return has_bomb

def fill_with_bombs(grid):
    all_bombs = list()          # a grid with bombs in every cell
    for i in range(0, len(grid)):
        all_bombs.append(list()) # create row
        for j in range(0, len(grid[0])):
            all_bombs[i].append("O") # fill it with bombs!
    return all_bombs

def explode_bombs(grid, has_bomb):
    new_grid = list(grid)
    while has_bomb:
        coordinate = has_bomb.pop()
        _explode_bomb(new_grid, coordinate)
    return new_grid

def _explode_bomb(grid, coordinate):
    i = coordinate[0]
    j = coordinate[1]
    # _destroy_cell does index bounds checking
    _destroy_cell(grid, i, j)
    _destroy_cell(grid, i+1, j)
    _destroy_cell(grid, i, j+1)
    _destroy_cell(grid, i-1, j)
    _destroy_cell(grid, i, j-1)
        
def _destroy_cell(grid, i, j):
    if _are_legal_indices(grid, i, j):
        grid[i][j] = "."      

def _are_legal_indices(grid, i, j):
    if i >= 0 and i < len(grid):
        if j >= 0 and j < len(grid[i]):
            return True
    return False



def bomberMan(n, grid):
    # Complete this function
    grid = to_matrix(grid)
    all_grids = generate_grids(grid)
    if n == 0:
        return to_string(all_grids[0])
    elif n == 1:
        return to_string(all_grids[1])
    elif n == 2:
        return to_string(all_grids[2])
    elif n == 3:
        return to_string(all_grids[3])
    else:
        # repitition of boards goes as 2 -> 3 -> 2 -> 5 -> 2
        rep = n % 4
        if rep == 1:
            return to_string(all_grids[5])
        if rep == 3:
            return to_string(all_grids[3])
        if rep == 2 or rep == 0:
            return to_string(all_grids[2])

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



