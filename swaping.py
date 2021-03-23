#create a single string separated with space from two strings by swapping the character at position 1.


def charchange(a, b):
  new_a = b[:1] + a[1:]
  new_b = a[:1] + b[1:]
  return new_a + ' ' + new_b
print(charchange('swathi', 'saseendran'))
