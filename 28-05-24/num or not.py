#check if data is a num or not
#124-true 12m4-false 1ab23-false
import string
strNum = input()
for i in strNum:
    if i not in string.digits:
        print("false")
        break
else:
    print("true")