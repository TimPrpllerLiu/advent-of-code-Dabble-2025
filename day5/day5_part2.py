file_path_fresh_range = 'Fresh_range.txt'
#file_path_fresh_range = 'checklist.txt'
start_list = []
end_list = []
with open(file_path_fresh_range, 'r') as file2:
    file_path_fresh_range = [line.strip() for line in file2.readlines()]
    food_ranges = []
    for row in file_path_fresh_range:

        #print(type(row),row)
        
        parts = row.split('-')
        #print(type(parts),parts)
        if len(parts) == 2:
            try:
                # Convert the start and end strings to integers
                start = int(parts[0])
                end = int(parts[1])
                start_list.append(start)
                end_list.append(end)
                food_ranges.append([start,end])                    
            except ValueError:
                print(f"Warning: Could not convert a range part to integer: {item}")
        else:
                print(f"Warning: Skipping item with incorrect format: {item}")

def merge_ranges(ranges):
    if not ranges:
        return []

    # 1. Sort the ranges by their start time
    ranges.sort(key=lambda r: r[0])

    
    merged = []
    current_start, current_end = ranges[0]

    for next_start, next_end in ranges[1:]:
        # Check for overlap: If the next range starts before or at the current merged range's end
        if next_start <= current_end:
            # Overlap/Contiguous: Extend the end of the current merged range
            current_end = max(current_end, next_end)
        else:
            # No Overlap: Finalize the current merged range and start a new one
            merged.append([current_start, current_end])
            current_start, current_end = next_start, next_end

    # Add the last merged range
    merged.append([current_start, current_end])
    return merged

merge_list = merge_ranges(food_ranges)
merge_lengths = [r[1]-r[0]+1 for r in merge_list] # THIS part! need to add 1 more number since 3,4,5 are all valid rather than 5-3 = 2.
food_ranges.sort(key=lambda r: r[0])
print('origina',food_ranges[0:4])
print("mergelist",merge_list[0:4])
print("merge legnths",merge_lengths[0:3])
print(sum(merge_lengths))
    


