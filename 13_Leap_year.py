'''
Leap Year Checker: Write a Python program that
takes a year as input and determines if it is a leap year or not
'''

def leap_year_checker(year):
    if year % 400 == 0:
        print(f"{year} is Leap year")
    elif year % 4 == 0 and year % 100 != 0 :
        print(f"{year} is Leap year")
    else:
        print(f"{year} is Not leap year")

leap_year_checker(2000)
leap_year_checker(2002)
leap_year_checker(2024)