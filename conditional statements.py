# IF condtion 
# In this statement if the condtion of IF is true it will goes to the next line and it will execute that 

age = 20
if age <= 18:
 print("you cant vote")
if age >= 18:
 print("you can vote")
 print("thankyou ! all the best ") 
 
height = 6.5
if height <= 6:
 print("you are not allowed for police job")
if height >= 6:
    print("congrats ! you are allowed ")
    
    
#IF ELSE condition
#in this if the IF block condition is true it prints next line , and another print statement prints when the condition is false

age = 15
if age >= 15:
    print("you should take ticket for travel")
else:
    print("you can travel for free") 
if age == 15:
    print("no need to take ticket")
else:
    print("ticket is must and should ")         

#IF-ELIF-ELSE STATEMENT 
# here multiple conditions are checked and excutes which is true 
# here we can use multiple conditions , are if , elif, elif, else 
  
age = 20
if age <= 10:
 print("you are child ")
elif age <= 15:
   print("you are teen ")
elif age <= 25:
    print(" you are adult")
else:
    print("aldut")
     
#NESTED IF CONDITION 
#writting a condition inside a condition is called  nested if condtion 
  
age = 20
is_voter= True

if age <= 20:
    if is_voter:
        print("he can vote easily ")
    else: 
     print("he cant do a vote ")
     
else:
    ("not elgible for vote")   
    
    
#CONDITIONAL EXPRESSIONS  (TERNARY OPERATOR)
# it is used to write a if-else statement in a single line , mostly it is used in choosing between two values based on a condition 

age = 20
s = "not elgible for driving license " if age <= 17 else ("elgible for license")
print(s)
        