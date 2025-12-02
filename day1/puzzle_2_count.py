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
Integer_division = 0
count_integer = 0
pass_0_count = 0
outputlist = []
outputlist2 = []
for index, change in enumerate(inputlist2):
    sum_val = sum_val + (change+int(change/100)*100)
    Integer_division = abs(change) // 100
    count_integer = 0
    count_integer = count_integer + Integer_division
    pass_0_count = count_integer + pass_0_count
    outputlist2.append(change)
    if index < 10:
        print(sum_val, (change+int(change/100)*100))
    if sum_val == 0 or sum_val == 100 or sum_val == -100:
        count_zero += 1
        sum_val = 0
        #print(sum_val,index,outputlist[index])
        outputlist.append(sum_val)
        #print(index,change)
    elif sum_val > 100:
        sum_val = sum_val - 100
        pass_0_count += 1
        outputlist.append(sum_val)
    elif sum_val < 0:
        sum_val = sum_val + 100
        pass_0_count += 1
        outputlist.append(sum_val)
    else:
        outputlist.append(sum_val)
    if pass_0_count != 0 and index < 5:
        print(index, change, sum_val,inputlist2[index],outputlist[index],count_integer, pass_0_count,Integer_division)
    #print("sum output",sum_val)

print(inputlist2[0:20])
print(outputlist[0:20])
print(pass_0_count)
print(count_zero)


