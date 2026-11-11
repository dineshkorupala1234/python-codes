# it is used to store collection of unique itesm 
# it stores only unique elements , and Duplicate values are removed autmatically 
# it supports fast search , insertion and deletion operations using hashing 
# it may not keep items in fixed order

s = {10,20,30,40,50}
print(s)
print(type(s))

#TYPE CASTING 
#it means converting one data type to another type like converting number to text 

s = set(["dog","cat","hen"])
print(s)
# list converted into text here 

#FROZEN SET
# frozen set is a unchangable set in python 
# it contains regular sets but we cannot add or remove items after created 
# if a input contains duplicate values it will not prints in o/p

colours = frozenset(["white","black","white"])
print(colours)

# METHODS 
# In Python,a method is a function attached to an object. You call it using the object, a dot, the method name, and parentheses:

# 1 .UNION
#  it combines all the items from both sets . duplicates are also appears only once 
a = { 1,2,3,4}
b = {5,6,7,8,}
c = a.union(b) #method 
print (a|b)    # operator 
print(c)

# INTERSECTION 
# It finds common ground between sets
# it returns new set containing only elements that exists in both set A and B

a = {10,20,30,40}
b = {50,60,70}
c = a.intersection(b) # method 
print(a&b)   #operator 
print(c)

#DIFFERENCE 
#A set containing items in the first set that are not in the second

a = {12,34,56}
b = {78,90,12}
c = a.difference(b) # method 
print(a-b) #operator 
print(c)

#SYMMETRIC DIFFERENCE 
# A set containing items that appears in one or other set , but doesn't matter in which set 
a = {100,200,300}
b = {400, 500, 600}
c = a.symmetric_difference(b)
print(a^b)
print(c)

#CLEAR 
# it means it removes all the elements from a set , leaves it empty
s = {12,34,123,67}
s.clear()
print(s)