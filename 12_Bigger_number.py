'''
Largest of Three Numbers: Write a Python program that takes three numbers as input
and prints the largest among them
'''
def largest(a,b,c):
    if a>b and a>c:
        print(f"{a} is the largest in the dataset of {a}, {b} and {c}")
    elif b>a and b>c:
        print(f"{b} is the largest in the dataset of {a}, {b} and {c}")
    else:
        print(f"{c} is the largest in the dataset of {a}, {b} and {c}")

largest(1,2,3)
largest(1,5,3)
largest(4,8,9)