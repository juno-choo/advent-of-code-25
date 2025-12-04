with open("day3.txt", "r") as f:
    day3Data = f.read().split()

def findTotalJoltage(banks):
    total = 0
    for bank in banks:
        total += findJoltage(bank)
        print(f"Cur tota: {total}")
    print(f"Total joltage: {total}")

def findJoltage(row):
    firstDigit = 0

    for i in range(len(row) - 1):
        if int(row[i]) > firstDigit:
            firstDigit = int(row[i])
            secondDigit = int(row[i+1])
            for j in range(i + 2, len(row)):
                secondDigit = max(secondDigit, int(row[j]))
                
    print(f"maxJoltage in bank: {firstDigit * 10 + secondDigit}")
    return (firstDigit * 10) + secondDigit
    

test = ['1119', '19009']   
# 19 + 99 = 811
print(findTotalJoltage(day3Data))