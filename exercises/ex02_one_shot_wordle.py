"""One-Shot Wordle."""

__author__ = "730556346"

SECRET: str = ("python")
guess: str = input(f"What is your {len(SECRET)} letter guess? ")

while len(guess) != len(SECRET):  # your guess is the wrong length
    guess = input(f"That was not {len(SECRET)} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001f7E9"
YELLOW_BOX: str = "\U0001f7E8"

index: int = 0
emoji: str = ""

letter: bool = False
alt: int = 0

if letter is True: 
    emoji = emoji + GREEN_BOX

while index < len(SECRET):  # while the character being analyzed is indexed at less than the total letters in the secret word 
    if guess[index] == SECRET[index]: 
        emoji = emoji + GREEN_BOX
        # if the letter is correct and in the correct position, store a green box 
    else: 
        alt = 0
        letter = False
        while letter is False and alt < len(SECRET):  # the character guessed is not in the correct position but is correct
            if SECRET[alt] == guess[index]:
                emoji = emoji + YELLOW_BOX
                letter = True
            alt = alt + 1
        if letter is False:  # the character guessed is not in the secret word 
            alt = alt + 1
            emoji = emoji + WHITE_BOX
    index = index + 1 

print(emoji)

if guess == SECRET:  # the guess is the same as the secret word
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")


    
        
        
    


    
