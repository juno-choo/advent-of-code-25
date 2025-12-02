with open("input.txt", "r") as f:
    data = f.read().split(',')

def addInvalids(listOfRanges):
    totalInvalids = 0

    for eachRange in listOfRanges:
        separated = eachRange.split('-') # ['100', '9999']
        totalInvalids += checkRepeat(separated[0], separated[1])
        print(f"Cur total: {totalInvalids}")
    print(f"Total invalids: {totalInvalids}")

def checkRepeat(start, end):
    sumOfInvalids = 0
    # Check each num in range
    for i in range(int(start), int(end) + 1):
        num = str(i)
        n = len(num)
        # Check only if places are even
        if n % 2 == 0:
            # If firstHalf equals secondHalf of string, it is invalid
            half = n // 2
            if num[0:half] == num[half:]:
                sumOfInvalids += int(num)
                print(f"{num} is invalid")
    return sumOfInvalids

test_range = ['10-15', '21-23', '99999-100100', '87-89']
s = '10'
e = '23'
print(addInvalids(data))