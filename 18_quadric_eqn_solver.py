'''
 Quadratic Equation Solver: Write a Python program that takes the coefficients (a, b, c) of a quadratic equation as input
 and calculates and prints the real roots (if they exist) or a message indicating the complex roots.
'''
import math
def quad(a,b,c):
    determinent = (b)**2 - 4*a*c

    if determinent == 0:
        root = (-b) / (2*a)
        print(root)

    elif determinent > 0:
        roots_1 = (-b) + math.sqrt(determinent) / (2*a)
        roots_2 = (-b) - math.sqrt(determinent) / (2*a)
        print(f"root1 : {roots_1} \n root2: {roots_2}")

    else:
        root = (-b) / (2 * a)
        imag = math.sqrt(-determinent)/ (2*a)
        print(f"The root is {root} ± {imag:.2f}i ")




quad(1, -5, 6)
quad(1, -4, 4)
quad(1, 2, 5) 