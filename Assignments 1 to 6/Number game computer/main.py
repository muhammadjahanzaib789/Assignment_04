import random

# Introduction
number = random.randint(1,100)
guesses = 0

while True:
    # User se input take
    user_guess = input("Enter your guess:")

    # Input ko integer main convert karna
    try:
        user_guess = int(user_guess)
        guesses += 1

        # Guess k check karna
        if user_guess < number:
            print("Too low! Try again")
        elif user_guess > number:
            print("Too high! Try again")
        else:
            print(f"Congratulations! You guessed the number in {guesses} tries.")
            break
    except ValueError:
        print("Please enter a valid number")
