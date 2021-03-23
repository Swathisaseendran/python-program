#Display the given pyramid with step number accepted from user.

n=int(input("Enter the step number="))
for x in range(1,n+1):
    for y in range(1,x+1):
        print(x*y,end='  ')
    print("\n")



