import csv
file_path = 'day2_input1.txt'
start_list = []
end_list = []
with open(file_path, 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        line_ranges = []
        for item in row:
            if item.strip():
                parts = item.strip().split('-')
                if len(parts) == 2:
                    try:
                            # Convert the start and end strings to integers
                            start = int(parts[0])
                            end = int(parts[1])
                            start_list.append(start)
                            end_list.append(end)
                            line_ranges.append([start,end])                    
                    except ValueError:
                            print(f"Warning: Could not convert a range part to integer: {item}")
                else:
                        print(f"Warning: Skipping item with incorrect format: {item}")

def find_repeat_pattern(inputnumber):
    number_as_string = str(inputnumber)
    digit_count = len(number_as_string)
    max_pattern_length = digit_count // 2
    #print("digit_count",digit_count)
    for pattern_length in range(1, max_pattern_length+1):
        if digit_count % pattern_length == 0:
            #print("pattern_length",pattern_length)
            potential_pattern = number_as_string[0:pattern_length]
            num_repeats = digit_count // pattern_length
            reconstructed_number = potential_pattern * num_repeats
            #print("reconstructed_number",reconstructed_number,"potential_pattern",potential_pattern,"num_repeats",num_repeats)
            if reconstructed_number == number_as_string:
                #print(reconstructed_number)
                return inputnumber
    return 0

    

#print(line_ranges)
print("-" * 50)
repeatnumber_list=[]
for row_index in range(len(start_list)):
    for test_num in range(start_list[row_index],end_list[row_index]):
        repeat_number = find_repeat_pattern(test_num)
        #print(repeat_number)
        #if len(repeatnumber_list) == 100: break
        if (repeat_number != 0) and (repeat_number is not None): 
            repeatnumber_list.append(repeat_number)
            

#print('find patter test',find_repeat_pattern(123123))
#print('find patter test',find_repeat_pattern(2222))
print((repeatnumber_list))
print(sum(repeatnumber_list))








#print(start_list,end_list)