import random

correct = False
secret_word = {
    "easy": "apple",
    "medium": "desktop",
    "hard": "excavator"
}
difficulty = input("Difficulty: Type easy, medium, or hard ")
random_word = secret_word[difficulty]


while not correct:
    player_guess = input("Enter a letter: ")
    if player_guess == random_word:
        print("Congrats! You guessed the word!")
        correct = True
    if player_guess in random_word:
        print("Correct! The word contains ", player_guess )
        print()
    elif player_guess not in random_word:
        print("Wrong!")
        print()
        