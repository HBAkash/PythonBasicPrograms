#Variable Swap: Write a Python program to swap the values of two variables without using a temporary variable
def swap(A,B):
    (A,B) = (B,A)
    return A,B
print(swap(2,4))
print(swap(2,5))