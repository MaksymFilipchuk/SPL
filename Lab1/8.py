import math
memoryres = []
print("\nYou can use operators: +, -, *, / ^, √, % \nNote: The square root is taken from the first entered number.")
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
                print("The operation is impossible! Try again.")
                continue
            res = a / b
        elif oper == '√':
            if a < 0:
                print("The operation is impossible! Try again. ")
                continue
            res = math.sqrt(a)

        print("Result=", res)
        ques3 = input("Do you want to save result in archive? (y-yes, n - no): ")
        if ques3.lower() == 'y':
            memoryres.append(res)
            print("The result successfully saved.")

        ques2 = input("Do you want to restore an archive? (y-yes, n - no): ")
        if ques2.lower() == 'y':
            if memoryres:
                print("Saved results:")
                for result in memoryres:
                    print(result)
            else:
                print("Archive is empty!")

        ques1 = input("Do you wont to make some calculations? (y-yes): ")
        if ques1.lower() != 'y':
            break
    except ValueError:
        print("The symbol isn't a number, Try again!")
