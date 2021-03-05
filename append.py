#Prompt the user for a list of integers.For all values greater than 100,store 'over' instead.

list=[]
for i in range(6):
    x=int(input("Enter the number="))
    if x<100:
        list.append(x)
    else:
        list.append("Over")
print(list)
