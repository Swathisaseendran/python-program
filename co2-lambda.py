#write lambda functions to find area of square,rectangle and triangle.


a=int(input("enter the length"))
sqrarea=lambda a:a*a
print("area of square",sqrarea(a))
l=int(input("enter the length"))
b=int(input("enter the width"))
rectarea=lambda l,b:l*b
print("area of rectangle",rectarea(l,b))
b=int(input("enter the base"))
h=int(input("enter the height"))
triarea=lambda b,h:1/2*b*h
print("area of triangle",triarea(b,h))