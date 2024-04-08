import math
import random as r

GRID_SIZE = 5
sel = int((GRID_SIZE**2 - 1)/2)

def create_grid():
    o = [0] * (GRID_SIZE**2)
    o[int((GRID_SIZE**2 - 1)/2)] = 3
    return o

grid = create_grid()

def print_grid(g = grid):
    #Prints grid to console followed by a spacer
    for i in range(GRID_SIZE):
        add = GRID_SIZE * i
        for j in range(GRID_SIZE-1):
            print(g[j+add], end=" ")
        print(g[GRID_SIZE-1+add])
    print("-----")

def generate_cell():
    perimeter = 4*(GRID_SIZE-1)-1
    o = r.randint(0, perimeter)
    #Generates key point in outer edge of grid
    if o > GRID_SIZE:
        #Bottom Row
        if o >= perimeter-GRID_SIZE:
            o += (GRID_SIZE*(GRID_SIZE-4) + 4)
        else:
            #Sides
            ref = o - GRID_SIZE
            o += int(math.ceil(ref/2))*(GRID_SIZE-2)
            
    if grid[o] == 0:
        grid[o] = 2
    else:
        #Chooses a different cell if chosen cell is filled
        generate_cell()

def key_points(n):
    for i in range(n):
        generate_cell()
    return n, grid

def grow_tile(s):
    #Choose Movement Direction
    grow = r.randint(0, 3)
    if grow == 0 and s%GRID_SIZE != 0:
        #Left
        s -= 1
    elif grow == 1 and s >= GRID_SIZE:
        #Up
        s -= 5
    elif grow == 2 and s%GRID_SIZE != GRID_SIZE-1:
        #Right
        s += 1
    elif grow == 3 and s < GRID_SIZE*(GRID_SIZE-1):
        #Down
        s += 5
    else:
        #Chooses a different direction if chosen direction is blocked
        return sel, True
    
    if grid[s] == 0 or grid[s] == 1:
        #Places island on empty grid squares when the path crosses over
        grid[s] = 1
    elif grid[s] == 2:
        #Marks the path complete when touching key point
        grid[s] = 4
        return s, False

    return s, True

def build_path(n):
    for i in range(n):
        growing = True
        sel = int((GRID_SIZE**2 - 1)/2)
        while growing:
            sel, growing = grow_tile(sel)

def main():
    k, g = key_points(int(input("Points: ")))
    build_path(k)
    print_grid()

main()
