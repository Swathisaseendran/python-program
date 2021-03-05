#count the occurences of each word in a line of text

w=input("Enter a string=")
count=dict()
words=w.split()
for x in words:
         if x in count:
             count[x]+=1
         else:
             count[x]=1
print(count)
