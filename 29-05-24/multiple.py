class Parent():
    def f1(self):
        print("f1 fn")
class Parent2():
    def f2(self):
        print("f2 fn")
class Child(Parent,Parent2):
    def f3(self):
        print("this is")
ob=Child()
ob.f1()
ob.f2()
ob.f3()