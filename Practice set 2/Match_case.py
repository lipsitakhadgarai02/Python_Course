# Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.
day = int(input("Enter a day number : "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Fryday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Day number please enter a correct day number!!")
'''
 Write a program using match case that simulates a simple calculator.

 Ask the user for two numbers and an operation (+, -, *, /).
 Perform the operation using match case.
 '''
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
op = input("Choose your operator(+, -, *, /,**,%) : ")
match op:
    case '+':
        print(f"Sum : {num1+num2}")
    case '-':
        print(f"Differnce : {num1-num2}")
    case '*':
        print(f"Product : {num1*num2}")
    case '/':
        print(f"Division : {num1/num2}")
    case '%':
        print(f"Reminder : {num1%num2}")
    case '**':
        print(f"Power {num1**num2}")
    case _:
        print("PLEASE ENTER A VALID OPERATION")