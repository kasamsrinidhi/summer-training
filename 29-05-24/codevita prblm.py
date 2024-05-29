'''Some prime numbers can be expressed as a sum of other consecutive prime numbers
For example
5=2+3,
17 = 2 + 3 + 5 + 7
41 = 2 + 3 + 5 + 7 + 11 + 13
Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2.
Write code to find out the number of prime numbers that satisfy the above mentioned property in a given range
Input Format: The first line contains a number N
Output Format: Print the total number of all such prime numbers which are less than or equal to N'''
def isPrime(n):
    if n==0 or n==1:
        return False
    for deno in range(2,int(n**0.5)+1):
        if n%deno==0:
            return False
    return True
n=int(input())
prime=[i for i in range(2,n+1) if isPrime(i)]
print(prime)
count,pSum=0,prime[0]
for p in prime[1:]:
    pSum += p
    if pSum>n:
        break
    if isPrime(pSum):
        count+=1
print(count)
