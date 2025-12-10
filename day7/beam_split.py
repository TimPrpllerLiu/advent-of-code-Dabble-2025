import math

file_path = "input_tree.txt"
#file_path = "sample2.txt"
with open(file_path, 'r') as file:
    star_line = [line.strip() for line in file.readlines()]
    print(len(star_line[0]),type(star_line))

def update_symbol(position,above,left,right,below):
    if position == '.':
        if (above == 'S' or above == '|'):
            new_position = '|'
        elif right == '^' or left == '^':
            new_position = '|'
        else:
            new_position = '.'
        caret_number = 0
        caret_remove_number = 0
        return caret_number, caret_remove_number, new_position
    elif position == 'S':
        new_position = 'S'
        caret_number = 0
        caret_remove_number = 0
        return caret_number, caret_remove_number, new_position
    elif position == '^':
        caret_number = 0
        caret_remove_number = 0
        
        #print(f"DEBUG: Pos=^, Above='{above}', Left='{left}'")
        if above == '|' and left == '|':
            caret_number = 1
            #print('SUCCESS: Caret Found!')
        elif above == '.' and left == '|':
            caret_remove_number = 1
            #print('SUCCESS2: Caret Found!')
        new_position = '^'
        return caret_number, caret_remove_number, new_position
    else:
        return 0, 0, position

row_len = len(star_line)
col_len = len(star_line[0])
caret_number = 0
caret_remove_number = 0

next_star_line = list(star_line)

for row_index,row in enumerate(star_line):
    next_row_string = row
    for col in range(col_len):
        position_pattern = row[col]
        if row_index == 0:
            above = None
        else:
            above = next_star_line[row_index - 1][col]
        if col == 0:
            left = None
        else:
            left = next_row_string[col - 1]
        if col == col_len-1:
            right = None
        else:
            right = next_row_string[col+1]
        if row_index == row_len -1:
            below = None
        else:
            below = star_line[row_index+1][col]
        #if row_index == 4 and col == 69:
            #print(position_pattern,above,left,right,below)
        caret_number_new,caret_remove_number_new, updated_position = update_symbol(position_pattern,above,left,right,below)
        
        caret_number += caret_number_new
        caret_remove_number += caret_remove_number_new
        #if row_index == 3 and 65 < col < 75:
           # print(updated_position)
        if updated_position != position_pattern:
            next_row_string = next_row_string[:col] + updated_position + next_row_string[col + 1:]
    next_star_line[row_index] = next_row_string

star_line = next_star_line
#print(star_line)
print('caret_number of actual splitter',caret_number,'caret_remove_number',caret_remove_number)


with open("output.txt", "w") as f:
    for item in star_line:
        f.write(item + "\n")
