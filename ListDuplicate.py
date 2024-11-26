#Write a Python function that takes a list of integers as input and returns a 
# new list containing only the elements that appear more than once in the original list. 
# The result list should not have duplicates and should be sorted in ascending order.

list1 = [4, 5, 6, 4, 7, 5, 8, 9]
remDup,output = [],[]

count =0

for i in range(len(list1)):
    if list1[i] not in remDup:
        remDup.append(list1[i])

print(remDup)

for i in range(len(remDup)):
    count = 0
    for j in range(len(list1)) :
        if remDup[i] == list1[j] :
            count += 1
    if count>1 :
        output.append(remDup[i])

print(output)