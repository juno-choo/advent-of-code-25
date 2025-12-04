with open("day3.txt", "r") as f:
    day3Data = f.read().split()

def findTotalJoltage(banks):
    total = 0
    for bank in banks:
        total += findJoltage(bank)
        print(f"Cur tota: {total}")
    print(f"Total joltage: {total}")

def findJoltage(row):
    stack = [row[0]]
    dropsLeft = len(row) - 12

    for i in range(1, len(row)):
        while dropsLeft and stack and int(row[i]) > int(stack[-1]):
            stack.pop()
            dropsLeft -= 1
        stack.append(row[i])

    return int(''.join(stack[0:12]))

test = '123456789012345678901234567890'  
# 991234567890
print(findTotalJoltage(day3Data))