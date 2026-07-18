students=[
    ("Amit",90),
    ("Ravi",900),
    ("Zoya",85),
    ("Meena",60)
]

students.sort(key=lambda student:student[1])

print(students)