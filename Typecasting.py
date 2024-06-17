'''
 Typecasting Challenge: Given three variables: `a = ‘100’`, `b = 25`, and `c = ‘10.5’`,
 write a Python program to perform the following operations and print the results: –
 Convert `a` to an integer and add it to `b`. – Convert `c` to a float and subtract
 it from the result of the first operation.
  – Convert the final result to a string and concatenate it with the string ” is the answer.”
'''
def typecast(a,b,c):
    a = int(a)
    b = b + a
    c = float(c)
    d = b - c
    e = str(d)
    print(f"{e} is the answer")

typecast(5,7,3)
