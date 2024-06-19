'''
Sum of N Numbers: Write a Python program using a for loop to
calculate the sum of the first N natural numbers, where N is taken as input from the user
'''

def sum(digit):
    sum = 0
    for i in range(digit+1):
        sum = sum + i
    print(sum)

sum(int(input("Enter the digit: ")))
sum(int(input("Enter the digit: ")))
sum(int(input("Enter the digit: ")))
