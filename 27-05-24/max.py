n=int(input())
nest=[list(map(int,input().split())) for i in range(n)]
maxIn,tSum=0,0
for index,data in enumerate(nest):
    if tSum<sum(data):
        tSum=sum(data)
        maxIn=index
print(maxIn)