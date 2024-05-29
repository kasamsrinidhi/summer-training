class Person:
    def __init__(self,name):#constructor
        self.name=name
    def say_hi(self):#method
        print("hello!!!!!my name is",self.name)
p=Person("srinidhi")#p is reference obj and person() is actual obj
p.say_hi()