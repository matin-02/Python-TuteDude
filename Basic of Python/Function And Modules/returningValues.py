def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

res = even_odd(10)
print(res)
print('-' * 100)

def add(num1, num2):
    res = num1 + num2
    return res

num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))
res = add(num1, num2)
print(f"The sum of {num1} and {num2} is {res}")

print('-' * 100)


def arthmetic(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    return addition, subtraction, multiplication

num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))
res1,res2,res3 = arthmetic(num1, num2)
print(f"Addition of {num1} and {num2} is {res1}")
print(f"Subtraction of {num1} and {num2} is {res2}")
print(f"Multiplication of {num1} and {num2} is {res3}")