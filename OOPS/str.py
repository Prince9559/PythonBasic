class Student:

    def __init__(self,name,marks):

        self.name=name
        self.marks=marks

    def __str__(self):
         return f"{self.name} scored {self.marks}"
    
s1=Student("Raju",90)
print(s1)

         