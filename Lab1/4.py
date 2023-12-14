print(" You can use operators: +, -, *, /")
while True:
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
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
            res = a / b
        print("Result= ", res)
        ques = input("Do you wont to make some calculations? (y-yes): ")
        if ques.lower() != 'y':
            break
    except ValueError:
        print("Error! Please try again.")
