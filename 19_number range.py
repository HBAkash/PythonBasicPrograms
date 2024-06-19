'''
Number Ranges: Write a Python program that takes an integer as input and prints whether the number falls within the ranges:
0-50, 51-100, 101-150, or above 150.
'''

def ranges(digit):
    if digit >=0:
        if 0<= digit <= 50:
            print("It falls in the ranges of 0 to 50")
        elif 51 <= digit <=100:
            print("It falls in the ranges of 51 to 100")
        elif 101 <= digit <= 150:
            print("It falls in the ranges of 101 to 150")
        else:
            print("Above 150")
    else:
        print("Give positive integer as input")

ranges(-45)
ranges(0)
ranges(42)
ranges(151)
