class Person:

    def __init__(self,name,email,mobile):

        self.name=name
        self.email=email
        self.mobile=mobile

p1=Person("Piyush","piyush34@gmail.com",9559890988)

for key,value in p1.__dict__.items():
    print(key, ":", value)
         