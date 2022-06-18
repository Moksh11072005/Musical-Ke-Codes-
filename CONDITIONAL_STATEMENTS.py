# "11" "if" and "else" functions ===>
a=23
b=43
if(a>b):
    print(a)
    print("a")
else:
    print(b, end="")
    print("b")
# "12" grading system in schools ===>
marks1 = float(input("Enter marks of subject 1\n>>>\n"))  
marks2 = float(input("Enter marks of subject 2\n>>>\n")) 
marks3 = float(input("Enter marks of subject 3\n>>>\n")) 
marks4 = float(input("Enter marks of subject 4\n>>>\n")) 
marks5 = float(input("Enter marks of subject 5\n>>>\n")) 
total = marks1 + marks2 + marks3 + marks4 + marks5
print ("Your Total Marks is\n>>>\n",total)
percentage = total/5
print("Your Percentage is\n>>>\n",percentage)
if 100 >= percentage >= 85:
    print('Your Grade is A')
elif 84 >= percentage >= 69:
    print('Your Grade is B')
elif 68 >= percentage >= 56:
    print('Your Grade is C')   
elif 55 >= percentage >= 44:
    print('Your Grade is D')   
elif 43 >= percentage >= 33:
    print('Your Grade is E')    
else :
    print('You are Failed !!!')    
# "13" Sales commission system ===>
sales = int(input("Enter your sale\n>>>"))
if sales>20000:
    print('commission is\n>>>50%')
elif 20000>=sales>10000:
    print  ('commission is\n>>>10%')
elif 10000>=sales>5000:
    print('commission is\n>>>5%')    
elif 5000>=sales>1000:
    print('commission is\n>>>1%')
elif 1000>=sales>0:
    print('commission is\n>>>.1%')    
elif 0>=sales:
    print('commission is\n>>>0%')  
# '20' formula to find leap years ===> 
year=int(input("Enter Year\n>>>"))
if year%4==0:
    print ('A Leap Year')
else :
    print('Not a Leap Year') 
# '21' TO FIND PROFIT AND LOSS ===>
c=int(input("Enter Cost Price\n>>>"))
s=int(input("Enter Selling Price\n>>>"))
if c<s:
    print ('You Got a Profit of Rs',s-c)
elif c>s:
    print("You Got a Loss of Rs",c-s)   
# '22' check that the number is odd or even ===>
n= int(input("Enter Your Number\n>>>"))
if n%2==0:
    print("The Number",n,"is an even number")
else:
    print("The Number",n,"is an odd number")  
# '23' check that the letter is a vowel or constant
n=input("Enter a Letter\n>>>")  
if n in 'aeiouAEIOU':
    print('vowel')
else :
    print('constant')
# '24' roots of a quadritic equation ===>
a=int(input("enter co-efficient a\n>>>"))
b=int(input("enter co-efficient b\n>>>"))
c=int(input("enter co-efficient c\n>>>"))
print('your quadritic equation is==>',a,'x^2 + ',b,'x + ',c)
d=(b*b)-(4*a*c)
print ('discriminant of quadritic equation=',d)
if d==0:
    print('there is exactly one real root') 
elif d>0:
    print('there are two distinct roots ') 
elif d<0:
    print('there are two distinct roots ')   
# '25' check whether a character is an alphabet, digit or special character           
character=input("enter \n>>>")
if character>='A' and character<='Z' or character>='a' and character<='z':
 print('Alphabet')
elif character in '1234567890':
 print('Number')
else:
 print('Special character') 
# '26' display quadrant of coordinates
x= int (input('enter x\n>>>'))
y= int (input('enter y\n>>>'))
print('your coordinates are \n>>>',(x,y))
if x>0 and y>0:
    print('1st quadrant')
elif x<0 and y>0:
    print('2nd quadrant')    
elif x<0 and y<0 :
    print('3rd quadrant')    
else :
    print('4th quadrant')        
# "17"  TIME TABLE ===> 
day = input("Enter your day\n>>> ")
if day == 'monday':
    print ("8:00  am -- 8:50  am --> Maths Class\n9:00  am -- 9:55  am --> No Class\n10:00 am -- 10:50 am --> Physics Class\n11:50 am -- 12:40 pm --> English Class\n12:40 pm -- 1:30  pm --> Computer science Class\nSCHOOL END")
if day == 'tuesday':
    print("8:00  am -- 8:50  am --> Maths Class\n9:00  am -- 9:55  am --> Chemistry Class\n10:00 am -- 10:50 am --> Physics Class\n11:50 am -- 12:40 pm --> English Class\n12:40 pm -- 1:30  pm --> Computer science Class\nSCHOOL END")
if day == 'wednesday':
    print("8:00  am -- 8:50  am --> Maths Class\n9:00  am -- 9:55  am --> Chemistry Class\n10:00 am -- 10:50 am --> Physics Class\n11:50 am -- 12:40 pm --> No Class\n12:40 pm -- 1:30  pm --> Computer science Class\nSCHOOL END")
if day == 'thrusday':
    print("8:00  am -- 8:50  am --> Maths Class\n9:00  am -- 9:55  am --> Chemistry Class\n10:00 am -- 10:50 am --> Physics Class\n11:50 am -- 12:40 pm --> English Class\n12:40 pm -- 1:30  pm --> No Class\nSCHOOL END")   
if day == 'friday':
    print("8:00  am -- 8:50  am --> No Class\n9:00  am -- 9:55  am --> Chemistry Class\n10:00 am -- 10:50 am --> Physics Class\n11:50 am -- 12:40 pm --> English Class\n12:40 pm -- 1:30  pm --> Computer science Class\nSCHOOL END")           
if day == 'saturday':
    print("NO SCHOOL...HAVE FUN...")
if day == 'sunday':
    print ("NO SCHOOL...HAVE FUN...")
else:
    exit                  
#input 3 no.s by the user (say a,b,a)
#sum 1 = sum of all no.s
#sum2 = sum of non duplicate no.s(b)
x=int(input("enter"))
y=int(input("enter"))
z=int(input("enter"))
sum1=x+y+z
print('sum1 = ',sum1)
if x==y:
    print("sum2 = ",z)   
elif x==z:
    print("sum2 = ",y)
elif y==z :
    print("sum2 = ",x)        
else :
    print("sum2 = ",sum1)     
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