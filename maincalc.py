import math
##///Simple Area-Perimeter Calculator///
# 1 - Greet the user using a greet() function
def greet():
    """ Simple Greeting for the user """
    print("Hello and welcome to the area/priemeter calculator!")
greet()
#2 - make the user select desired shape
shapes = ['Triangle','Square','Rectangle']
shape = int(input("Which shape do you want? '0' for triangle , '1' for square and '2' for rectangle.\n"))
#3 - ask the user which calculation process they want
process = input(f"which calculation for the {shapes[shape]} do you want? 'a' for Area , 'p' for Perimeter.\n")
#4 - calculate
if shape == 0 and process == 'a':
    height = int(input("Please enter your triangle's height\n"))
    base = int(input("Please enter your triangle's base length\n"))
    area = 0.5 * base * height
    print(f"Your triangle's area = {area}")
elif shape == 0 and process == 'p':
    side1 = int(input("Please enter the length of the first side\n"))
    side2 = int(input("Please enter the length of the second side\n "))
    base = int(input("Please enter the length of the base\n"))
    Perimeter  = side1 + side2 + base
    print(f"Your triangle's priemeter is {Perimeter}")
elif shape == 1 and process == 'a':
    side = int(input("Please enter the side length of your squaren\n"))
    area = side * side
    print(f"Your square's area is {area}")
elif shape == 1 and process == 'p':
    side = int(input("Please enter the side length of your square\n"))
    Perimeter = 4 * side
    print("Your square's priemeter is {Perimeter}")
elif shape == 2 and process == 'a':
    width = int(input("Please enter the width of your rectangle\n"))
    length = int(input("Please enter the length of your rectangle\n"))
    area = width * length
    print(f"Your rectangle's area is {area}'")
elif shape == 2 and process == 'p':
    width = int(input("Please enter the width of your rectangle\n"))
    length = int(input("Please enter the length of your rectangle\n"))
    Perimeter = (width + length) * 2
    print(f"Your rectangle's Perimeter is {Perimeter}")
else:
    # For invalid inputs like random words,etc.
    print("Error , please make sure you put valid input")

