#write a python program to remove an element form specified index.
myData = tuple(input().split())
i = int(input())
inList = list(myData)
inList.pop(i)
print(tuple(inList))
print(myData[:i] + myData[i+1:])