import os

script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, "data1.txt"), "r") as f:
    raw_intervals = f.read().split()
    intervals = []
    for i in raw_intervals:
        start, end = i.split('-')
        intervals.append((int(start), int(end)))

with open(os.path.join(script_dir, "data2.txt"), "r") as f:
    checks = f.read().split()

def find(intervals, checks):
    good = 0
    
    for c in checks:
        val = int(c)
        found_match = False

        for start, end in intervals:
            if start <= val <= end:
                found_match = True
                break 
        
        if found_match:
            good += 1

    return good

print(find(intervals, checks))