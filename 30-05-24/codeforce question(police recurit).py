n=int(input())
events=list(map(int,input().split()))
avapolice=0
unevents=0
for event in events:
    if event>0:
        avapolice+=event
    elif event==-1:
        if avapolice<=abs(event):
            unevents+=abs(event)-avapolice
            avapolice=0
        else:
            avapolice -= abs(event)
print(unevents)