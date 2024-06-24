'''
 Fibonacci Sequence: Write a Python program using a for loop to generate the Fibonacci sequence up to a given limit N.
'''

def fibonacci(digit):
    first_digit = 0
    second_digit = 1
    print(first_digit)
    print(second_digit)
    for i in range(digit+1):

        new = first_digit + second_digit
        first_digit = second_digit
        second_digit = new
        print(new)

fibonacci(6)
