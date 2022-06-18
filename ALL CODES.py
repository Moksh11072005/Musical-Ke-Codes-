# # # playsound module installation--> (pip install playsound[in terminal{ONLY IN VS CODE}])
# # # use of playsound module
# # # from playsound import playsound 
# # # playsound("location of music.mp3 [with \\]")
# "1" print variables- ===>
a="moksh"
b="a"
c="good"
d="boy"
print("a")
print("b")
print("c")
print("d")
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
# "4" STRINGS ===>
# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())
#Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)
# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)
# writing variables seperately 
a=input('enter word')
print(a[0])
print(a[1])
print(a[2])
print(a[3])
# string slicing
a="1234"
print(a[0:3])
# "5" greetings ===>
a=input("enter your name\n")
print("dear, " + a)
print("you are selected")
b=("Date ===>09-05-2021")
print (b)
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
#LIST
list1=["a","b","c","d"]
for i in (list1):
    print(i)
#mutability of a list
list1=["a","b","c","d"]
list1[0]="b"
print(list1)
#operations===>
#concatenation
list1=["a","b","c","d"]
list2=["e","f","g","h"]
print(list1+list2)
#repetition
list1=["a"]
print(list1*4)   
#membership
list1=["a","b","c","d"]
print("b" in list1)
print("e" in list1)
#slicing
list1=["a","b","c","d"]
print(list1[0:2])
#TRAVERSING A LIST
list1=["a","b","c","d"]
#for loop
for i in list1:
    print(i)
#while loop
i = 0
while i < len(list1):
 print(list1[i])
 i += 1 
#range and len function
for i in range(len(list1)):
    print(list1[i])
#BUILT-IN FUNCTIONS
#1 len()
list1=["a","b","c","d"]
print(len(list1))
#2 list()---> creates an empty list
list1=["a","b","c","d"]
list2 = list()
print(list2)
#3 list(strl)--->converts each character of a string in to a list
str1='aeiou'
list3=list(str1)
print(list3)
#4 append()--->adds characters at the end of a list
list1=["a","b","c","d"]
list1.append('e')
print(list1)
#5 extend()---> basically adds two lists 
list1=["a","b","c","d"]
list1.extend(list3)
print(list1)
#6 insert()---> inserts an element at a particular index
list1=["a","b","c","d"]
list1.insert(2,'x')
print(list1)
#7 count()--->counts the number of times a character is repeated
list1=["a","b","c","d"]
print(list1.count('a'))
#8 index()---> prints the index of the selected character
list1=["a","b","c","d"]
print(list1.index('a'))
#9 remove()--->removes the selected element 
list1=["a","b","c","d"]
list1.remove('a')
print(list1)
#10 reverse()
list1=["a","b","c","d"]
list1.reverse()
print(list1)
#11 sort()
#11.1---> sorting in ascending order
list1=["e","b","c","d"]
list1.sort()
print(list1)
#11.2 sorting in descending order
list1=["e","b","c","d"]
list1.sort(reverse=True)
print(list1)
#12 sorted()--->creates a new list from the selected list arranged in sorted order
list1=["e","b","c","d"]
list4=sorted(list1)
print(list4)
#13 min()--->Returns minimum or smallest element of the list
#   max()--->Returns maximum or largest element of the list
#   sum()--->Returns sum of the elements of the list
list1 = [34,12,63,39,92,44]
print(min(list1))
print(max(list1))
print(sum(list1))   
# "10" perimeter and area of a rectangle ===>
a=int(input("Enter length\n"))
b=int(input("Enter breadth\n"))
perimeter=2*(a+b)
area=a*b
print("perimeter of rectangle is\n", perimeter)
print("area of the rectangle is\n", area)
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
# "14" TUPLES ===>
# creating a tuple by input function
f1 = input("Enter Fruit Number 1\n ")
f2 = input("Enter Fruit Number 2\n ")
f3 = input("Enter Fruit Number 3\n ")
f4 = input("Enter Fruit Number 4\n ")
f5 = input("Enter Fruit Number 5\n ")
f6 = input("Enter Fruit Number 6\n ")
f7 = input("Enter Fruit Number 7\n ")

