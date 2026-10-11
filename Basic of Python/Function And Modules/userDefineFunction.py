# user define Function
# Syntax:-
"""
def function_name(ar1,ar2,ar3 ,...):
    statement 1
    statement 2
    statement 3
    ...
    statement N
"""

def Greeting_someone(name): # name is a agrument
    print(f"Hello {name} Good Morning")
    print("Its a beautiful day")

# calling a function
greeting = Greeting_someone("John")


def even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

num = int(input("Enter a number: "))
even_odd(num)

def add(a,b):
    res = a + b
    print(f"the sum of {a} and {b} is {res}")

a = int(input("Enter a number1: "))
b = int(input("Enter a number2: "))
add(a,b)
