class A:
    n=10
    def __init__(self,z,y=5):
        self.zee=z
        self.yee=y
    def disp(self):
        print(self.zee,self.n)
class B(A):
    def __init__(self,m,x,p):
        self.my=m
        A.__init__(self,x,p)
obj=B(10,11,2002)
obj.disp()

#using super method
class A:
    n=10
    def __init__(self,z,y=5):
        self.zee=z
        self.yee=y
    def disp(self):
        print(self.zee,self.n)
class B(A):
    def __init__(self,m,x,p):
        super().__init__(x,p)
        self.my=m
    def p(self):
        print(A.n,super().n)
obj=B(10,15,21)
obj.disp()
obj.p()

#other method
class A:
    def __init__(self,z):
        self.zee=z
class B(A):
    def __init__(self,z,x):
        super().__init__(x)
        self.zee=z
    def p(self):
        print(self.zee,A(12).zee)
obj=B(10,15)
obj.p()
