'''Given a binary array nums, return the maximum number of consecutive 1's in the array
 """ Inputs: nums=[1,1,0,1,1,1]
             nums=[1,0,1,1,0,1]

     Outputs: 3
              2'''
b=list=list(map(int,input().split()))
count,maxVal=0,0
for i in b:
    if i==1:
        count+=1
        if count > maxVal:
            maxVal=count
    else:
        count=0
print(maxVal)
    