#remove duplicates from a list
#i/p: 1 4 2 5 5 3 4 7 o/p:[1,4,2,5,3,7]
n=list(map(int,input().split()))
#print(list(set(n)))
#ulist=list(set(n))
#print(ulist)
reslist=[]
for i in n:
    if i not in reslist:
        reslist.append(i)
print(reslist)