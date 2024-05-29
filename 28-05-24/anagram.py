'''Rotate a given String in the specified direction by specified magnitude.After each rotation make a note of the first character of the rotated String,
After all rotation are performed the accumulated first character as noted previously will form another string, say FIRSTCHARSTRING. Check If FIRSTCHARSTRING is an Anagram of any substring of the Original string.
If yes print neg YES otherwise "NO".
Input: The first line contains the original string s. The second line contains a single integer q. The ith of the next q lines contains character d[i] denoting direction and integer r[i] denoting the magnitude.
Constraints: 1 <= Length of original string C = 30
1 <= q <= 10
Output: YES or NO
Input:
carrace
3
L 2
R 2
L 3
Output:
NO
Explanation:
After applying all the rotations the FIRSTCHARSTRING string will be "rcr" which is not anagram of any sub string of original string "carrace".'''
data=input()
rot=int(input())
res=''
for i in range(rot):
    di,mag=input().split()
    if di.upper()=='L':
        res+=(data[int(mag):]+data[:int(mag)])[0]
    elif di.upper()=='R':
        res+=(data[:int(mag)]+data[int(mag):])[0]
subList=[data[i:i+rot] for i in range(0,len(data)-rot+1)]
print(res,subList)
#Anagram:
for subele in subList:
    if sorted(subele)==sorted(res):
        print("Yes")
        break
else:
    print("No")



