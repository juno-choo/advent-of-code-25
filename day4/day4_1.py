with open("input.txt", "r") as f:
    grid = f.read().split()

test = ["@.@.@",
        "@.@.@",
        ".@@@@",
        "@@.@."]

ROWS = len(grid)
COLS = len(grid[0])
def search(grid):
    total = 0

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == '@' and valid(row, col):
                total += 1

    print(f"Total: {total}")

def valid(r, c):
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

print(search(grid))
