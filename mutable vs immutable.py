# MUTABLE AND IMMUTABLE 
# MUTABLE 
# mutable objects can be changed after they created 

scores = [21,34,56]         #the list is mutable so it combined value into given list
scores.append(56)           
print(scores)
scores.insert(65,1)
print(scores)

#IMMUTABLE
# immutable objects cant be changed after they are created 

word = "dinesh"   # checking by using string - it is unmutable 
word = word+"kumar"
print(word)

# OBJECT REFERENCE 
# it is like a address that tells pyhton to where the particular data is stored
# we use built-in-function id() to check objects identity
#if two variables have same id they refer to same object
numbers = [12,23,45]
other = numbers
other.append(4)
print(id(numbers))
print(id(other))
print(numbers is other)

#SHALLOW COPY 
# it creates a new outer object while keeping references to same items inside it 
import copy 
orginal =[[10,20],[30,40]]
shallow = copy.copy(orginal)
print(orginal)
print(shallow)
print(orginal is shallow)

#DEEP COPY 
#it also creates the object but here it copies inside it 
import copy
orginal = [[1,3],[12,30]]
deep = copy.deepcopy(orginal)
deep[0].append(90)
print(orginal)
print(deep)
