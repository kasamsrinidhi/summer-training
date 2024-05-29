#generate a num from the given string,if no digit found return 0
# i/p-123av45b78 o/p 1234578
import string
a=input()
num=""
for i in a:
    if i in string.digits:
        num+=i
if num == "":
    print('0')
else:
    print(int(num))