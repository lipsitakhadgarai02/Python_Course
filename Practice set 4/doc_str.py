'''Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across function calls.'''
def increment():
    a = 0
    a = a+1
    print(a)
increment()
increment()
increment()

'''Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.'''
def multiply(a,b):
    ''' This function takes two intergeric number as a input
    a : Intergeric value
    b : Intergeric value
    it reutrns a int value which is product of two input number that is a * b
    '''
    return a*b
print(multiply.__doc__)
help(multiply)