myFruitList = [f1, f2, f3, f4, f5, f6, f7]
print(myFruitList)             
# "17" FIND THE NUMBER IS PRIME OR NOT ===>
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
# '18' LOOPS ===>
# question a 
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
# '19' formula to find leap years ===> 
year=int(input("Enter Year\n>>>"))
if year%4==0:
    print ('A Leap Year')
else :
    print('Not a Leap Year') 
# '20' TO FIND PROFIT AND LOSS ===>
c=int(input("Enter Cost Price\n>>>"))
s=int(input("Enter Selling Price\n>>>"))
if c<s:
    print ('You Got a Profit of Rs',s-c)
elif c>s:
    print("You Got a Loss of Rs",c-s)   
# '21' check that the number is odd or even ===>
n= int(input("Enter Your Number\n>>>"))
if n%2==0:
    print("The Number",n,"is an even number")
else:
    print("The Number",n,"is an odd number")  
# '22' check that the letter is a vowel or constant
n=input("Enter a Letter\n>>>")  
if n in 'aeiouAEIOU':
    print('vowel')
else :
    print('constant')
# '23' roots of a quadritic equation ===>
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
# '24' check whether a character is an alphabet, digit or special character           
character=input("enter \n>>>")
if character>='A' and character<='Z' or character>='a' and character<='z':
 print('Alphabet')
elif character in '1234567890':
 print('Number')
else:
 print('Special character') 
# '25' display quadrant of coordinates
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
#TUPLES
tuple1=("a","b","c","d")
print(tuple1)
#tuples are immutable
#operations
#1 concatenation
tuple1=("a","b","c","d")
tuple2=("b","c","d")
print(tuple1+tuple2)
#2 repetition
tuple1=("a","b","c","d")
print(tuple1*3)
#3 membership
tuple1=("a","b","c","d")
print("a" in tuple1)
#4 slicing
tuple1=("a","b","c","d")
print(tuple1[0:2])
#TRAVERSING A TUPLE
tuple1=("a","b","c","d")
#for loop
for i in tuple1:
    print(i)
#while loop
i = 0
while i < len(tuple1):
    print(tuple1[i])
    i += 1 
#range and len function
for i in range(len(tuple1)):
    print(tuple1[i])
# BUILT IN FUNCTIONS
#1 len()
tuple1=("a","b","c","d")
print(len(tuple1))
#2 max()--->returns the element with max value
tuple1=("a","b","c","d")
print(max(tuple1))
#3 min()--->returns the element with min value 
tuple1=("a","b","c","d")
print(min(tuple1))
#4 index()---> returns the index of the selected element
tuple1=("a","b","c","d")
print(tuple1.index("a"))
#5 sum()---> returns the sum of the elements of the tuple (only for integers)
tuple1=(3,2,6,4,6)
print(sum(tuple1))
#6 count()--->returns the number of the selected element repeated in a tuple
tuple1=("a","b","c","a","d")
print(tuple1.count("a"))
#7 sorted()---> returns the sorted tuple
tuple1=("a","b","c","d","a")
print(sorted(tuple1))
#8 tuple()---> creates a tuple
print(tuple('abc'))
#DICTIONARY
dict1={ 'Mohan':95, #marks of 4 students
'Ram':89,
'Suhel':92, 
'Sangeeta':85
}
print(dict1)
# ACCESSING THE ELEMENTS OF THE DICTIONARY
dict1={ 'Mohan':95, #marks of 4 students
'Ram':89,
'Suhel':92, 
'Sangeeta':85
}
print(dict1['Mohan'])
print(dict1['Ram'])
print(dict1['Suhel'])
print(dict1['Sangeeta'])
#LOOPS
#for loop 
dict1={ 'Mohan':95, #marks of 4 students
'Ram':89,
'Suhel':92, 
'Sangeeta':85
}
for i in dict1:
    print(i,":",dict1[i])

#
for key,value in dict1.items():
    print(key,':',value)    
