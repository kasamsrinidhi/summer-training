class Demo:
    def __init__(self):
        self.a=1
        self._b=1
    def display(self):
        return self._b
obj=Demo()
print(obj.__b)
#o/p error