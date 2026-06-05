import random

def get_valid_guess():
    # "guess and ensures it is a valid integer"
    while True:
        try:
            guess = int(input("Enter your guess:"))
            return guess
        except ValueError:
            print(" Not correct. TRY AGAIN")


def play_game():
    "Runs a single round of the number guessing game"
    print(" THE GAME IS STARTED")
    print("I'm thinking of a number between 1 and 200")
    
    secret_number = random.randint(1, 50)
    attempts = 0
    
    while True:
        guess = get_valid_guess()
        attempts += 1
        
        if guess < secret_number:
            print(" Too low! Try a higher number")
        elif guess > secret_number:
            print(" Too high! Try a lower number")
        else:
            print("Correct! You guessed the number in {attempts} attempts")

            break

def main():
    # """Main loop to handle game initialization and replays."""
    print(" Welcome to the Number Guessing Game")
    
    while True:
        play_game()
        
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay not in ['yes']:
            print("Thanks for playing! Goodbye")
            break

main()