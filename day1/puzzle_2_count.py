file_path = 'input.txt'

with open(file_path, 'r') as file:
    input_list = file.readlines()
    inputlist2 = []
for i in range(0,len(input_list)):
    if input_list[i][0] == 'L':
        inputlist2.append(-int(input_list[i][1:]))
    if input_list[i][0] == 'R':
        inputlist2.append(int(input_list[i][1:]))
sum_val = 50
count_zero = 0
count_integer = 0
pass_0_count = 0
outputlist = []
outputlist2 = []

current_sum = 50 # S (Starting point for the rotation)
zero_crossing_count = 0 # This will be the new password
print(f"{'index':5} | change | current_sum    | new_sum_val  |           crossings   | Point 0")
print("-" * 50)
for index, change in enumerate(inputlist2):
    
    new_sum_val = current_sum + change
    # Calculate the number of 100-unit boundaries crossed (including landing on 0/100/etc.)
    # This formula is robust for both positive and negative changes.
    # It gives the total number of multiples of 100 encountered during the rotation.
    crossings = abs((new_sum_val // 100) - (current_sum // 100))
    if current_sum == 0 and change<0: # negative rounding has extra count, need to take it out when it just returned to 0
        crossings -=1

    zero_crossing_count += crossings

    # Update the current_sum to the new dial position (0-99)
    # The modulo operator (%) handles the reduction for both positive and negative numbers.
    current_sum = new_sum_val % 100
    if (new_sum_val > 0 and new_sum_val%100 == 0 and current_sum ==0): # positive count has extra when it is not 0! different as negative case that need to take out
        if crossings > 0:
            crossings -= 1
            zero_crossing_count -=1
            count_integer+=1
    
            
    point_at_0 = 0
    if current_sum == 0:
        point_at_0 = 1
        pass_0_count +=1
    outputlist.append(crossings)
    # troubleshooting:
    if  110<=index<= 121:
        print(f"{index:5} | {change:6} | {current_sum:15} | {new_sum_val:11} | {crossings:27} | {point_at_0:5}| {pass_0_count:10}")
    
#print(count_integer)

file_name = 'crossings_list.txt'
string_list = [str(x) for x in outputlist]
with open(file_name, 'w') as file:
    file.write('\n'.join(string_list))

print(f"List saved successfully to {file_name}")

print(zero_crossing_count)
print(pass_0_count)
print(pass_0_count+zero_crossing_count)
