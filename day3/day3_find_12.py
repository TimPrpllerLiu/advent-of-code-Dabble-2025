file_path = "joltage_battery_banks.txt"
with open(file_path, 'r') as file:
    input_list = [line.strip() for line in file.readlines()]
    
print("input list",len(input_list))
# this task will find 12 digits, which is peak for regional so can construct the largest voltage.
# I think it should be from 1:88 find the largest as the first, then from this largest index to 89 to find the second digit and so on

def find_12_joltage(number_string):
    digit_list = list(number_string)
    START_index = 89
    END_index = 100
    tempJoltage = ''
    index_found = 0
    for i in range(START_index,END_index+1):
        current_slice = digit_list[index_found:i]
        #print('type slice',index_found,i)
        index_found_new,digit_find = find_the_first_largest(index_found,i,digit_list)
        index_found = index_found_new+1
        #print("index_found new",index_found,index_found_new,digit_find)
        #print(type(tempJoltage),tempJoltage,digit_find)
        tempJoltage = tempJoltage + digit_find
    return tempJoltage
    
def find_the_first_largest(index_slice,end_slice,full_list): #the dynamic slice should use the full list as reference to find the index
    data_list_slicd = full_list[index_slice:end_slice]
    #print(data_list_slicd)
    largest_value = max(data_list_slicd)
    first_index = data_list_slicd.index(largest_value)
    update_index = int(index_slice)+int(first_index)
    #print('firstindex',type(first_index),first_index,largest_value,len(data_list_slicd))     
    return update_index,largest_value

Joltage_list = []
count_tmp = 1
for row in input_list:
    #print('inputlistypte',type(input_list[0]))
    joltage = find_12_joltage(row)
    Joltage_list.append(int(joltage))
    #if count_tmp == 2:
    #    break
print(Joltage_list)
print('output Joltage length is ', len(Joltage_list))
print('Sum of Joltage is ', sum(Joltage_list))