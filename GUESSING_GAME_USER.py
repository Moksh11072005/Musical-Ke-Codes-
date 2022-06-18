# r = write any number below
r=1
rules=print("Rules:\nComputer will chose a random number between 1 and 10.\nYou will be having only 5 chances to answer.\nGOOD LUCK!!!")
for i in range (5):
    ur=int(input("Enter Your Number\n>>>"))
    if r==ur:
        print("YAY!!!, You guessed the number correctly ")
        break
    
else :
    print("You Lost!!!,Please try again")        
