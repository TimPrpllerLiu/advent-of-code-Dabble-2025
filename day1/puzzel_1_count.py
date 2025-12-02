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
outputlist = []
outputlist2 = []
for index, change in enumerate(inputlist2):
    #print("sum input",sum_val)
#for change in inputlist2:
    sum_val = sum_val + (change % 100)
   # print(index)
    #print(change)
    #print("change",change)
    outputlist2.append(change)
    if sum_val == 0 or sum_val == 100 or sum_val == -100:
        count_zero += 1
        sum_val = 0
        #print(sum_val,index,outputlist[index])
        outputlist.append(sum_val)
        #print(index,change)
    elif sum_val > 100:
        sum_val = sum_val - 100
        outputlist.append(sum_val)
    elif sum_val < 0:
        sum_val = sum_val + 100
        
        outputlist.append(sum_val)
    else:
        outputlist.append(sum_val)
    #print("sum output",sum_val)

print(inputlist2[0:20])
print(outputlist[0:20])
print(outputlist2[0:20])
print(count_zero) #1182


