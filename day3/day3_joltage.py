file_path = "joltage_battery_banks.txt"
with open(file_path, 'r') as file:
    input_list = [line.strip() for line in file.readlines()]
    
print("input list",len(input_list))

def find_top2_sort(number_string):
    digit_list = list(number_string)
    largest_num = max(digit_list)
    #print(largest_num)
    largest_count = digit_list.count(largest_num)

    if largest_count >= 2:
        return (int(largest_num)*10 + int(largest_num))
    elif largest_count == 1:
        if largest_num == digit_list[-1]: # when last digit is largest
            digit_B = int(largest_num)
            new_list = digit_list[0:-1]
            digit_A = int(max(new_list))

        else: # when largest number is not the last digit, then remove the numbers ahead and find the largest in the rest
            digit_A = int(largest_num)
            index_A = number_string.index(str(largest_num))
            new_list = digit_list[index_A+1:]
            digit_B = int(max(new_list))
        return digit_A*10+digit_B

Joltage_list = []
for row in input_list:
    joltage = find_top2_sort(row)
    Joltage_list.append(joltage)
print(Joltage_list)
print('output Joltage length is ', len(Joltage_list))
print('Sum of Joltage is ', sum(Joltage_list))