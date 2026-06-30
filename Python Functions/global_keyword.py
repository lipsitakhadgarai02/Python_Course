def sum(a,b):
    print("Hey i am adding")
    global z #this tells please modify global value of z and create a local varible
    z = 1
    c = a+b
    return c
z = 12
print(sum(2,3))
print(z)
