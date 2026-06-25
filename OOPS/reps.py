class Student:

    def __init__(self,name,marks):
         
         self.name=name
         self.marks=marks

    def __repr__(self):
          
          return f"Student(name='{self.name}', marks={self.marks}) "
    

s1=Student("Amit",89)
print(repr(s1))   
