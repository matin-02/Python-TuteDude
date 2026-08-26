# if block is used to check the condition is true under the if block or not
# syntax of if
# indentation is important
#if condition:
#    statement1
#    statement2
#   ...
#    statement n
#statement

# The if block in Python executes a specific section of code only when a designated condition is true.
# It is the fundamental building block of decision-making in Python programs.
#  Anatomy of an if BlockEvery Python if block requires three distinct components:
# The if keyword to start the statement.
# A boolean condition followed immediately by a colon (:).
# An indented block of code underneath (traditionally 4 spaces).python

# example :-
age = int(input("What is your age? : "))

if age >= 18:
    print("You are adult. you can caste the Vote!!")
print("Sorry")