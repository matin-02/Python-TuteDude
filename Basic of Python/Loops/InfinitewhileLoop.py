"""

correct_pass = ("Python")
while True:
    user_pass = input("Enter Your Password : Py")
    if user_pass == correct_pass:
        print("Correct Password")
        break
    else:
        print("Incorrect Password")
print("Logged in!")

"""
while True:
    print("Welcome to Python TuteDude!")