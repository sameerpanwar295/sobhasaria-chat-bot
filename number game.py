def get_valid_guess():
    "guess and ensures it is a valid integir"
    while True:
        try:
            guess = int(input("Enter the guess:"))
            return guess
        except ValueError:
            print("Invalid input please enter a whole number")