l=156
x = 10
y = x
a=['lukesh','1','kumar','kalam']
a.sort()
if id(x) == id(y):
	print("x and y refer to the same object")
print(id(x))
print(id(l))
print(id(x)-id(l))
print(a)
print(id(a))
#del a
print(a)