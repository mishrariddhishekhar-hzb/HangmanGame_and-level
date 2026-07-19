import random
from typing import Any  
words = ["apple", "tiger", "horse", "lion", "panda", "zebra", "grape", "guava", "peach", "mango"]

word = random.choice(words)
guessed_letters = []

max_attempts = 6
wrong_guesses = 0

word = random.choice(words)               
guessed_letters = []

max_attempts = 11
wrong_guesses = 0 

print("🎮 Welcome to Hangman! ")
print("HINT : Word you guess is a fruit🍎 or wild animal🐾. \nHave fun playing! ")

while wrong_guesses < max_attempts:
    display_word = ""
    for letter in word : 
        if letter in guessed_letters:
            display_word += letter + " "
        else :
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player has gussed the word
    if "_ " not in display_word:
        print("🎉 Congratulations ! You guessed the word:", word)
        break

    guess = input("Enter a letter: ") .lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. ")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess! ")
        print("Attempt left:", max_attempts - wrong_guesses)

if wrong_guesses == max_attempts:
    print("\n💀 Game Over! ")
    print("The correct word was:", word)