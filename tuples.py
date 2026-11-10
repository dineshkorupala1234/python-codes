#tuples are similar to list but they can't be changed after they created 
# they can hold elements of different datatypes
# they are ordered , immutable , hetrogenious

# CREATING A TUPLE
# it is created by placing items inside a parathasis()

# using string
fruits = ("grapes","orange","mango")
print(fruits)

#using list 
books = [1,2,3,4,5]
print(tuple(books))

# using built-in function
tup = tuple('dinesh')
print(tup)

# SLICING 
# slicing means getting of section of tuple uesing index positions 
# positive starts from 0 
# negative starts from -1 from right to left 
# [: default beginging of string 
# [:: -1] to reverse a string 
# :] default end of a sequence 

tup = tuple("dineshkumar")
print(tup[1:])
print(tup[::-1])
print(tup[4:8])

#INDEXING 
# getting one item from a tuple by its position 
members = ("sai","shiva","dev","prakash")
print(members[3])

#PACKING 
# packing means putting several values in one tuple

person = "dinesh",22,"nagarkurnool"
print(person)

#UNPACKING
#unpacking means assigning the tuples to seperate variables

person= ("dinesh",22,"nagarkurnool")
name,age,place = person
print(name)
print(age)
print(place)

#IMMUTABILITY
#it means it cannot be changed after it created 
colors = ("red", "blue")
colors[0] = "blue"