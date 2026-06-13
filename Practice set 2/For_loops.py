# Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)
# Print the multiplication table of a number (entered by user).
n = int(input("Enter a number of which you want to know the table : "))
for j in range(1,11):
    print(f"{n} * {j} = {n*j}")

# Calculate the sum of all numbers from 1 to 100 using a for loop.
sum = 0
for i in range(1,101):
    sum += i
print("Sum of 1 to 100 is : ",sum)
# Print the following pattern using a for loop:
'''
*
**
***
****
'''
for j in range(1,5):
    for i in range (j):
        print('*',end="")
    print()