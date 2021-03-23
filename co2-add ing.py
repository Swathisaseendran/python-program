#Add 'ing' at the end of a given string.if it already ends with 'ing',then add 'ly'.

string=input("enter a string=")
if string.endswith("ing"):
    print(string+"ly")
else:
    print(string+"ing")