with open("input.txt", "r") as f:
    data = f.read().split()

import math
def find(commands):
    cur = 50
    res = 0
    print(f"First pos: {cur}")
    for command in commands:
        direction = command[0]
        distance = int(command[1:])

        step = 1 if direction == 'L' else -1
        for _ in range(distance):
            cur += step
            cur %= 100

            if cur == 0:
                res += 1
                
        print(f"Cur pos: {cur}")
    return res

test_data = ['L49', 'L102'] # 2
print(find(data)) 