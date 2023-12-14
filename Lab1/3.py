print(" You can use operators: +, -, *, /")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
while True:
    oper = input("Enter the operator: ")
    if oper not in ('+', '-', '*', '/'):
        print("Error! Enter a operator isn't correct: ")
        continue
    if oper == '+':
        res = a + b
    elif oper == '-':
        res = a - b
    elif oper == '*':
        res = a * b
    elif oper == '/':
        res = a / b
    print("Result=", res)
    break
