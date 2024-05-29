#prgrm to get a list,sorted in increasing order by the last elmt in each tuple from a given list of non-empty tuples
#i/p:[(2,5),(1,2),(4,4),(2,3),(2,1)]
#o/p:[(2,1),(1,2),(2,3),(4,4),(2,5)]
def end(t):
    return t[-1]
n=int(input())
data=[tuple(map(int,input().split()))for i in range(n)]
print(data)
a=sorted(data,key=end)
print(a)
