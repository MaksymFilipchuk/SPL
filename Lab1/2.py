print(" You can use operators: +, -, *, /")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
while True:
    oper = input("Enter the operator: ")
    if oper in ('+', '-', '*', '/'):
        print("Entered: the first number: ", a, ";Entered: the second number: ", b, "; Operator: ", oper)
        break
    else:
        print("Error! Enter a operator isn't correct: ")
