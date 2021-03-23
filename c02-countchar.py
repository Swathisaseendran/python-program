#count the number of characters(character frequency)in a string.

string=input("Enter a string=")
s={}
for i in string:
    if i in s:
        s[i]+=1
    else:
        s[i]=1
print("Count of all characters are:",s)