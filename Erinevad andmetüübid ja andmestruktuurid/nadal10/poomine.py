import random
import urllib.request
url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urllib.request.urlopen(url)
long_txt = response.read().decode()
all_words = long_txt.splitlines()
lives = 8
has_guessed = False
tried_letters = []
guessed = []

word = random.choice(all_words)

def show_word(actual_word, guessed_letters):
    to_display = ""
    for letter in actual_word:
        if (letter in guessed_letters):
            to_display += letter
        else:
            to_display += "_"
    return to_display

while not has_guessed and lives > 0:
    print(show_word(word, guessed))
    letter = input("Input letter:")
    if (len(letter) != 1):
        print("one letter at a time!")
        continue
    if (letter in tried_letters):
        print(f"{letter} already guessed!")
        continue
    tried_letters.append(letter)

    if (letter in word):
        print(f"{letter} is in word")
        guessed.append(letter)

        has_guessed = True
        for i in word:
            if (i not in guessed):
                has_guessed = False
                break
        if (has_guessed):
            print(f"You have quessed the word: {word}")
        continue
    lives -= 1
    print(f"lives left: {lives}")

if (lives == 0):
    print(f"You did not guess the word {word}")