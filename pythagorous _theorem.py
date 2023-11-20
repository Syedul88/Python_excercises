
first_value = int(input("value 1: "))
second_value = int(input("value 2: "))
third_value = int(input("value 3: "))

def hypo():
    if first_value**2 + second_value**2 == third_value**2 or first_value**2 + third_value**2 == second_value**2 or second_value**2 + third_value**2 == first_value**2:
        print("This is a pythagorous theorem")
    else:
        print("This is not a pythagorous theorem")
hypo()

# alternative

import math

def hypo(side1, side2):
    hypotenious = math.sqrt(side1**2 + side2**2)
    print("hypotenious: ", hypotenious)

hypo(3,4)
hypo(4,5)