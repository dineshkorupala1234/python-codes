# IMPLICIT TYPE CONVERSION 
# Implicit conversion in Python happens automatically when different data types are used together in an expression.

a = 12
b = 10.3
c = a + b
print("a:",type(a))
print("b:",type(b))
print("c=",c)
print("c:",type(c))

# "a" is an integer and "b" is float.
# During "c = a + b", Python implicitly converts a to a float to avoid data loss.
# the result, "c" becomes a float with the value 22.3.
# here conversion done automatically 


# EXPLICIT TYPE CONVERSION 
a = "100"
b = float(a)
print(a)
print(type(a))

#a  value :is a string 
# we give instruction that to convert a value into int type 
# and we print a 
# then we print its type 
# here conversion done manually 

# isinstance in python 
# it is nothing but ,it tells what the given data or variable type, if correct or wrong and tells which is true according to the condtion 
  
a = 10
b = "dinesh"
c = [2,3,22,4,2]
d = 23.2
e = {12,23,1,3,3}
f = (12,23,12,3)
print(isinstance(a,int))
print(isinstance(b,str))
print(isinstance(c,list))
print(isinstance(d,float))
print(isinstance(e,set))
print(isinstance(f,tuple))
