#Write a Python function that takes a string as input and returns a dictionary where:

#Each key is a character from the string (excluding spaces), and
#The corresponding value is the number of times that character appears in the string.



input_string = "hello world"
list1 = []
remDup = []
dict1 = {}

for i in range(len(input_string)):
    if input_string[i] != ' ':
        list1.append(input_string[i])
        if input_string[i] not in remDup:
            remDup.append(input_string[i])

for i in range(len(remDup)):
    count = 0
    for j in range(len(list1)) :
        if remDup[i] == list1[j]:
            count +=1
    dict1[remDup[i]]=count

print(dict1)