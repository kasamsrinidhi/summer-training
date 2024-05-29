#double ended key
from collections import deque
data=input()
qStr=deque(data)
rot=int(input())
res=""
for i in range(rot):
    di,mag=input().split()
    if di== 'l' or di== 'L':
        qStr.rotate(-int(mag))
        res += qStr[0]
    elif di== 'r' or di== 'R':
        qStr.rotate(int(mag))
        res += qStr[0]
subList = [data[i:i+rot] for i in range(0,len(data)-rot+1)]
#Anagram:
for subele in subList:
    if sorted(subele)==sorted(res):
        print("Yes")
        break
else:
    print("No")

    