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

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display_word[position] = letter

print(display_word)

winner = False

while not winner:
    if "_" not in display_word:
        winner = True
        break
    else:
        second_guess = input("Guess again ")
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == second_guess:
                display_word[position] = letter
    print(display_word)

if winner:
    print("You Won!")














