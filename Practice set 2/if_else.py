# 1.Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0 :
    print("The number is negative.")
else: 
    print("The number is zero.")

# Create a program that checks if a person is eligible to vote (age >= 18).
age =  int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".
if number % 2 == 0:
    print(number," is even.")
else:
    print( number,"is odd.")