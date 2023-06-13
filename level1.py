
correct = False
secret_word = ("h", "e", "l", "l", "o")
secret_word = sorted(secret_word)
letters = []

while not correct:
    player_guess = input("Enter a letter: ")
    letters = sorted(letters)
    if player_guess in secret_word:
        print("Correct! The word contains the letter ", player_guess )
        letters.append(player_guess)
        print(letters)
        print()
    elif player_guess not in secret_word:
        print("Wrong!")
        print()
    if letters == secret_word:
        print("Congrats! You guessed the word!")
        correct = True