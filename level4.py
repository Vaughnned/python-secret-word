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
lives = 6


while not correct and lives > 0:
    player_guess = input("Enter a letter: ")
    letters = sorted(letters)
    if player_guess in chosen_word:
        for element in chosen_word:
            if chosen_word.count(element) == 1 and letters.count(element) == 0:
                letters.append(player_guess)
                print("cool")
            elif chosen_word.count(element) > 1 and letters.count(element) > 1 and letters.count(element) < chosen_word.count(element):
                print("weird")
                letters.append(player_guess)
        print("Correct! The word contains ", player_guess )
        print(letters)
        print()
    elif player_guess not in chosen_word:
        lives = lives - 1
        print("Wrong!")
        print()
    if letters == chosen_word:
        print("Congrats! You guessed the word!")
        correct = True
    print("Remaining lives: ", lives)
    if lives == 0:
        print("Game Over!")

        

        # for element in chosen_word:
        #   if chosen_word.count(element) == 1 and letters.count(element) == 0:
        #     letters.append(player_guess)
        #   elif chosen_word.count(element) > 1 and letters.count(element) < chosen_word.count(element):
        #     letters.append(player_guess)