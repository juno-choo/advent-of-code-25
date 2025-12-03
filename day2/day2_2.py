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
        
        # Check groups of 1,2,3... n//2
        for k in range(1, n//2 + 1):
            # Check if k is a factor of n, it might be 3 * '3's with n = 3, or 2 * '123's with n = 6
            if n % k == 0:
                subStr, repeats = num[0:k], n // k
                if subStr * repeats == num:
                    sumOfInvalids += int(num)
                    print(f"Invalid num: {num}")
                    break
            
    return sumOfInvalids

test_range = ['123123-124125', '21-23', '887-888', '2526-2828']
s = '10'
e = '23'
print(addInvalids(data))