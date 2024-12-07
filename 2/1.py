# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

with open('test.txt', 'r') as file:
   total = 0
   for line in file:
      s = line.strip()
      for first in s:
         for second in s:
            print(first, second)

         
          
      
