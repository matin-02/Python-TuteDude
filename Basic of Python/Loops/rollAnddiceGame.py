"""
write a program to simulate a roll of a die/dice
A die has 6 faces with numbers 1 to 6 written on them
The program should randomly prints a number between 1 and 6
"""
import random
print("===========* Wel-Come to the Game of Roll A Dice *===========")
while True:
    choice = input("Press Enter to role the Dice or 'q' to Quit the Game ")
    if choice == 'q':
        print("Thank you for playing The Game")
        break

    elif choice == '' :
        number  = random.randint(1,6)
        print(f"Your number is {number}")
    else:
        print("Invalid Choice")

print("GAMER OVER!!!")

