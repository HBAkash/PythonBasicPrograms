'''
Table of a Number: Write a Python program using a for loop to print the multiplication table of a given number N.
'''

def multiplication_talbe(n):
    for i in range(1,11):
        print(f'{i} X {n} = {i*n}')\

multiplication_talbe(7)