class Money:

    def __init__(self,amount):
        self.amount=amount

    def __add__(self, other):
         return Money(self.amount + other)    

m1=Money(100)
m2=Money(300)

print(m1+m2)
         