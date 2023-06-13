import random

correct = False

difficulty = input("Difficulty: Type easy, medium, or hard ")
secret_word = [["a", "p", "p", "l", "e"], ["d", "e", "s", "k", "t", "o", "p"], ["e", "x", "c", "a", "v", "a", "t", "o", "r"]]
if difficulty == "easy":
    chosen_word = sorted(secret_word[0])
    print(chosen_word)
elif difficulty == "medium":
    chosen_word = sorted(secret_word[1])
    print(chosen_word)
elif difficulty == "hard":
    chosen_word = sorted(secret_word[2])
    print(chosen_word)
letters = []


while not correct:
    player_guess = input("Enter a letter: ")
    letters = sorted(letters)
    if player_guess in chosen_word:
        print("Correct! The word contains ", player_guess )
        letters.append(player_guess)
        print(letters)
        print()
    elif player_guess not in chosen_word:
        print("Wrong!")
        print()
    if letters == chosen_word:
        print("Congrats! You guessed the word!")
        correct = True