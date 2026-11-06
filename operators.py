a = 234
b = 23
c = 2345
print("addition:",a+b)
print("subraction:",a-b)
print("multiply",a*b)
print("divide",a/b)

#real time example to define the operators
balance = 2000
pin = 1234
if pin == 1234:  
    print("the pin is true")
if pin != 1234:
    print("invalid pin")
if balance <= 2000:
   print("thankyou!, take ur money")
   
a = 120
b = 200
print(a < b)   
print(a > b)   
print(a * b)   
print(a / b)   

#identity operators 
a = 1219
b = 345 
c = a
d = c
print(a is not c)
print(b is not a)
print(c is a)
print( c is d)  

#bitwise operators 
a=5
b=3
print(a & b)
print(a | b)
print(~a)
print(a >> b)
print(a << b)
print(a ^ b)

#assignment operators
a = 30
b = a 
print(b)
b += a
print(b)
b -= a
print(b)

#identity operators
a = 12
b = 20 
c = a
d =12
print(a is not b)
print(a is c)
print(d is a )
 
 #membership operator 
a = 10 
b = 20 
my_list = [12,234,10,27,89]
  
if(a not in my_list):
    print("yes it is not in list ")
else:
    print("a is present in the list")
if(b in my_list):
    print("yes it is in list")
else:
   print("it is not in my list ")
 
 

