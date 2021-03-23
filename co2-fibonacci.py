#Generate fibonacci series of N terms.

n=int(input("Enter the limit="))
print("Fibonacci series of",n,"terms:")
a=0
b=1
c=a+b
print(a)
print(b)
print(c)
for i in range(n-3):
    a=b
    b=c
    c=a+b
    print(c)