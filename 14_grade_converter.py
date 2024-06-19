'''
Grades Classification: Write a Python program that takes a student’s percentage as input
and prints their corresponding grade according to the following criteria: –
90% or above: A+ – 80-89%: A – 70-79%: B – 60-69%: C – Below 60%: Fail
'''

def grade_converter(number):
    if number >= 90:
        print("A+")
    elif 80 <= number <= 89:
        print("A")
    elif 70<= number <= 79:
        print("B")
    elif 60<= number <= 69:
        print("C")
    else:
        print("F")


grade_converter(100)
grade_converter(75)
grade_converter(85)
grade_converter(63)
grade_converter(45)
grade_converter(0)
