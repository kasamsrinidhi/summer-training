#given an integer n, return all the numbers in the range {1, n} sorted in lexo graphical order
#you must write an algorithm that runs in 0(n) tme and uses 0(1) extra space.
#input: n=13
#output:[1,10,11,12,13,2,3,4,5,6,7,8,9]\
data = int(input())
rlist=[str(i) for i in range(1,data+1)]
rlist.sort()
print(list(map(int,rlist)))