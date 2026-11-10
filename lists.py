#it is used to store collection of objects in order
# they are dyamic , resizeable , and capable of storing multiple data types
# elements are accessed using its position 
# list can be changed , updated, removed after list is created 
# list are created in these ways = [] , list construction-list(), repeating elements 

# creeating list using []
a = [1,2,3,4,]
print(a)
b = ("apple","grapes")
print(b)
 
# creating list using list constructor list()
a= ((1,2,3 , "apple",4.5))
print(a)
b = list("ABCD")
print(b)

# using Repeated elements
a=[2] * 5
b=[0] * 6
print(a)
print(b)

#INDEXING 
# it is getting one item from a list by its position 
# postitive position starts at 0 , negative position starts count from end  

numbers = [12,31,12,90]
print(numbers[0])
print(numbers[-1])

#SLICING 
#slicing means getting a section of list 
# in this the end position is not included

numbers = [10,20,30,40,50]
print(numbers[1:4])

#METHODS IN PYTHON 
numbers = [10,20,30]
numbers.append(5)   # the 5 added in list 
print(numbers)
numbers.remove(10)
print(numbers)
numbers.count(30)
print(numbers)

#SORTING
# sorting means arranging items in a list
#like largest or alphabetically 
numbers = [300,500,100,83]
numbers.sort()
print(numbers)

# NESTED LIST 
# a list inside a list is called nested list 
members= [["dinesh",22],["yogi",23]]
print(members[0])
print(members[1][0])

