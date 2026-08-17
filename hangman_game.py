import os
import random


WORDS = ["python", "laptop", "coding", "student", "hangman"]
MAX_WRONG_GUESSES = 6


def choose_word():
    demo_word = os.getenv("HANGMAN_WORD", "").lower()
    if demo_word in WORDS:
        return demo_word
    return random.choice(WORDS)


def show_word(secret_word, guessed_letters):
    display = []
    for letter in secret_word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")
    return " ".join(display)


def play_game():
    secret_word = choose_word()
    guessed_letters = []
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print(f"You can make {MAX_WRONG_GUESSES} wrong guesses.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("Word:", show_word(secret_word, guessed_letters))
        print("Guessed letters:", " ".join(guessed_letters) if guessed_letters else "None")
        print("Wrong guesses left:", MAX_WRONG_GUESSES - wrong_guesses)

        guess = input("Enter one letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")

        if all(letter in guessed_letters for letter in secret_word):
            print("Word:", show_word(secret_word, guessed_letters))
            print("Congratulations! You guessed the word:", secret_word)
            break
    else:
        print("Game over! The word was:", secret_word)


if __name__ == "__main__":
    play_game()
