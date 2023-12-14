print(" You can use operators: +, -, *, /")
while True:
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        oper = input("Enter operator: ")

        if oper not in ('+', '-', '*', '/'):
            print("Error! Please enter correct operator: ")
            continue

        if oper == '+':
            res = a + b
        elif oper == '-':
            res = a - b
        elif oper == '*':
            res = a * b
        elif oper == '/':
            if b == 0:
                print("You cant devide into zero! Try again.")
                continue
            res = a / b
        print("Result= ", res)
        ques = input("Do you wont to make some calculations? (y-yes): ")
        if ques.lower() != 'y':
            break
    except ValueError:
        print("The symbol isn't a number, Try again!")
