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
