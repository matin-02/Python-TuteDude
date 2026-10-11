# Task2 :- Using the Math Module For Calculations

import math
# Write a Python Program That :-
# 1.   Asks the user for a number as input.
n = int(input("enter a number : "))

# 2.   Uses the math module to calculate the:

# Square root of the number
print(f"The Square root : {math.sqrt(n)}")

# Natural logarithm (log base e) of the number
if n > 0:
    print(f"Logarithm : {math.log(n)}")

# Sine of the number (in radians)
    print(f"Sine : {math.sin(n)}")
