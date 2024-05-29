#input a list and sort the elements in the list based on its length
#i/p:hi 1 425 2104  o/p:['1','hi','425',2104']
# n=input().split()
# print(sorted(n,key=len))
print(sorted(input().split(),key=len))