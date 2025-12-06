import math
file_path = 'Cephalopod_math.txt'
with open(file_path,'r') as file:
    all_lines = file.readlines()
    #print((all_lines[0][0:10]))
    # use list comprehension to try convert the lines into list!! Very powerful way
    raw_sign_line = [sign for sign in all_lines[len(all_lines)-1].strip().split(' ') if sign in ('+', '*')]
    raw_num_lines = []
    for line in all_lines[0:len(all_lines)-1]:
        numbers = [int(num) for num in line.strip().split(' ') if num] # Expression + iteration + Condition for which to keep
        raw_num_lines.append(numbers)
    #print(type(raw_num_lines), type(raw_num_lines[0]),len(raw_sign_line),type(raw_sign_line))
# now after read all as list, we can do column work easier
Grand_total = 0
#print([row[0] for row in raw_num_lines]) 
#print(raw_sign_line[0])
for col in range(len(raw_sign_line)):
    column_value = 0
    column_list = [row[col] for row in raw_num_lines]
    #print('first sign',raw_sign_line[col])
    if raw_sign_line[col] == '+':
        column_value = sum(column_list)
    elif raw_sign_line[col] == '*':
        column_value = math.prod(column_list)
    else:
        print("something wrong with the sign read in")
        break
    Grand_total = Grand_total + column_value

print(Grand_total)
