import math
memoryres = []
print("\nYou can use operators: +, -, *, / ^, √, % "
      "\nNote: The square root is taken from the first entered number.")
while True:
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        oper = input("Enter operator: ")

        if oper not in ('+', '-', '*', '/', '%', '^', '√', 'M','R'):
            print("Error! Enter valid operator: ")
            continue

        if oper == '+':
            res = a + b
        elif oper == '-':
            res = a - b
        elif oper == '*':
            res = a * b
        elif oper == '%':
            res = a % b
        elif oper == '^':
            res = a ** b
        elif oper == '/':
            if b == 0:
                print("Operation is not correct. Try again.")
                continue
            res = a / b
        elif oper == '√':
            if a < 0:
                print("The operation is impossible! Try again. ")
                continue
            res = math.sqrt(a)

        expression = f"{a} {oper} {b}"
        memoryres.append((expression, res))

        print("Result=", res)

        ques2 = input("Do you want to open journal? (y-yes, n - no): ")
        if ques2.lower() == 'y':
            if memoryres:
                print("Journal of calculations:")
                for i, (expression, result) in enumerate(memoryres, start=1):
                    print(f"{i}. {expression} = {result}")
            else:
                print("Journal is empty!")

        ques1 = input("Do you wont to make some calculations? (y-yes): ")
        if ques1.lower() != 'y':
            break
    except ValueError:
        print("The symbol isn't a number, Try again!")
