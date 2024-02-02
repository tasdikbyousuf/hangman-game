import time
from random_word import RandomWords

def welcome_user():
    """
    Gets the player's name and displays a welcome message.
    """
    user = input("Enter player name: ")
    print("Welcome, ", user, "!", sep="")
    time.sleep(1)

def display_start_message():
    """
    Displays the start message with a delay for a better user experience.
    """
    print("Start guessing: ")
    time.sleep(0.5)

def generate_random_word():
    """
    Generates a random word for the player to guess.
    """
    words = RandomWords()
    return words.get_random_word()

def display_word_progress(word, guesses):
    """
    Displays the word with correct guesses or underscores.
    """
    for char in word:
        print(char if char in guesses else "_", end="")
    print()

def main_game_loop(word):
    """
    Manages the main game loop, prompting the player for guesses and updating the game state.
    """
    guesses = ""
    turns = len(word)

    while turns > 0:
        display_word_progress(word, guesses)
        if all(char in guesses for char in word):
            print("\nYou won")
            break

        guess = input("Guess a character:")
        guesses += guess

        if guess not in word:
            turns -= 1
            print("Wrong")
            print("You have", turns, 'more guesses')

            if turns == 0:
                print("Correct word:", word)
                print("You Lose")

def play_game():
    """
    Orchestrates the game by calling relevant functions.
    """
    welcome_user()
    display_start_message()
    word_to_guess = generate_random_word()
    main_game_loop(word_to_guess)

# Entry point of the program
if __name__ == "__main__":
    play_game()
