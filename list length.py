#check whether list are of same length

nlist=[2,7,9,4]
mlist=[5,6,4,2,5]
if len(mlist)==len(nlist):
    print("equal length",len(mlist))
else:
    print("First list length=",len(nlist),"\nSecond list length=",len(mlist),"\nDifferent length")
print("--------------------")

#check whether sums to same value

if sum(nlist)==sum(mlist):
    print("First list sum=",sum(nlist),"\nSecond list sum=",sum(mlist),"\nSum of lists are same")
else:
    print("Different sums")
print("--------------------")

#check whether any value occur in both

for a in range(4):
    for b in range(5):
        if nlist[a]==mlist[b]:
            print(nlist[a],"is occuring in both list")