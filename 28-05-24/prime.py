#check the number is prime or not
n=int(input())
#1st logic
count=0
for deno in range(1,n+1):
    if n % deno == 0:
        count+=1
if count==2:
    print("prime")
else:
    print("not prime")
#2 O(n),O(1)
for deno in range(2,n):
    if n % deno == 0:
        print("not prime")
        break
else:
    print("prime")
#3
for deno in range(2,(n//2)+1):
    if n % deno == 0:
        print("not prime")
        break
else:
    print("prime")
#4 sqrt(n))
for deno in range(2,int(n**0.5)+1):
    if n % deno == 0:
        print("not prime")
        break
else:
    print("prime")