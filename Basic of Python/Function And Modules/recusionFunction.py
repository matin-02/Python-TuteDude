"""
Recursion is a process in which a function calls itself till a certain is not met
there are 2 parts to any recursive function
1. Base/terminal condition
2. Recursive condition
"""

# factorial of n == n * (n - 1) * (n - 2) * ... 2 * 1
# n!

print("without recursion")
def fact(num):
    facto = 1
    while num > 1:
        facto *= num
        num -= 1

    return facto

n = int(input("enter a number : "))
print(fact(n))

print("*=*" * 100)

print("without recursion")
print("*=*" * 100)

def fact1(num):

     if num == 1:
         return 1
     else:
         return  num * fact1(num - 1)

num = int(input("enter a number : "))
print(fact1(num))