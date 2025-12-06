file_path_food = 'food_list.txt'
file_path_fresh_range = 'Fresh_range.txt'
with open(file_path_food, 'r') as file:
    food_list = [line.strip() for line in file.readlines()]
    #print(f"food_list {type(food_list)} type {len(food_list)} {food_list[0]}")
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
        
    print(f"file_path_fresh_range {type(food_ranges)} {len(food_ranges)} {food_ranges[0:3]}")


def check_number_in_multiple_ranges(number, ranges_list):
    """
    Checks if a single number is within ANY range in the list of [min, max] pairs.
    """
    for min_val, max_val in ranges_list:
        # Use the fast, clear, chained comparison
        if min_val <= number <= max_val:
            return True      
    return False

count_id = 0
for item in food_list:
    if check_number_in_multiple_ranges(int(item), food_ranges):
        count_id += 1
print(f"Total id free is {count_id}")
