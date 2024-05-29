#remove all consecutive duplicates from a given string
#i/p:abbcsa o/p:abcsa
data=input()
res=data[0]
k=0
for i in range(1,len(data)):
    if data[i]!=res[k]:
        res+=data[i]
        k+=1
print(res)