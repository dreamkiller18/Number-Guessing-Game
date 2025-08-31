import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


secret_number = random.randint(1, 100) #Generates a random number between 1 and 100


for attempts in range(1, 11) : #user gets 15 chances to guess the correct option 
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too Low!")
    elif guess > secret_number:
        print("Too High!")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.") #this part runs if you have succesfully compleeted guessing the number completly
        break
else:
    # This runs if the player didn't guess the number within the attempts
    print(f"Sorry, you've used all your attempts. The number was {secret_number}.")

