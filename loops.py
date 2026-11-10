#loops is nothing but it repeats the block of code ubtil the condition satisfis 
#the main types of loops are FOR and WHILE loop 

#FOR LOOP 
# it executes the block of code in loop untill its reaches the range value
# like n = 4 , n stores value 4
# for i in range (0,4) , it tells pyhton to create line of numbes from 0 to the n value meets 
#it loops repeatedly untill it meets the n value 

n = 4
for i in range(0,5):
 print(i)
 
# WHILE LOOP 
# it also executes the block of code untill the given condition matches
#we should use WHILE before the condition 

count = 1
while count < 5:
    count = count + 1
    print(count) 
    
#NESTED LOOPS 
#it is a loop inside a another loop

for i in range(1, 6):
    for j in range(i):
     print(i,end='')
     print()
     
 # break statement (cnfsd)
 #in python the stetement break is used to exit or break that loop 
 # using FOR LOOP 
 
for i in range(4):
    if i == 3:
        break 
    print(i)    
    
 #continue statement 
 #it is a loop control statement 
 #it tells that to skip the rest of current round of a loop and jumps to next round
 # we use continue here 
 
for i in range(5):
    if i == 3:
        continue
    print(i)
    
#PASS STATEMENT 
# it is a null operation
#it does nothing at all and carries normally 

for i in range(6):
    if i == 4:
        pass
    print(i)
    
# RANGE()
# it genrates the sequence of numbers that loop works on 
# it has three ways to use it -> range(stop) , range(start , stop) , range(start,stop,step)
for i in range(4):
 print(i,end="")
 
#LOOP ELSE 
#it is a block of code that runs only if a loop finishes all of its rounds completely 
    
for lap in range(1,4):
  print(f"completeing lap number{lap}")
else :
    print("race finished ")


 