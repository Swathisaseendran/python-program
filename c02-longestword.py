#Accept a list of words and return length of longest word.

l=[]
limit=int(input("enter the no.of words in the list="))
for i in range(limit):
     a=input("enter words")
     l.append(a)
print(l)
length=len(l[0])
temp=l[0]
for i in l:
    if len(i) > length:
       length=len(i)
       temp=i
print("The longest word",temp,"is of length",length)




