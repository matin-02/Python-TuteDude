# The if-elif-else block handles multiple mutually exclusive conditions in Python.
# It evaluates conditions in a top-down order and executes only the first block that evaluates to True.

# creating the mark grading System using the IF-ELIF-ELSE

mark = int(input("Enter mark: "))

if mark >= 90:
    print("Grade A")
elif 80 <= mark < 90:
    print("Grade B")
elif 70 <= mark < 80:
    print("Grade C")
elif 60 <= mark < 70:
    print("Grade D")
elif 50 <= mark < 60:
    print("Grade E")
else:
    print("Fail")

