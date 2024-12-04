with open('data.txt', 'r') as file:
   lines = file.readlines()

a = []
b = []
total = 0

for line in lines:
   s = line
   aval, bval = map(int, s.split('   '))
   a.append(aval)
   b.append(bval)

a.sort()
b.sort()

for idx, x in enumerate(a):

   total += (abs(a[idx] - b[idx]))

print(total)



