"""Guessing the side of a coin."""

__author__ = "730556356"


import random 

# Globals 
POINTS: int = 0 
PLAYER: str = ""

# Constants 
EMOJI_COIN = "\U0001FA99"
EMOJI_HEADS = "\U0001f1ED"
EMOJI_TAILS = "\U0001F1F9"


def flip() -> None:
    """Simulates a coin flip."""
    return random.choice(['heads', 'tails'])


def main() -> None:
    """The function that runs the guessing game."""
    greet()
    loop()


# Greeting procedure
def greet() -> None: 
    """Greeting the player and asking for their name."""
    global PLAYER
    PLAYER: str = input("Before we begin, what is your name? ")
    print(f"Welcome {PLAYER}! In this game you will be asked to guess the correct side of coin before it is flipped entering either 'h' or 't'.\n ")
    return None
    

# Function for coin flip 
def coin_flip(POINTS: int) -> int:
    """Asks the player for their guess, flips a coin, and updates their score accordingly."""
    guess = input(f"\n{PLAYER}, please guess if the coin will land on heads ({EMOJI_HEADS}) or tails ({EMOJI_TAILS})")
    if guess != "heads" and guess != "tails": 
        print("Invalid input. Please enter 'heads' or 'tails. ")
        return coin_flip(POINTS)
    result = random.choice(["heads", "tails"])
    print(f"The coin landed on {result} {EMOJI_COIN}")
    if result == guess: 
        POINTS += 1
        print(f"You guess was correct! Your score is currently {POINTS}!\n")
        return POINTS
    if result != guess: 
        POINTS = POINTS
        print(f"Your guess was incorrect. Sorry! Your score is currently {POINTS}.\n")
    
    
# Custom function
def more() -> None:
    """Asks the user to guess a number, gives them 3 attempts, and updates their score accordingly."""
    global POINTS
    print(f"\n{PLAYER}, let's try something different.\n")
    print("Please guess a number between 1 and 10. You will have 3 guesses and each incorrect guess will deduct 1 point from your total score.")
    correct_number = random.randint(1, 10)
    for i in range(3): 
        guess = int(input(f"Attempt {i+1}: "))
        if guess == correct_number: 
            POINTS += 1
            print(f"Congratulations, your guess is correct! Your score is now {POINTS}!")
            return
        else:
            POINTS -= 1
    else:
        print(f"Sorry, you did not guess the correct number in 3 guesses. Your final score is {POINTS}.")


# Game loop
def loop() -> None:
    """Asks the player to choose an action running the main game loop."""
    global POINTS 
    while True: 
        print("What would you like to do next?\n1. Guess the side of the coin\n2. Additional interaction\n3. Quit the game\n ")
        choice = input("Enter the number of your choice: ")
        if choice == "1": 
            POINTS = coin_flip(POINTS)
        if choice == "2": 
            more()
        if choice == "3":
            print(f"\n Thanks for playing {PLAYER}! Your final score is {POINTS}. Good job!")
            return 
        

if __name__ == "__main__":
    main()