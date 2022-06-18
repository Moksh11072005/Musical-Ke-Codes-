# "16" CALCULATOR  ===>
print('press 2 for two digit calculator \nor\npress 3 for three digit calculator')
ch = int(input('press your choice\n>>>\n'))
while ch == 2:
    number1 = float(input("Enter your first number\n>>>\n"))
    number2 = float(input("Enter your second number\n>>>\n"))
    print('press "+" for addition')
    print('press "-" for subtraction')
    print('press "*" for multiplication')
    print('press "/" for division')
    choice = input('press your choice')
    if choice == '+':
        print("THE RESULT IS\n>>>\n", number1+number2)
        break
    elif choice == '-':
        print("THE RESULT IS\n>>>\n", number1-number2)
        break
    elif choice == '*':
        print("THE RESULT IS\n>>>\n", number1*number2)
        break
    elif choice == '/':
        print("THE RESULT IS\n>>>\n", number1/number2)
        break
    else:
        break
else:
    number1 = float(input("Enter your first number\n>>>\n"))
    number2 = float(input("Enter your second number\n>>>\n"))
    number3 = float(input("Enter your third number\n>>>\n"))
    choice = input(
        'enter your choice[ + , - , * , / , +- , +* , +/ , -+ , -* , -/ , *+ , *- , */ , /+ , /- , /* ]\n>>>\n')
    if choice == '+':
        print("THE RESULT IS\n>>>\n", number1+number2+number3)
    elif choice == '-':
        print("THE RESULT IS\n>>>\n", number1-number2-number3)
    elif choice == '*':
        print("THE RESULT IS\n>>>\n", number1*number2*number3)
    elif choice == '/':
        print("THE RESULT IS\n>>>\n", number1/number2/number3)
    elif choice == '+-':
        print("THE RESULT IS\n>>>\n", number1+number2-number3)
    elif choice == '+*':
        print("THE RESULT IS\n>>>\n", number1+number2*number3)
    elif choice == '+/':
        print("THE RESULT IS\n>>>\n", number1+number2/number3)
    elif choice == '-+':
        print("THE RESULT IS\n>>>\n", number1-number2+number3)
    elif choice == '-*':
        print("THE RESULT IS\n>>>\n", number1-number2*number3)
    elif choice == '-/':
        print("THE RESULT IS\n>>>\n", number1-number2/number3)
    elif choice == '*+':
        print("THE RESULT IS\n>>>\n", number1*number2+number3)
    elif choice == '*-':
        print("THE RESULT IS\n>>>\n", number1*number2-number3)
    elif choice == '*/':
        print("THE RESULT IS\n>>>\n", number1*number2/number3)
    elif choice == '/+':
        print("THE RESULT IS\n>>>\n", number1/number2+number3)
    elif choice == '/-':
        print("THE RESULT IS\n>>>\n", number1/number2-number3)
    elif choice == '/*':
        print("THE RESULT IS\n>>>\n", number1/number2*number3)
