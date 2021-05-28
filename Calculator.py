# -----------------------------
# ----- Simple Calculator -----
# ----- By: Ali Samir Ali -----
# -----------------------------

import math


def display():
    print("------------------------------------------------")
    print("Please, Choose An Operation From The Next List: ")
    print("- Addition => +")
    print("- Subtraction => -")
    print("- Multiplication => *")
    print("- Division => /")
    print("- Modules => %")
    print("- Power => p")
    print("- Square Root => r")
    print("- Factorial => f")
    print("- Exit => 0")
    print("------------------------------------------------")
    print("Enter Your Choice: ")


def run_program():
    print("Welcome to my simple calculator :)")
    display()

    while True:
        operation = input()

        if operation == '0':
            print("Thanks For Using My Program\nGood Bye :)")
            break
        else:
            if operation == '+':
                number_1 = float(input("Enter 1st Number: "))
                number_2 = float(input("Enter 2nd Number: "))
                print(number_1, " + ", number_2, " = ", (number_1 + number_2))
            elif operation == '-':
                number_1 = float(input("Enter 1st Number: "))
                number_2 = float(input("Enter 2nd Number: "))
                print(number_1, " - ", number_2, " = ", (number_1 - number_2))
            elif operation == '*':
                number_1 = float(input("Enter 1st Number: "))
                number_2 = float(input("Enter 2nd Number: "))
                print(number_1, " * ", number_2, " = ", (number_1 * number_2))
            elif operation == '/':
                number_1 = float(input("Enter 1st Number: "))
                number_2 = float(input("Enter 2nd Number: "))
                print(number_1, " / ", number_2, " = ", (number_1 / number_2))
            elif operation == '%':
                number_1 = float(input("Enter 1st Number: "))
                number_2 = float(input("Enter 2nd Number: "))
                print(number_1, " % ", number_2, " = ", (number_1 % number_2))
            elif operation == 'p':
                base = float(input("Enter Base Number: : "))
                exponent = float(input("Enter Exponent Number: "))
                print("Result = ", math.pow(base, exponent))
            elif operation == 'f':
                number = int(input("Enter A Number: "))
                print("Result = ", math.factorial(number))
            elif operation == 'r':
                num = int(input("Enter A Number: "))
                print("Result = ", math.sqrt(num))
            else:
                print("Please Choose A Correct Operation :|")
        display()


run_program()
