#create only odd index characters
#hello everyone -- e,l, ,v,r,o,e
list1="hello everyone"
reslist=[]
for i in range(len(list1)):
    if i%2!=0:
        reslist.append(list1[i])
ores=[]
for ch in list1[1::2]:
    ores.append(ch)
print(reslist)
print(ores)
#comprehension
print([list1[i] for i in range(len(list1)) if i%2!=0])
print([ch for ch in list1[1::2]])