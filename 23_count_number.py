'''
Count Digits in a Number: Write a Python program using a while loop to count the number of digits in a given integer N.
125465
'''

def counter(digit):
    sums = 0
    while digit > 0:
        digit = digit // 10
        sums = sums + 1
    print(sums)

counter(148564)

