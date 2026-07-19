import random
from typing import Any

# Hangman levels
levels = [
    {
        "name": "Level 1",
        "topic": "Fruits",
        "words": ["apple", "grape", "guava", "lemon", "mango"]
    },
    {
        "name": "Level 2",
        "topic": "Animals",
        "words": ["rabbit", "donkey", "monkey", "jaguar", "beaver"]
    },
    {
        "name": "Level 3",
        "topic": "Countries",
        "words": ["germany", "romania", "vietnam", "hungary", "nigeria"]
    },
    {
        "name": "Level 4",
        "topic": "Flowers",
        "words": ["lavender", "gardenia", "bluebell", "foxglove"]
    },
    {
        "name": "Level 5",
        "topic": "Sports",
        "words": ["football", "baseball", "cricket"]
    },
    
]

max_attempts = 11

print("🎮 Welcome to the Hangman Game!")

for level in levels:

    word = random.choice(level["words"])

    guessed_letters = []
    wrong_guesses = 0

    print("\n" + "=" * 40)
    print(level["name"])
    print("Topic:", level["topic"])
    print("=" * 40)

    # Game loop for the current level
    while wrong_guesses < max_attempts:

        # Display the current word
        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Wrong guesses:", wrong_guesses, "/", max_attempts)
        print("Guessed letters:", guessed_letters)

        # Check if the word is completely guessed
        if "_" not in display_word:
            print("\n🎉 Congratulations!")
            print("You completed", level["name"])
            print("The word was:", word)
            break

        # Take user input
        guess = input("\nEnter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter only one alphabet letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        # Add the guess to the list
        guessed_letters.append(guess)

        # Check whether the guess is correct
        if guess in word:
            print("✅ Correct guess!")
        else:
            wrong_guesses += 1
            print("❌ Wrong guess!")
            print("Chances left:", max_attempts - wrong_guesses)

    # If the player uses all 11 chances
    if wrong_guesses == max_attempts:
        print("\n💀 Game Over!")
        print("You ran out of chances.")
        print("The correct word was:", word)
        print("You reached", level["name"])
        break

else:
    # This runs only if all levels are completed
    print("\n🏆 CONGRATULATIONS!")
    print("You completed all the levels!")
    print("🎉 You are the Hangman Champion!")