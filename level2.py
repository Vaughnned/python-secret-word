import random

correct = False
secret_word = [["h", "e", "l", "l", "o"], ["a", "p", "p", "l", "e"], ["h", "o", "u", "s", "e"]]
random_word = sorted(secret_word[random.randint(0,2)])
letters = []


while not correct:
    player_guess = input("Enter a letter: ")
    letters = sorted(letters)
    if player_guess in random_word:
        print("Correct! The word contains ", player_guess )
        letters.append(player_guess)
        print(letters)
        print()
    elif player_guess not in random_word:
        print("Wrong!")
        print()
    if letters == random_word:
        print("Congrats! You guessed the word!")
        correct = True
