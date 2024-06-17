#String Concatenation: Write a Python program that takes two strings as input and concatenates
# them into a single string without using the `+` operator

def concat(str1,str2):
    print(f"{str1} {str2}") #method 1
    print("{} {}".format(str1,str2) )#method 2
    print(" ".join([str1,str2]) )#method 3


concat("Hello", "Hridoy")
