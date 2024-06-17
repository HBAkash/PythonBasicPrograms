#Positive, Negative, or Zero: Write a Python program that takes a number as
# input and prints whether it is positive, negative, or zero

def even_odd_zero(digit):
    if digit == 0:
        print("Zero")
    elif digit % 2 == 0:
        print("Even")
    elif digit % 2 != 0:
        print("Odd")

even_odd_zero(0)
even_odd_zero(3)
even_odd_zero(4)




