# The if-else block handles binary decisions in Python.
# It executes one block of code when a condition is true,
# and an alternate block of code when that condition is false.
# Syntax :-

#if condition:
    # block  of code to be execute when the condition True
#else:
    # block  of code to be execute when the condition is False

age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to vote")
else:
    age = 18 - age
    print(f"You need {age } more years to vote")

# Write the program to check the number is even or odd

a = int(input("Enter a number: "))

if a % 2 == 0:
    print("Even")
else:
    print("Odd")