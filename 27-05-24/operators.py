ex=['',[],(),{},False,0,1]
print(any(ex))
n=[1,2,3]
print(n*2)
#list comprehension
lst=[x ** 2 for x in range(1,11) if x%2==0]
print(lst)
cube=[i*i*i for i in range(1,6)]
print(cube)
cube=[i*i*i for i in range(1,6) if i*i*i % 2 ==0]
print(cube)