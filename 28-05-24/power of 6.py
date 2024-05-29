#power of 6
#given an int n,return true if it is a power of 6.otherwise return false
#an int n is a power of 6,if there exists an int x such that n==6^x
#ex:input :36 output:true
#ex:input 22 o/p:false
n=int(input())
while n!=1:
    if n%6==0:
        n//=6
    else:
        print("false")
        break
else:
    print("true")