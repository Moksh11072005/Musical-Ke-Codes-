# FOR LOOP

#  question a 
# 123
# 123

for i in range (1,3):
    for j in range (1,4):
        print (j,end=' ')
    print () 


# question b
# 111
# 222

for i in range (1,3):
    for j in range (1,4):
        print (i,end=' ')
    print ()


# question c
# 123
# 456

m=1
for i in range (1,3):
    for j in range (1,4):
        print (m,end=' ')
        m=m+1
    print ()


# question d
# 1
# 23
# 456

m=1
for i in range (1,4):
    for j in range (1,1+i):
        print (m,end=' ')
        m=m+1
    print ()


# question e
# 6
# 66
# 666
# 6666

for i in range (1,5):
    for j in range (1,1+i):
        print ('6',end=' ')
    print ()    
#question f 
#  *
# ***
#*****
n = 3
for i in range(3): 
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1)) 
#12345          i=rows
#1234           j=columns
#123
#12
#1
rows = int(input("enter the number of rows\n>>>"))
for i in range (rows,0,-1):
    for j in range (1,1+i):
        print (j,end=' ')
    print ()    
# "3" reverse a number ===>
number=int(input("Enter your number\n>>>\n"))
x=number
reverse=0
while (number>0):
    reverse=(reverse*10)+number%10
    number=number//10
print ('reverse of the number is\n>>>\n',reverse) 
if x == reverse:
    print('A palindromic number')
else:
    print('Not a palindromic number')  

# "18" FIND THE NUMBER IS PRIME OR NOT ===>
number = int(input("Enter a number: "))  
  
if number > 1:  
   for i in range(2,number):  
       if (number % i) == 0:  
           print(number,"is not a prime number")  
           break  
   else:  
       print(number,"is a prime number")  
         
else:  
   print(number,"is not a prime number")   
# find prime numbers in a range ===>
n=int(input("enter the range "))
for num in range(0,n+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
# find the sum of "n" natural no.s ===>
a=0
n=int(input('enter ur range'))
for i in range (0,n+1):
    a+=i
print(a)
# multiplication table of a given number ===>
a=int (input("enter your number"))
m=0
n=int(input("enter your range"))
for i in range (1,n+1):
    m=a*i
    print(m)
#AAAAAAAAAABBBBBBBCCCCCCEEEEE
for i in range (1, 5) :
    print ("A" * i , end = "")
for i in range (3, 5) :
    print ("B" * i , end = "")
for i in range (1, 4) :
    print ("C" * i , end = "")
for i in range (2, 4) :
    print ("E" * i , end = "")      
# 8
# 86
# 864
# 8642
num = "8642"
for i in range (4) :
    print (num[ : i + 1])
#######
#     #
#     #
#     #
#     #
#     #
#######

for i in range (7) :
    for j in range (7) :
        if i == 0 or i == 6:
            print ("#", end = "")
        elif j == 0 or j == 6 :
            print ("#", end = "")
        else :
            print (" ", end = "")
    print ()
# (a)

#######
#    
 #   
  #  
    #
      #
#######

# (b)

#######
      #
     #
    #
   #  
 #   
#######

#(a)
for i in range (7) :
    for j in range (7) :
        if i == 0 or i == 6:
            print ("#", end = "")
        elif j == i :
            print ("#", end = "")
        else :
            print (" ", end = "")
    print ()

#(b)
for i in range (7) :
    for j in range (7) :
        if i == 0 or i == 6:
            print ("#", end = "")
        elif j == 7 - i :
            print ("#", end = "")
        else :
            print (" ", end = "")
    print ()  
# FIBONACCI SERIES 
r=int(input("enter range"))
first=int(input('enter first number'))
second = int(input('enter second number'))
print(first)
print(second)
for i in range (r+1):
    third = first + second 
    first,second=second,third
    print(third)  
# AP , GP or FIBONACCI SERIES 
ch=int(input("'1' for A.P.\n'2' for G.P.\n'3' for fibonacci series\nenter your choice"))
while ch == 1:
    print("your choice is A.P.")
    t=int(input("enter no. of terms"))
    d=int(input("enter difference"))
    first=int(input("enter first term"))
    for i in range (t):
        second=first+d
        print(first)
        first=second
    break
while ch==2:
    print("your choice is G.P.")
    t=int(input("enter no. of terms"))
    d=int(input("enter ratio"))
    first=int(input("enter first term"))
    for i in range (t):
        second=first*d
        print(first)
        first=second
    break    
else:
    print("your choice is fibonacci series")
    r=int(input("enter range"))
    first=int(input('enter first number'))
    second = int(input('enter second number'))
    print(first)
    print(second)
    for i in range (r+1):
        third = first + second 
        first,second=second,third
        print(third)  
# guessing game
for i in range (5):
    guess = int(input("enter your guess"))
    if guess==5:
        print("5 is correct")
        break
else :
    print("please try again")     
# Rock Paper Scissor Game Against Your Computer
import random
rules=print("Rules:\n1  for 'Stone', 2  for 'Paper' and 3  for 'Scissor'\nYou will be having only 5 chances to play.\nGOOD LUCK!!!")
for i in range (5):
    ch=(1,2,3)
    user=int(input("---------------------\nenter your choice\n>>>"))
    computer=random.choice(ch)
    if user==computer:
        print("TIE (NO POINTS)")
    elif user==1 and computer==2 :
        print('1 POINT TO COMPUTER')    
    elif user==1 and computer==3 :
        print('1 POINT TO YOU')    
    elif user==computer:
        print("TIE (NO POINTS)")    
    elif user==2 and computer==1 :
        print('1 POINT TO YOU')
    elif user==2 and computer==3 :
        print('1 POINT TO COMPUTER')        
    elif user==3 and computer==2 :
        print('1 POINT TO YOU')    
    elif user==3 and computer==3 :
        print('TIE (NO POINTS)')
    elif user==3 and computer==1 :
        print('1 POINT TO COMPUTER')    
    else:
        print("INVALID CHOICE PLEASE TRY AGAIN")
        break
    print("computer's choice\n>>>",computer) 
#GUESSING GAME
import random
rules=print("Rules:\nComputer will chose a random number between 1 and 10.\nYou will be having only 5 chances to answer.\nGOOD LUCK!!!")
list1=[1,2,3,4,5,6,7,8,9,10]
r=random.choice(list1)
for i in range (5):
    ur=int(input("Enter Your Number\n>>>"))
    if r==ur:
        print("YAY!!!, You guessed the number correctly ")
        break
    
else :
    print("You Lost!!!,Please try again")        
    print("Computer chose",r)                           