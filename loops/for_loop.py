#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#Looping Through a String:
for x in "banana":
    print(x)

#The break Statement:
#with the break statement we can stop the loop before it has looped through all the items:

fruits_2 = ["apple", "banana", "cherry"]
for x in fruits_2:
  if x == "banana":
    break
  print(x)

#The continue Statement:
#we can stop the current iteration of the loop, and continue with the next:

names = ["apple", "banana", "cherry"]
for x in names:
  if x == "banana":
    continue
  print(x)

#the range() function
#to loop through a set of code a specified number of times, we can use the range() function,
#the range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for i in range(9):
   print(i)

#range(a, b), means values from a to b (but not including b):
for x in range(4, 9):
   print(x)

#range(a, b, c) c is the increment:
for x in range(2, 30, 3):
   print(x)

#Else in for loop:
#the else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
   print(x)
else:#the else block will NOT be executed if the loop is stopped by a break statement
   print("Finally finished!")

print("Hello")