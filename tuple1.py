tuple1 = ('lukesh','kumar',1,'kumar')
print(tuple1)

print(tuple1[1])
print(tuple1[::])
print(len(tuple1))

list2 = list(tuple1)
list2.append("Kalam")
tuple1=tuple(list2)
print(tuple1)
#del tuple1  Delete 
print(tuple1)

banana,green,*red = tuple1
print("banana ", banana)
print(green)
print(red)