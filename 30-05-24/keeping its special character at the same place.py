#reverse a string keeping its special character at the same place
#i/p:h@ello o/p:o@lleh
import re
string = input()
string_list = re.findall("[a-zA-Z]",string)
string_list.reverse()
for i in range(len(string)):
    if(string[i]=='#' or string[i]== "@"):
        string_list.insert(i,string[i])
print("".join(string_list))