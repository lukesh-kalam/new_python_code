print("Hello Lukesh Kumar")
x,y = 45,98

d = 'lukeshKumar'
if 'lukesh' in d:
    print("Yes")

print(type(d))
tip = str(type(d))

if 'str' in tip:
    print("This is a string")



# List 

list1= ["kalam","lukesh","lukesh","kumar"]

print(list1)
print(list1.pop())
list1.append("Devansh")
print(list1)
print(list1.count("lukesh"))

if "lukesh" in list1:
    print("Lukesh string is present in the list ")
list1.insert(2,"Srinivas")
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)

print(len(list1))
print(list1[2:4])

print(list1[::])
print(list1[::3])
list1.remove("lukesh")

print("Sort  List ")
list1.sort()
print(list1)

list1.sort(reverse=True)
list1.pop(2)
print(list1)



