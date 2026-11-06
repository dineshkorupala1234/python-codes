#INPUT
# #the input is just taking the information from the user in the form of any data type . 
# but we should just type input in the code like line 6,7,8 
#after name prints we should press enter in terminal to show age 

name = input("dinesh")
age = input(22)
height = input(6.1)
print(name)
print(age)
print(height)

#OUTPUT
# it is just showing the information to the user after running 

a = 20
b = 30
print(a)
print(b)
print(a+b)
print(a*b),(a/b)

#f string
 
name = "dinesh"
age = 22
print(f"my name is {name} and iam {age} years old ")

#print() function 
lst =[12,23,221]
a = ("dinesh")
height = 6.2
print(list,a,height)

#END 
# we use this to print in one line by using END even the print blocks are two 

print("hello good morning ",end="")
print("how are you")

#SEPERATOR (SEP)
# #we can use this to print in another line just diff is we use SEP here and that prints in next line 
print("hello good morning","22",sep="!")

# format menthod
# in this we use {} to place holders , and .format(name,age) to insert values 
name = "dinesh"
age = 22
print("my name is {} and my age is {}".format(name,age))








