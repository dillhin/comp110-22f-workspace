"""EX01 - Chardle: practicing the conceptual tools of Wordle"""
__author__ = 730568677

number_of_matches: int = 0
word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else:   
    character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character")
    exit()
else:
    print("Searching for " + character + " in " + word)
if character == word[0]:
    number_of_matches: int = number_of_matches + 1
    print(character + " found at index 0")
if character == word[1]:
    number_of_matches: int = number_of_matches + 1
    print(character + " found at index 1")
if character == word[2]:
    number_of_matches: int = number_of_matches + 1
    print(character + " found at index 2")
if character == word[3]:
    number_of_matches: int = number_of_matches + 1
    print(character + " found at index 3")
if character == word[4]:
    number_of_matches: int = number_of_matches + 1
    print(character + " found at index 4")

if number_of_matches == 0:
    print("No instances of " + character + " found in " + word)
if number_of_matches == 1:
    print(str(number_of_matches) + " instance of " + character + " found in " + word)
if number_of_matches > 1:
    print(str(number_of_matches) + " instances of " + character + " found in " + word)