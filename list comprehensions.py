#generate positive list of numbers from a given list of integers

a=[-3,-2,-1,0,1,2,3,4]
b=[x for x in a if x>0]
print("Positive integers are..",b)
print("-----------------------")


#square of n numbers

list=[]
n=int(input("Enter no:of numbers="))
for i in range(n):
    x=int(input("Enter number="))
    list.append(x)
print("list=",list)
sq=[x**2 for x in list]
print("list of squares=",sq)
print("-----------------------")


#form a list of vowels selected from a given word.

word=input("Enter a word=")
v="aeiou"
list=[x for x in word if x in v]
print("vowels are=",list)

print("-----------------------")

#list of ordinal value of each element of a word.


l="garden"
a=[ord(x) for x in l]
print("ordinal values=",a)