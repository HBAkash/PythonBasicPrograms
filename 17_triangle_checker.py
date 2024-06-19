'''
Triangle Type Checker: Write a Python program that takes three sides of a triangle as input and determines whether
it forms an equilateral, isosceles, or scalene triangle.
'''

def triangle(a,b,c):
    if a==b==c:
        print("Equilateral triangle")
    elif (a==b) or (b==c) or (c==a):
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

triangle(10,10,10)
triangle(15,25,12)
triangle(12,5,12)

