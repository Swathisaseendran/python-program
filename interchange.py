#create a string from given string where first and last character exchanged.

str=input("Enter a string=")
start=str[0]
end=str[-1]
mid=str[1:-1]
print(end+mid+start)