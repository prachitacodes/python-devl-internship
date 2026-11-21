#Q1
import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com/"
response = requests.get(url)
if response.status_code == 200:
    print("Website fetched successfully!\n")
else:
    print("Failed to fetch website. Status:", response.status_code)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("div", class_="quote")

print(f"Found {len(quotes)} quotes\n")
print("=" * 50)

for i, quote in enumerate(quotes, start=1):
    text   = quote.find("span", class_="text").get_text()
    author = quote.find("small", class_="author").get_text()
    tags   = quote.find("div", class_="tags").get_text(strip=True)

    print(f"Quote {i}:")
    print(f"  Text   : {text}")
    print(f"  Author : {author}")
    print(f"  Tags   : {tags}")
    print("-" * 50)
#Q2
import random

words = ["python", "hangman", "computer", "programming", "keyboard",
         "internet", "developer", "algorithm", "variable", "function"]

hangman_stages = [
    """
    -----
    |   |
    |
    |
    |
    |
    --------""",
    """
    -----
    |   |
    |   O
    |
    |
    |
    --------""",
    """
    -----
    |   |
    |   O
    |   |
    |
    |
    --------""",
    """
    -----
    |   |
    |   O
    |  /|
    |
    |
    --------""",
    """
    -----
    |   |
    |   O
    |  /|\\
    |
    |
    --------""",
    """
    -----
    |   |
    |   O
    |  /|\\
    |  /
    |
    --------""",
    """
    -----
    |   |
    |   O
    |  /|\\
    |  / \\
    |
    --------"""
]

secret_word = random.choice(words)
max_wrong = 6
guessed_letters = []
wrong_guesses = 0

def show_progress(word, guessed):
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def show_hint(word):
    return f"Hint: The word starts with '{word[0].upper()}' and has {len(word)} letters."

print("=" * 40)
print("       WELCOME TO HANGMAN!")
print("=" * 40)
print(show_hint(secret_word))

while wrong_guesses < max_wrong:
    print(hangman_stages[wrong_guesses])
    progress = show_progress(secret_word, guessed_letters)
    print(f"\nWord  : {progress}")
    print(f"Wrong guesses left : {max_wrong - wrong_guesses}")
    print(f"Letters guessed    : {', '.join(guessed_letters) if guessed_letters else 'None'}")

    if "_" not in progress:
        print("\n🎉 YOU WIN! The word was:", secret_word.upper())
        break

    guess = input("\nGuess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single letter only!")
        continue

    if guess in guessed_letters:
        print(f"⚠️  You already guessed '{guess}'. Try another!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print(f"✅ '{guess}' is correct!")
    else:
        wrong_guesses += 1
        print(f"❌ '{guess}' is wrong!")
else:
    print(hangman_stages[6])
    print(f"\n💀 GAME OVER! The word was: {secret_word.upper()}")

print("=" * 40)
print("Thanks for playing Hangman!")
print("=" * 40)    
