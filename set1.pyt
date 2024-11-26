list1 = [1, 2, 3, 4, 5, 6,1,1,1,1,1]
set1= set(list1)

print(set1)

for i in set1:
    print(i)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3=set1.union(set2)
print(set3)

print(set3.intersection(set1))
set3 = set1|set2
print(set3)

set3.add("LUkesh")
print(set3)
for i in set3:
    print(i)

set3.remove(2)