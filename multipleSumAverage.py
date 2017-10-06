for i in range(1000):
  if i % 2 == 1:
    print i
'''This for loop will run from 0 to 1000, then check if the number is odd, and print that number'''

for i in range (5, 1000000, 5):
    print i
'''This loop will run from 5 to 1000000 in steps of 5 and print every 5th number'''

a = [1, 2, 5, 10, 255, 3]
x = (sum(a))
print x
'''This function adds all of the items in the list and prints the sum.'''

a = [1, 2, 5, 10, 255, 3]
print sum(a)/len(a)
'''This program takes the sum of the list and divides it by the number of items in the list.'''   
