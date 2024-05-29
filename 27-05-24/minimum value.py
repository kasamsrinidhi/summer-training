'''Given two arrays, A and B, of wqual size n, the task is to find the minimum value of A[0]*B[0]+A[1]*B[1]+......+A[n-1]*B[n-1].Shuffling of arrays A and B is alowed
Examples: IP: A[]={3,1,1} and B={6,5,4}
OP: 23
IP: A[]={6,1,9,5,4} and B=[]={3,4,8,2,4}
OP:80'''
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
res=0
b=sorted(b)[::-1] #b=sorted(b).reverse()
for i in range(len(a)):
    res += a[i]*b[i]
print(res)
