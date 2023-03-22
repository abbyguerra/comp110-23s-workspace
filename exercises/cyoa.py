"""Guessing the side of a coin."""

__author__ = "730556356"


import random 

# Globals 
points: int = 0 
player: str = ""

# Constants 
EMOJI_COIN = "\U0001FA99"
EMOJI_HEADS = "\U0001f1ED"
EMOJI_TAILS = "\U0001F1F9"


def main() -> None:
    """The function that runs the guessing game."""
    greet()
    loop()


# Greeting procedure
def greet() -> None: 
    """Greeting the player and asking for their name."""
    global player
    player: str = input("Before we begin, what is your name? ")
    print(f"Welcome {player}! In this game you will be asked to guess the correct side of coin before it is flipped entering either 'h' or 't'.\n ")
    return None
    

# Function for coin flip 
def coin_flip(points: int) -> int:
    """Asks the player for their guess, flips a coin, and updates their score accordingly."""
    guess: str = input(f"\n{player}, please guess if the coin will land on heads ({EMOJI_HEADS}) or tails ({EMOJI_TAILS})")
    if guess != "heads" and guess != "tails": 
        print("Invalid input. Please enter 'heads' or 'tails. ")
        return coin_flip(points)
    result: str = random.choice(["heads", "tails"])
    print(f"The coin landed on {result} {EMOJI_COIN}")
    if result == guess: 
        points += 1
        print(f"You guess was correct! Your score is currently {points}!\n")
        return points
    if result != guess: 
        points = points
        print(f"Your guess was incorrect. Sorry! Your score is currently {points}.\n")
    
    
# Custom function
def more(correct_number: int) -> None:
    """Asks the user to guess a number, gives them 3 attempts, and updates their score accordingly."""
    global points
    print(f"\n{player}, let's try something different.\n")
    print("Please guess a number between 1 and 10. You will have 3 guesses and each incorrect guess will deduct 1 point from your total score.")
    correct_number: int = random.randint(1, 10)
    for i in range(3): 
        guess = int(input(f"Attempt {i+1}: "))
        if guess == correct_number: 
            points += 1
            print(f"Congratulations, your guess is correct! Your score is now {points}!")
            return
        else:
            points -= 1
    else:
        print(f"Sorry, you did not guess the correct number in 3 guesses. Your final score is {points}.")


# Game loop
def loop(choice: int) -> None:
    """Asks the player to choose an action running the main game loop."""
    global points
    while True: 
        print("What would you like to do next?\n1. Guess the side of the coin\n2. Additional interaction\n3. Quit the game\n ")
        choice: int = input("Enter the number of your choice: ")
        if choice == "1": 
            points = coin_flip(points)
        if choice == "2": 
            more()
        if choice == "3":
            print(f"\n Thanks for playing {player}! Your final score is {points}. Good job!")
            return 
        

if __name__ == "__main__":
    main()