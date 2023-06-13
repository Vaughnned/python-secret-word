import random

attempts = 6
correct = False
secret_word = {
    "easy": "apple",
    "medium": "desktop",
    "hard": "excavator"
}
difficulty = input("Difficulty: Type easy, medium, or hard ")
random_word = secret_word[difficulty]


while not correct and attempts > 0:
    player_guess = input("Enter a letter: ")
    if player_guess == random_word:
        print("Congrats! You guessed the word!")
        correct = True
    if player_guess in random_word:
        print("Correct! The word contains ", player_guess )
        print()
    elif player_guess not in random_word:
        print("Wrong!")
        attempts = attempts - 1
        print("Attempts remaining: ", attempts)
        print()
    if attempts == 0:
        print("Game Over!")
        