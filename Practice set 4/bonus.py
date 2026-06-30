# Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.
def fib(k):
    if k <= 1:
        return k
    return fib(k - 1) + fib(k - 2)

def fibonacci(n):
    '''
    Print the first n Fibonacci numbers using recursion.
    '''
    for i in range(n):
        print(fib(i), end=" ")

# Example usage
fibonacci(10)
# Prints: 0 1 1 2 3 5 8 13 21 34
print()
print(fib(4))

# Write a function safe_divide(a, b) that returns the result of a / b,
# but returns "Cannot divide by zero" if b is 0.
def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
print(safe_divide(3,4))

import module
print(module.even(4))