# BUILT-IN FUNCTIONS
#1 len()
dict1={ 'Mohan':95, #marks of 4 students
'Ram':89,
'Suhel':92, 
'Sangeeta':85
}
print(len(dict1))
#2 dict()---> creates a dictionary from a list of key and values 
list = [('Mohan',95),('Ram',89),('Suhel',92),('Sangeeta',85)]
print(dict(list))
#3 keys()---> returns the keys in dictionary
dict1={ 'Mohan':95, #marks of 4 students
'Ram':89,
'Suhel':92, 
'Sangeeta':85
}
print(dict1.keys())
#4 values()---> returns the values in dictionary
dict1={ 'Mohan':95, #marks of 4 students
'Ram':89,
'Suhel':92, 
'Sangeeta':85
}
print(dict1.values())
#5 items()---> basically converts the dictionary into a tuple
dict1={ 'Mohan':95, #marks of 4 students
'Ram':89,
'Suhel':92, 
'Sangeeta':85
}
print(dict1.items())
#6 get()---> Returns the value corresponding to the key passed as the argument .If the key is not present in the dictionary it will return None
dict1={ 'Mohan':95, #marks of 4 students
'Ram':89,
'Suhel':92, 
'Sangeeta':85
}
print(dict1.get('Sangeeta'))
#7 update()--->appends the key-value pair in the end of the dictionary
dict1={ 'Mohan':95, #marks of 4 students
'Ram':89,
'Suhel':92, 
'Sangeeta':85
}
dict2={ 'M':5, 
'R':9
}
dict1.update(dict2)
print(dict1)
#8 del()---> deletes the item of the respective key
dict1={ 'Mohan':95, #marks of 4 students
'Ram':89,
'Suhel':92, 
'Sangeeta':85
}
del dict1['Ram']
print(dict1)
#9 clear()---> deletes all the items of the dictionary
dict1={ 'Mohan':95, #marks of 4 students
'Ram':89,
'Suhel':92, 
'Sangeeta':85
}
dict1.clear()
print(dict1)
#QUESTIONS
#1 Write a program to count the number of times a character appears in a given string.
st = input("Enter a string: ")
dictioanry = {} #creates an empty dictioanry
for character in st:
    if character in dictioanry: #if next character is already in the dictioanry
        dictioanry[character] += 1
    else:
        dictioanry[character] = 1 #if character appears for the first time
for key in dictioanry:
    print(key,':',dictioanry[key]) 
#2 Write a function to convert a number entered number in to words 
def convert(num):
    #numberNames is a dictionary of digits and corresponding number 
    #names
    numberNames = {0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',\
    5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
 
    result = ''
    for ch in num:
        key = int(ch) #converts character to integer
        value = numberNames[key]
        result = result + ' ' + value
        return result
num = input("Enter any number: ") #number is stored as string
result = convert(num) 
print("The number is:",num)
print("The numberName is:",result)
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
original_matrix=[]
sorted_matrix=[]
adduct_matrix=[]
rows=int(input("Enter the number of rows : "))
columns=int(input("Enter the number of columns : "))
# input the matrix 
for a in range (rows):
    c=[]
    q=[]
    for b in range (columns):
        d=int(input(f"Enter element {a+1},{b+1} : "))
        c.append(d)
        q.append(d)
    original_matrix.append(q)
    # create a bubble sort for the matrix
    g=len(c)
    for i in range (g):
        for j in range (0,g-i-1):
            if c[j]>c[j+1]:
                c[j],c[j+1]=c[j+1],c[j]
    sorted_matrix.append(c)
# print the original matrix 
print("The Original Matrix is : ")
for e in range (rows):
    for f in range (columns):
        print(original_matrix[e][f],end=" ")
    print()
# print the sorted matrix 
print("The Sorted Matrix is : ")
for h in range (rows):
    for k in range (columns):
        print(sorted_matrix[h][k],end=" ")
    print()
# add the original and sorted matrix
for l in range (rows):
    n=[]
    for m in range (columns):
            n.append(original_matrix[l][m]+sorted_matrix[l][m])
    adduct_matrix.append(n)
# print the adduct matrix
print("The Adduct Matrix is : ")
for o in range (rows):
    for p in range (columns):
        print(adduct_matrix[o][p],end=" ")
    print()
def BUBBLE_SORT (r):
    # BUBBLE SORT
    m=[]
    for i in range (r):
        a=int(input(f"Enter element {i+1} : "))
        m.append(a)
    n=len(m)
    for i in range (n):
        for j in range (0,n-i-1):
            if m[j]>m[j+1]:
                m[j],m[j+1]=m[j+1],m[j]
    print(m)

                


  
                