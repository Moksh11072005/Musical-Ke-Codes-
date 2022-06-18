#A
for row in range(6):
    for col in range(5):
        if ((col==0 or col==4) and (row!=0)) or ((row==0 or row==3) and (col>0 and col<4)):
            print("*",end='')
        else:
            print(end=' ')
    print()
#B
for row in range(7):
    for col in range(4):
        if (col==0 or (col==3 and (row!=0 and row!=6))) or ((row==0 or row==3 or row==6) and (col>0 and col<3)):
            print('*',end=' ')
        else:
            print(end='  ')
    print()
#C
for row in range(6):
    for col in range(4):
        if (col==0 and (row!=0 and row!=5)) or ((row==0 or row==5) and (col!=0)):
            print('*',end=' ')
        else:
            print(end='  ')
    print()
#D
for row in range(6):
    for col in range(4):
        if ((row==0 or row==5) and (col!=3)) or ((col==0 or col==3) and (row!=0 and row!=5)):
            print('*',end=' ')
        else:
            print(end='  ')
    print()    
#E
for row in range(7):
    for col in range(4):
        if ((row==0 or row==3 or row==6)) or ((col==0) and (row!=0 and row!=3 and row!=6)):
            print('*',end='')
        else:
            print(end=' ')
    print()
#F
for row in range(7):
    for col in range(4):
        if (col==0) or ((row==0 or row==3) and col!=0):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
#G
for row in range(7):
    for col in range(4):
        if (col==0 and (row!=0 and row!=6)) or ((row==0 or row==6) and (col!=0)) or (row==4 and (col!=0 and col!=1)) or ((row==5) and col>2) :
            print("*",end=" ")
        else:
            print(end="  ")
    print()
#H
for row in range(7):
    for col in range(4):
        if (col==0 or col==3) or (row==3 and (col>0 and col<3)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
#I
for row in range(7):
    for col in range(5):
        if (row==0 or row==6) or (col==2 and (row!=0 and row!=6)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
#J
for row in range(7):
    for col in range(4):
        if ((row==0 and col!=0) or (row==6 and col!=3)) or (col==2 and (row!=0 and row!=6)) or (row==5 and col<1):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
#K
row_val=0
col_val=3
for row in range(7):
    for col in range(4):
        if col==0 or row==col+3:
            print('*',end=' ')
        elif row==row_val and col==col_val:
            print('*',end='  ')
            row_val=row_val+1
            col_val=col_val-1
        else:
            print(end='  ')
    print()       
#L
for row in range(6):
    for col in range(4):
        if col==0 or row==5 and col!=0:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
#M
for row in range(6):
    for col in range(5):
        if col==0 or col==4 or row==col and col>0 and col<3 or col==3 and row==1:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
#N
for row in range(6):
    for col in range(6):
        if col==0 or col==5 or row==col and col!=0 and col!=5:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
#O
for row in range(5):
    for col in range(5):
        if ((row==0 or row==4) and 0<col<4) or ((col==0 or col==4) and 0<row<4):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
#P
for row in range(7):
    for col in range(5):
        if col==0 or ((row==0 or row==3) and col!=4) or col==4 and 0<row<3:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
#Q
for row in range(6):
    for col in range(5):
        if ((row==0 or row==4) and 0<col<4) or ((col==0 or col==4) and 0<row<4) or row==col+1 and col!=1:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
#R
for row in range(7):
    for col in range(5):
        if col==0 or ((row==0 or row==3) and col!=4) or col==4 and 0<row<3 or row==col+2:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
#S
for row in range(7):
    for col in range(4):
        if row==0 and col!=0 or row==6 and col!=3 or row==3 and 0<col<3 or col==0 and 0<row<3 or col==3 and 3<row<6:
            print("*",end=" ")
        else:
            print(end="  ")
    print()
#T
for row in range(6):
    for col in range(5):
        if row==0 or col==2 and row!=0:
            print("*",end=" ")
        else:
            print(end="  ")
    print()





