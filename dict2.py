students = {
    "Alice": {"age": 25, "major": "Computer Science", "grades": [90, 85, 88]},
    "Bob": {"age": 23, "major": "Mathematics", "grades": [75, 80, 72]},
    "Charlie": {"age": 22, "major": "Physics", "grades": [92, 88, 95]},
}

totalAge = students["Alice"]["grades"][1]+students["Bob"]["grades"][1]+students["Charlie"]["grades"][1]
print(totalAge)


count = 0
for i in range(2):
    count += students["Alice"]["grades"][i] + students["Bob"]["grades"][i]+students["Charlie"]["grades"][i]

print(count)

print(len(students["Alice"]["grades"]))