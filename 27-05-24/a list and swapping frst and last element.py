#Read a list and swap first elementnd last element in the list:
#print the list swapping first value and last value in the list
a=input().split()
a[0],a[-1]=a[-1],a[0]
print(a)