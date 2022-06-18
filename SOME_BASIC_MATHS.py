# "2" addition,subtraction,multiplication and division of variables ===>
a=1
b=2
# for addition--> 
print(a+b)
# for subtraction ===>
print(a-b)
# for multiplication ===>
print(a*b)
# for division ===>
print(a/b)
# average of two numbers ===>
a=int(input("enter first number\n"))
b=int(input("enter second number\n"))
avg=(a+b)/2
print("the average of a and b is\n",avg)
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
# "6" area of circle(pi r^2) ===>
a=float(input("enter radius\n"))
b=float(3.14)
print("area of the circle is",b*a*a)
# "7" perimeter and area of rectangle ===>
a=int(input("Enter length\n"))
b=int(input("Enter breadth\n"))
perimeter=2*(a+b)
area=a*b
print("perimeter of rectangle is\n", perimeter)
print("area of the rectangle is\n", area)
# "8" celsius to fahrenheit (formula -- ===> (0°C × 9/5) + 32 ) ===>
a=float(input("enter degree celsius\n"))
b=float(1.8)
c=float(32)
print("degree celsius in fahrenheit is\n",(a*b)+32)
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

#
number = int(input("Enter your number\n>>>"))
if number%2 != 0:
    print ("Weird") 
if number%2==0 and 2<=number<=5:
    print ('not weird')
if number%2==0 and 6<=number<=20:
    print('Weird')    
if number%2==0 and number>20:
    print('Not Weird')  
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
elif n%2!=0:
    print("The Number",n,"is an odd number") 
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
#'26' input 3 no.s by the user (say a,b,a)===>
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
#'27' find prime numbers in a range ===>
n=int(input("enter the range "))
for num in range(0,n+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
#'28' find the sum of "n" natural no.s ===>
a=0
n=int(input('enter ur range'))
for i in range (0,n+1):
    a+=i
print(a)
#'29' multiplication table of a given number ===>
a=int (input("enter your number"))
m=0
n=int(input("enter your range"))
for i in range (1,n+1):
    m=a*i
    print(m)                 
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
# input a matrix by user 
r=int(input("Enter rows : "))
c=int(input("Enter columns : "))
matrix=[]
for i in range(r):
    m=[]
    for j in range (c):
        e=int(input(f"Enter element {i+1},{j+1} : "))
        m.append(e)
    n=len(m)
    #sort the initial matrix (row wise sorting)
    for q in range (n):
        for k in range (0,n-q-1):
            if m[k]>m[k+1]:
                m[k],m[k+1]=m[k+1],m[k]
    matrix.append(m)
# print the row wise sorted matrix 
for x in range (r):
    for y in range (c):
        print(matrix[x][y],end=" ")
    print()  