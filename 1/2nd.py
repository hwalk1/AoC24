a = []
b = []

with open('data.txt', 'r') as file:
   for line in file:
      s = line
      aval, bval = map(int, s.split('   '))
      a.append(aval)
      b.append(bval)

total = 0


for x in a:
   total += b.count(x) * x
   
print(total)
