#sort dictionary in ascending and descending order.


y = {'anu': 2, 'besti': 16, 'megha': 21}
l = list(y.items())
l.sort()
print('Ascending order is', l)
l = list(y.items())
l.sort(reverse=True)
print('Descending order is', l)
