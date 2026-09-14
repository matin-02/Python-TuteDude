"""
Create a simple number guessing game.
The user get 10 chances to guess a number.
if the user guesses the number before 10 chance , stop asking the number from the user, say congrats and end the game
if the user never guesses the number , ask them 10 times and then end the game!!
"""

num = 1
print("WELCOME TO THE NUMBER GUESSING GAME . We have a number that needs to be guessed. you have 10 attempts.")
print("The secret number is Between 1 and 50")
secret_number = 25
attempts = 10
if_guess_correct = False

while num <= 10:

    print(f"You Have {attempts} attempts remaining.")
    user_number = int(input("Enter your guess: "))

    if user_number == secret_number:
        print("Congratulations, you guessed the secret number!")
        if_guess_correct = True
        break

    else:
        if user_number < secret_number:
            higher_or_lower = "higher"
            print(f"Sorry , Your guess is Wrong ! Try {higher_or_lower} number.")

        else:
            higher_or_lower = "lower"
            print(f"Sorry , Your guess is Wrong ! Try {higher_or_lower} number.")

    num += 1
    attempts -= 1

if not if_guess_correct:
    print("Bad Luck!! You exhausted all your attempts and couldn't guess the secret number.")
print(f"The secret number was {secret_number} . Game Over")