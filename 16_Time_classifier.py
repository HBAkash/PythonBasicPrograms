'''
 Time Classification: Write a Python program that takes the time in hours (24-hour format)
 as input and prints “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night” based on the time
'''

def timeclass(time):
    if 05.00 <= time <= 12.00:
        print("Good Morning")
    elif 12.01 <= time <= 18.00:
        print("Good Afternoon")
    elif 18.01 <= time <= 20.00:
        print("Good Evening")
    else:
        print("Good Night")

timeclass(07.00)
timeclass(11.55)
timeclass(02.25)
timeclass(17.25)
timeclass(03.25)
