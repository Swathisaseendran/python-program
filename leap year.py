#display future leap years

y1=int(input("Enter current year="))
y2=int(input("Enter final year="))
print("Leap years")
for i in range(y1,y2+1):
    if i%4==0 and i%100!=0 or i%400==0:
        print(i)