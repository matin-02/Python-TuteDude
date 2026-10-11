# .py file is a module
# Built -in modules
# math , radom , datetime,...

# how to import a module in python
# syntax: - import module_name
# syntax for importing only few functions/variables: from module_name import f1,f2,f3

import math as  m
a: int = int(input("Enter a number: "))
# calculate the square root of a number

print(m.sqrt(a))

r = int(input("Enter a radius: "))
area = m.pi * (r ** 2)
print(f"Area of the Circle is {area} and radius is {r}")
print(m.pi)

# another way to import
from random import randint
value = randint(1, 10)
print(f"The random number is {value}")