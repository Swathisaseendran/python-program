#get a string from an input string where all occurrences of first character replaced with '$' , except first character .

w=input("Enter a string=")
start=w[0]
s=w.replace(start,'$')
print(start+s[1:])


