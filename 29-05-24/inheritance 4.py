class A:
    def __init__(self,x=3):
        self._x=x
class B(A):
    def __init__(self):
        super().__init__(5)
    def disp(self):
        print(self._x)
def main():
    obj=B()
    obj.disp()
main()