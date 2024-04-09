# This is a sample Python script.
#Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

ran_choice = random.randint(0, 2)

chosen_word = word_list[ran_choice]

print(chosen_word)

display_word = []

for element in chosen_word:
    display_word.append("_")

print(display_word)

guess = input("Guess a letter in the hidden word ").lower()

winner = 0

if display_word == word_list[0]:
    winner = 1
elif display_word == word_list[1]:
    winner = 1
elif display_word == word_list[2]:
    winner = 1
else:
    you_win = 0

i = 0

while i < len(chosen_word):
    for letter in chosen_word:
        if letter == guess:
            letter_position = chosen_word.index(letter)
            display_word[letter_position] = letter
            i += 1

print(display_word)


for letter in chosen_word:
    while i < len(chosen_word):
        if letter == guess:
            i += 1
            letter_position = chosen_word.index(letter)
            display_word[letter_position] = letter
