# A nested if statement occurs when you place a conditional block inside another conditional block.
# This allows you to check secondary conditions only after a primary condition has already proven true.

# create a program to for grading System of marks check the marks if the student is pass then
# allow the grading system , if student is fail then don't allow the grading system

mark = int(input("Enter Mark: "))
if mark >= 60:
    print("congrats your passed")

    if mark >= 90:
        print("Grade A")
    elif 80 <= mark < 90:
        print("Grade B")
    elif 70 <= mark < 80:
        print("Grade C")
    else:
        print("Grade D")

else:
    print("you have fail, study more next time")
