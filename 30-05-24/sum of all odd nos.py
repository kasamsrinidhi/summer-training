#prgrm to print sum of all odd nos present in a larger no.
#34468778445566
#o/p:27
n=int(input())
totSum=0
while n!=0:
    rem=n%10
    if rem%2!=0:
        totSum+=rem
    n//=10
print(totSum)#space complexity-12 bytes time complexity- O(n)

#2nd logic
n2=input()
#odd=['1','3','5','7','9']
odd="13579"
totsum=0
for i in n2:
    #if i in odd:
    if i in odd:
        totsum+=int(i)
print(totsum)#space complexity time complexity- O(n)