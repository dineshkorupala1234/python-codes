#STRINGS 
# A strings is a sequence of characters , we use it to store text, names, numbers etc
# they are enclosed with a quotation marks
# - single quotes , double quotes , triple quotes and both behaves same 

a = 'WNDS'
b = "Windows"
print (a)
print(b)

# MULTI LINE STRINGS 
# it can be created using triple quotes 

s = """ Hi my name is dinesh
 iam learning python """
print(s)

#IMPORTANT STRING METHODS 
# upper() -converts to upper case 
# loweR() - converts to lower case
# len()- counts letter
# replace() - we can replace word
#spilt() - spilts a string 
# find () - finds a word or character
# strip() - removes extra spaces

name = ("dinesh")
print("welcome",name)
print("the length is ",len(name))
print("uppercase",name.upper())
print("lower case",name.lower())

#SLICING 
# it is seperating the part of a string using ramge of its position 
# syntax - string[start:end]
# start = staring index , end = ending indexx

name = " dinesh"
print(name[1:4])
print(name[3:6]) 
print(name[:4])
print(name[4:])

# INDEXING 
# it means accessing a single character from a string using its position
# POSITIVE INDEXING - starts from left to right from 0
# NEGATIVE INDEXING - starts from right to left from -1

name = "dinesh"
print(name[3])
print(name[4])
print(name[5])

#STRING FORMATING 
# it is just inserting values or variables in to a string
# three methods of it 
# f-string , format() , %formatting
name = "dinesh"
age = 22
print(f"my name is {name} and iam {age} years old ")

#STRING MANUPLATION 
# the process of changing or working with the text program like replacing, changing letter case , joining strings 

text = "dinesh kumar"
print(text.upper)
print(text.replace("kumar","korupala"))
print(text[0:5])
print(text + "!")