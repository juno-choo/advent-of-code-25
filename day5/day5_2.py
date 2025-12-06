import os

script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, "data1.txt"), "r") as f:
    raw_intervals = f.read().split()

def count_optimized(raw_intervals):
    # 1. Parse 
    parsed = []
    for i in raw_intervals:
        start, end = i.split('-')
        parsed.append((int(start), int(end)))
    
    # 2. Sort by start time
    parsed.sort()

    merged = []
    
    # 3. Merge Overlaps
    for current_start, current_end in parsed:
        if not merged:
            merged.append([current_start, current_end])
        else:
            # Get the last interval we added
            last_start, last_end = merged[-1]
            
            # Check for overlap
            # If current start is less than last end, they overlap
            if current_start <= last_end: 
                # Merge them by taking the maximum end point
                merged[-1][1] = max(last_end, current_end)
            else:
                # No overlap, just add it to the list
                merged.append([current_start, current_end])

    # 4. Calculate total length
    total_count = 0
    for start, end in merged:
        total_count += (end - start + 1)
        
    return total_count

print(count_optimized(raw_intervals))