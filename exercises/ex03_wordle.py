"""Structured Wordle"""
__author__ = "730556346"

def contains_char(parameter: str, character: str) -> bool: 
    """Searching for a character."""
    assert len(character) == 1. 
    index: int = 0 
    while index < len(parameter): 
        if parameter[index] == character:
            return True 
        else: 
            index = index + 1
    return False

def emojified(guessprmtr: str, secretprmtr: str) -> str: 
    """Developing an emoji string."""
    assert len(guessprmtr) == len(secretprmtr)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    indextwo: int = 0 
    emojis: str = ""
    while indextwo < len(secretprmtr):
        if guessprmtr[indextwo] == secretprmtr[indextwo]: 
            emojis = emojis + GREEN_BOX
            indextwo = indextwo + 1
        else: 
            if contains_char(secretprmtr, guessprmtr[indextwo]) is True: 
                emojis = emojis + YELLOW_BOX
                indextwo = indextwo + 1
            else: 
                emojis = emojis + WHITE_BOX 
                indextwo = indextwo + 1
    return emojis

def input_guess(guessint: int) -> str:
    """Making a guess."""
    SECRET: str
    guess: str = input(f"Enter a {guessint} character word: ")
    while guessint != len(guess): 
        guess = input(f"That wasn't {guessint} chars! Try again: ")
    return guess

def main() -> None: 
    """The entrypoint of the program and main game loop."""
    SECRET: str = "codes"
    game_loop: bool = True 
    turn: int = 1 
    while turn < 7 and game_loop is True: 
        print(f"=== Turn {turn}/6 ===")
        guess: str = (input_guess(len(SECRET)))
        print(emojified(guess, SECRET))

        if guess == SECRET: 
            print(f"You won in {turn}/6 turns!")
            game_loop = False
        turn = turn + 1
        if turn == 7: 
            print ("X/6 - Sorry, try again tommorow!")
            game_loop = False 

if __name__ == "__main__": 
    main()


