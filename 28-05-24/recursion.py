#recursion
def greet(n):
    if n<=0:
        return
    print("hello")
    greet(n-1)
greet(2)
#5 4 3 2 1
def num(n):
    if n<=0:
        return
    print(n,end=" ")
    num(n-1)
num(5)
#1 2 3 4 5
def num(n):
    if n<=0:
        return
    num(n-1)
    print(n,end=" ")
num(5)