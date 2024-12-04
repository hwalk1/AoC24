
a = []
b = []

with open('data.txt', 'r') as file:
   for line in file:
      s = line
      aval, bval = map(int, s.split('   '))
      a.append(aval)
      b.append(bval)

a.sort()
b.sort()

total = 0
for idx, x in enumerate(a):
   total += (abs(a[idx] - b[idx]))

