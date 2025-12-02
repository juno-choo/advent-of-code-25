with open("input.txt", "r") as f:
    data = f.read().split()

def find(commands):
    cur = 50
    res = 0

    for command in commands:
        direction = command[0]
        distance = int(command[1:])

        cur = cur - distance if direction == 'L' else cur + distance

        cur %= 100
        if cur == 0:
            res += 1

        print(f"Cur pos: {cur}")

    return res

test_data = ['L51', 'L15', 'R16', 'L1']
print(find(data))