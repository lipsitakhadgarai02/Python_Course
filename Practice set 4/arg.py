'''Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".'''
def full_name(first , last):
    return f"{first} {last}"
print(full_name("Lipsita","Khadgarai"))


'''Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:
Both length and width
Only length (use default width)'''
def calculate_area(lenght,widht = 10):
    return lenght*widht
print(f"Area of the Rectangle is {calculate_area(2)}")
