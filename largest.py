#Find biggest of 3 numbers entered.

a=int(input("Enter First number="))
b=int(input("Enter Second number="))
c=int(input("Enter Third number="))
if a>b:
    if a>c:
        print(a,"is the largest number")
    else:
        print(c,"is the largest number")
elif b>c:
    print(b,"is the largest number")
else:
    print(c,"is the largest number")