import time
from random_word import RandomWords

user = input("Enter player name: ")
print("Welcome, ", user, "!", sep="")

time.sleep(1)
print("Start guessing: ")
time.sleep(0.5)

words = RandomWords()
word = words.get_random_word()

guesses = ""
turns = 10

while turns > 0:

    # make a counter that starts with zero
    failed = 0

    # for every character in secret_word
    for char in word:

        # see if the character is in the players guess
        if char in guesses:

            # print then out the character
            print(char, end=""),

        else:

            # if not found, print a dash
            print("_", end=""),

            # and increase the failed counter with one
            failed += 1

            # if failed is equal to zero

    # print You Won
    if failed == 0:
        print("\nYou won")
        # exit the script
        break
        # ask the user go guess a character
    guess = input("guess a character:")

    # set the players guess to guesses
    guesses += guess

    # if the guess is not found in the secret word
    if guess not in word:

        # turns counter decreases with 1 (now 9)
        turns -= 1

        # print wrong
        print("Wrong")

        # how many turns are left
        print("You have", + turns, 'more guesses')

        # if the turns are equal to zero
        if turns == 0:
            # print "You Lose"
            print(word)
            print("You Lose")