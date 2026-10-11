# Task 1 : - Calculate Factorial Using a Function

# problem Statement : - Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and
# calculates its factorial using a loop or recursion.

def Factorial(n):
    fact = 1
    for i in range(1 , n + 1):
        fact = fact * i

    # 2.   Returns the calculated factorial.
    return fact

# 3.   Calls the function with a sample number and prints the output.
n = int(input("enter a number : "))
print(Factorial(n))

