# video player plays a game in which the character competes in a hurdle race.
#Hurdles are of varying heights, and the characters have a maximum height they can jump. There is a magic potion they can take that will increase their maximum jump height by unit for each dose.
#How many doses of the potion must the character take to be able to jump all of the hurdles. If the character can already clear all of the hurdles, return
#Example height = [1, 2, 3, 3, 2] k = 1
n,k=map(int,input().split())
hlist=list(map(int,input().split()))
print(max(hlist)-k)