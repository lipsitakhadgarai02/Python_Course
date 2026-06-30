'''Write a lambda function that adds two numbers and test it.'''
a = lambda x,y : x+y
print(a(2,3))

'''Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.'''
l = [1, 2, 3, 4, 5]
s = list(map(lambda x : x*x,l))
print(s)
