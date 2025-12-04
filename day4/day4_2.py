with open("input.txt", "r") as f:
    grid = f.read().split()

# grid = ["@.@.@",
#         "@.@.@",
#         ".@@@@",
#         "@@.@."]

grid = [list(s) for s in grid]
ROWS = len(grid)
COLS = len(grid[0])

def search(grid, totalRemoved, removedInSearch):
    toRemove = []
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == '@' and valid(grid, row, col):
                toRemove.append((row, col))

    for row, col in toRemove:
        grid[row][col] = '.'
        totalRemoved += 1
        removedInSearch += 1

    if removedInSearch == 0:
        print(f"Total removed: {totalRemoved}")
        return totalRemoved
    else:
        print(f"Removed {removedInSearch} rolls this time.")
        search(grid, totalRemoved, 0)

def valid(grid, r, c):
    directions = [(0,1), (1,0), (1,1), (1,-1), (-1,1), (-1,0), (0,-1), (-1,-1)]
    neighbors = 0

    for dr, dc in directions:
        if (dr + r) >= 0 and (dr + r) < ROWS and (dc + c) >= 0 and (dc + c) < COLS and grid[dr + r][dc + c] == '@':
            neighbors += 1
    
    return neighbors < 4

# 9 
# ["x.x.x",
 # "x.@.x",
 # ".@@@x",
 # "xx.x."]

print(search(grid, 0, 0))
