import math
file_path = 'Cephalopod_math.txt'
with open(file_path,'r') as file:
    all_lines = file.readlines()
    raw_sign_line = [sign for sign in all_lines[len(all_lines)-1].strip().split(' ') if sign in ('+', '*')]
    character_lists = []
    for line in all_lines[0:len(all_lines)-1]:
        cleaned_line = line.strip()
        character_list = list(cleaned_line)
        character_lists.append(character_list)
    print(len(character_lists),(character_lists[0][0]),(character_lists[1][0]),(character_lists[2][0]),(character_lists[3][0]))
    number_row = len(character_lists)
    number_col = len(character_lists[0])
    print(number_row,number_col)

final_numbers = 0
forward_sign = 0
current_vertical_digits=[]
for col_index in range(number_col):
    current_column = []
    print(f"--- Processing Column Index: {col_index} ---")
    for row_index in range(number_row):
        character = character_lists[row_index][col_index]
        current_column.append(character)
        #print('crrentcolum',current_column)
    #f col_index == 13:
        #break
    if all(char == ' ' for char in current_column):
        #print('all char == empy')
        if raw_sign_line[forward_sign] == "+":
            line_result = sum(current_vertical_digits)
            print('sum value',raw_sign_line[forward_sign],forward_sign)
            #print('final number',final_numbers)
        elif raw_sign_line[forward_sign] == "*":
            line_result = math.prod(current_vertical_digits)
            print('multip value',raw_sign_line[forward_sign],forward_sign)
            #print('final number',final_numbers)
        forward_sign += 1
        final_numbers += line_result
        current_column = []
        current_vertical_digits = []
    else:
        col_digits = [char for char in current_column if char != ' ']
        number_str = "".join((col_digits))
        #print('number_str',number_str)
        current_vertical_digits.append(int(number_str))


    print('digi join',current_vertical_digits)
    print('number',forward_sign)
    print('final number',final_numbers)
    
if current_vertical_digits:
    if raw_sign_line[forward_sign] == "+":
            line_result = sum(current_vertical_digits)
            print('sum value',raw_sign_line[forward_sign],forward_sign)
            #print('final number',final_numbers)
    elif raw_sign_line[forward_sign] == "*":
            line_result = math.prod(current_vertical_digits)
            print('multip value',raw_sign_line[forward_sign],forward_sign)
final_numbers += line_result
print('last last add',final_numbers) # has to run the last column separately due to it only reached to 998, not 999.










