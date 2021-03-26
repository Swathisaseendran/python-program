class Rectangle:
    def __init__(self,length,breadth):
       self.length=length
       self.breadth=breadth
    def area(self):
       return(self.length*self.breadth)
    def perimeter(self):
        return(2*(self.length+self.breadth))
r1=Rectangle(4,5)
r2=Rectangle(9,2)
a=r1.area()
b=r2.area()
c=r1.perimeter()
d=r2.perimeter()
print("the areas are",a,b,"respectively")
print("the perimeters are",c,d,"respectively")

if a>b:
    print(a,"is the greater area")
else:
    print(b,"is the greater area")

