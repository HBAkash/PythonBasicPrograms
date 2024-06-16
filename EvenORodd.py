#Even or Odd: Write a Python program that takes an integer as input and prints whether it is even or odd
def check(digit):
    if digit % 2 == 0:
        print("Even")
    else:
        print("Odd")
check(2)
check(5)
check(0)