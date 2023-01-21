"""EX01 - Chardle - A cute step toward Wordle"""

__author__ = "730556346"

word: str = input ("Enter a 5-character word: ")
if len(word) != 5: 
    print ("Error: Word must contain 5 characters")
else:
    character: str = input("Enter a single character: ")
    print("Searching for " + character + " in " + word)
    counter: int = 0

    if (character == word [0]): 
        print (character + " found at " + "index 0")
        counter+=1
    if (character == word [1]):
        print (character + " found at " + "index 1")
        counter+=1
    if (character == word [2]):
        print (character + " found at " + "index 2")
        counter+=1
    if (character == word [3]):
        print (character + " found at " + "index 3")
        counter+=1
    if (character == word [4]):
        print (character + " found at " + "index 4")
        counter+=1

    if counter ==0: 
        print ("No instances of " + character + " found in " + word)
    else: 
        print(str(counter) + " instances of " + character + " found in " + word)







