'''
Factorial Calculator: Write a Python program using a while loop to calculate the factorial of a given number N.
'''
def factorial(digit):
    n = digit
    sum = 1
    while n > 0:
        sum *= n
        n = n-1
    print(f"The factorial of {digit} is {sum}")
factorial(5)