word = input("Enter Your Word\n>>>")
for i in word:
    if i == "a" or i == "A":
        for row in range(6):
            for col in range(5):
                if ((col == 0 or col == 4) and (row != 0)) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
                    print("*", end='')
                else:
                    print(end=' ')
            print()
        print("\n")
    elif i == "B" or i == "b":
        for row in range(7):
            for col in range(4):
                if (col == 0 or (col == 3 and (row != 0 and row != 6))) or ((row == 0 or row == 3 or row == 6) and (col > 0 and col < 3)):
                    print('*', end=' ')
                else:
                    print(end='  ')
            print()
        print("\n")
    elif i == "C" or i == "c":
        for row in range(6):
            for col in range(4):
                if (col == 0 and (row != 0 and row != 5)) or ((row == 0 or row == 5) and (col != 0)):
                    print('*', end=' ')
                else:
                    print(end='  ')
            print()
        print("\n")
    elif i == "D" or i == "d":
        for row in range(6):
            for col in range(4):
                if ((row == 0 or row == 5) and (col != 3)) or ((col == 0 or col == 3) and (row != 0 and row != 5)):
                    print('*', end=' ')
                else:
                    print(end='  ')
            print()
        print("\n")
    elif i == "E" or i == "e":
        for row in range(7):
            for col in range(4):
                if ((row == 0 or row == 3 or row == 6)) or ((col == 0) and (row != 0 and row != 3 and row != 6)):
                    print('*', end='')
                else:
                    print(end=' ')
            print()
        print("\n")
    elif i == "F" or i == "f":
        for row in range(7):
            for col in range(4):
                if (col == 0) or ((row == 0 or row == 3) and col != 0):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()
        print("\n")
    elif i == "G" or i == "g":
        for row in range(7):
            for col in range(4):
                if (col == 0 and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col != 0)) or (row == 4 and (col != 0 and col != 1)) or ((row == 5) and col > 2):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()
        print("\n")
    elif i == "H" or i == "h":
        for row in range(7):
            for col in range(4):
                if (col == 0 or col == 3) or (row == 3 and (col > 0 and col < 3)):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()
        print("\n")
    elif i == "I" or i == "i":
        for row in range(7):
            for col in range(5):
                if (row == 0 or row == 6) or (col == 2 and (row != 0 and row != 6)):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()
        print("\n")
    elif i == "J" or i == "j":
        for row in range(7):
            for col in range(4):
                if ((row == 0 and col != 0) or (row == 6 and col != 3)) or (col == 2 and (row != 0 and row != 6)) or (row == 5 and col < 1):
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()
        print("\n")
    elif i == "K" or i == "k":
        row_val = 0
        col_val = 3
        for row in range(7):
            for col in range(4):
                if col == 0 or row == col+3:
                    print('*', end=' ')
                elif row == row_val and col == col_val:
                    print('*', end='  ')
                    row_val = row_val+1
                    col_val = col_val-1
                else:
                    print(end='  ')
            print()
        print("\n")
    elif i == "L" or i == "l":
        for row in range(6):
            for col in range(4):
                if col == 0 or row == 5 and col != 0:
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()
        print("\n")
    elif i == "M" or i == "m":
        for row in range(6):
            for col in range(5):
                if col == 0 or col == 4 or row == col and col > 0 and col < 3 or col == 3 and row == 1:
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()
        print("\n")
    elif i == "N" or i == "n":
        for row in range(6):
            for col in range(6):
                if col == 0 or col == 5 or row == col and col != 0 and col != 5:
                    print("*", end=" ")
                else:
                    print(end="  ")
            print()
        print("\n")
