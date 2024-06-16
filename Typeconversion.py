# Type Conversion: Given a list of integers, write a Python program to
# convert each element of the list to a string

def inttostr(lst):
    lst2 = []
    for i in lst:
        lst2.append(str(i))
    print(lst2)

inttostr([1,2,3,4,5])
inttostr([10,20,30,45,85])
