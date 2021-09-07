# Removing element and pushing element at a sametime from the list quickly
from collections import deque
d=deque()
h=deque()
d.append("lukesh")
d.append("kumar")
d.append(1)
print(d)

d.rotate(-1)
print(d)
d.appendleft("kumar")
print(d)
d.append('1')
print(d)
print(list(reversed(d)))
d.extendleft(d)
print(d)
print(id(d[1]))