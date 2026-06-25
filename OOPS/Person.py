class Person:

    def __init__(self,name, mobile,address):

        self.name=name
        self.mobile=mobile
        self.address=address


p1=Person("Prince Kumar",9559618602,"Bhadohi")

for key,value in p1.__dict__.items():

    print(key, ":", value)