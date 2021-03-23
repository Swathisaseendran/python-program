#Accept an integer n and compute n+nn+nnn.


sum=0
n=int(input("Enter a number="))
sum=(n+((n*10)+n)+((n*100)+(n*10)+n))
print(n,"+",((n*10)+n),"+",(n*100)+(n*10)+n,"=",sum)