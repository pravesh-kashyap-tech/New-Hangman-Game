#!/usr/bin/env python3
import random
import os

# Word Bank by Category & Difficulty
WORD_BANK = {
    "Country": {
        "easy": ["india", "china", "nepal", "japan", "brazil"],
        "hard": ["argentina", "kazakhstan", "australia", "switzerland", "venezuela"]
    },
    "Capital": {
        "easy": ["delhi", "tokyo", "paris", "rome", "london"],
        "hard": ["washington", "canberra", "amsterdam", "copenhagen", "uzbekistan"]
    },
    "Animal": {
        "easy": ["cat", "dog", "lion", "tiger", "bear"],
        "hard": ["elephant", "kangaroo", "alligator", "chimpanzee", "hippopotamus"]
    },
    "Bird": {
        "easy": ["crow", "duck", "hen", "owl", "parrot"],
        "hard": ["flamingo", "woodpecker", "peacock", "albatross", "nightingale"]
    },
    "Fruit": {
        "easy": ["mango", "apple", "pear", "kiwi", "grape"],
        "hard": ["pineapple", "pomegranate", "strawberry", "blackberry", "watermelon"]
    },
    "Vegetable": {
        "easy": ["peas", "onion", "okra", "corn", "bean"],
        "hard": ["cauliflower", "broccoli", "cabbage", "spinach", "brinjal"]
    },
    "Celebrity": {
        "easy": ["raj", "amit", "alia", "tom", "brad"],
        "hard": ["shahrukh", "salman", "scarlett", "leonardo", "benedict"]
    },
    "Sport": {
        "easy": ["golf", "tennis", "cricket", "chess", "hockey"],
        "hard": ["badminton", "basketball", "baseball", "gymnastics", "wrestling"]
    }
}

USED_WORDS = set()

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_word():
    while True:
        print("\n🎮 Welcome to Advanced Hangman 🎮")
        print("Categories available:")
        for i, cat in enumerate(WORD_BANK.keys(), 1):
            print(f"{i}. {cat}")

        cat_choice = input("\nChoose a category (1-8): ")
        categories = list(WORD_BANK.keys())
        try:
            category = categories[int(cat_choice) - 1]
        except:
            print("⚠️ Invalid choice, defaulting to 'Country'")
            category = "Country"

        diff = input("Choose difficulty (easy/hard): ").lower()
        if diff not in ["easy", "hard"]:
            print("⚠️ Invalid difficulty, defaulting to 'easy'")
            diff = "easy"

        available_words = [w for w in WORD_BANK[category][diff] if w not in USED_WORDS]

        if not available_words:
            print(f"⚠️ No more {diff} words left in {category}! Please choose another.")
            continue
        else:
            word = random.choice(available_words)
            USED_WORDS.add(word)
            return word.lower(), category, diff

def hangman():
    word, category, diff = choose_word()
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        clr()
        print(f"👉 Category: {category} | Level: {diff.capitalize()}")
        print(HANGMAN_PICS[6 - lives])  
        print("Lives left:", lives)

        # Show guessed word in CAPITALS
        display = [letter.upper() if letter in used_letters else "_" for letter in word]
        print("Word: ", " ".join(display))

        guess = input("\nGuess a letter: ").lower()

        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                lives -= 1
        elif guess in used_letters:
            print("⚠️ You already used that letter.")
            input("Press Enter to continue...")
        else:
            print("❌ Invalid input, enter a-z.")
            input("Press Enter to continue...")

    clr()
    if lives == 0:
        print(HANGMAN_PICS[-1])
        print("\n💀 You lost! The word was:", word.upper())
    else:
        print("\n🎉 You guessed it! The word was:", word.upper())

if __name__ == "__main__":
    while True:
        hangman()
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thanks for playing! Goodbye.")
            break
