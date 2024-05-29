class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return 1
    def __eq__(self,other):
        return self.x*self.y==other.x*other.y
ob1=A(5,2)
ob2=A(2,5)
print(ob1==ob2)