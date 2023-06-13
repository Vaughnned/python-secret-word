
correct = False
secret_word = "hello"


while not correct:
    player_guess = input("Enter a letter: ")
    if player_guess == secret_word:
        print("Congrats! You guessed the word!")
        correct = True
    if player_guess in secret_word:
        print("Correct! The word contains the letter ", player_guess )
        print()
    elif player_guess not in secret_word:
        print("Wrong!")
        print()