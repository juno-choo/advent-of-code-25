with open("input.txt", "r") as f:
    data = f.read().split(',')

def countInvalid(listOfRanges):
    invalid = 0

    for eachRange in listOfRanges:
        separated = eachRange.split('-') # ['100', '9999']
        invalid += checkRepeat(separated[0], separated[1])
        print(invalid)
    print(f"Total invalid: {invalid}")
    return invalid

def checkRepeat(start, end):
    invalid = 0 
    # Check each num in range
    for i in range(int(start), int(end) + 1):
        num = str(i)
        n = len(num)
        # Check only if places are even
        if n % 2 == 0:
            # If firstHalf equals secondHalf of string, it is invalid
            half = n // 2
            if num[0:half] == num[half:]:
                invalid += 1
                print(f"1st half: {num[0:half]}, 2nd: {num[half:]}")
    return invalid 

test_range = ['10-15', '21-23', '99999-100100', '87-89']
s = '10'
e = '23'
print(countInvalid(test_range))