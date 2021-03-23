#From a list of integers, create a list removing even numbers.

li=[1,2,3,4,5,6,7,8,9]
for x in li:
    if x%2==0:
       li.remove(x)
print(li)