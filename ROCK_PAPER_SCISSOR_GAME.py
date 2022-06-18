# Rock Paper Scissor Game Against Your Computer
import random
rules=print("Rules:\n1  for 'Stone', 2  for 'Paper' and 3  for 'Scissor'\nYou will be having only 5 chances to play.\nGOOD LUCK!!!")
score=0
for i in range (5):
    ch=(1,2,3)
    user=int(input("---------------------\nenter your choice\n>>>"))
    computer=random.choice(ch)
    if user==computer:
        print("\nTIE (NO POINTS)")
        score=score+0
    elif user==1 and computer==2 :
        print('\n1 POINT TO COMPUTER')
        score=score+0    
    elif user==1 and computer==3 :
        print('\n1 POINT TO YOU')
        score=score+1    
    elif user==computer:
        print("\nTIE (NO POINTS)")
        score=score+0    
    elif user==2 and computer==1 :
        print('\n1 POINT TO YOU')
        score=score+1
    elif user==2 and computer==3 :
        print('\n1 POINT TO COMPUTER')
        score=score+0        
    elif user==3 and computer==2 :
        print('\n1 POINT TO YOU')
        score=score+1    
    elif user==3 and computer==3 :
        print('\nTIE (NO POINTS)')
        score=score+0
    elif user==3 and computer==1 :
        print('\n1 POINT TO COMPUTER')
        score=score+0    
    else:
        print("\nINVALID CHOICE PLEASE TRY AGAIN")
        break
    print("\ncomputer's choice\n>>>",computer)
print("\nYour Score is\n>>>",score,"/5")    
