student={
    "name":"Alok",
    "math":90,
    "science":90
}

print(student["math"])

student["english"]=89
student["math"]=90

print(student.get("history","Not found"))

for key, value in student.items():
    print(key,"=",value)