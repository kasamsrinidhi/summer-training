#print the string in reverse order using recursion
def revStr(data):
    if data=="":
        return data
    return data[-1]+revStr(data[:-1])
strData=" string"
print(revStr(strData))
