#wipro
#prgrm to sort first half in ascending order & second order in descending order in an array
#i/p:1 21 5 2 50 16
#o/p:1 2 5 50 21 16
n=list(map(int,input().split()))
n1=len(n)
res=sorted(n)[:n1//2]
print(res)
res +=sorted(n,reverse=True)[:n1//2]
print(res)