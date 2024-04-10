# This is a sample Python script.
# Step 1
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
ran_choice = random.randint(0, 2)
chosen_word = word_list[ran_choice]
print(chosen_word)
display_word = []

for element in chosen_word:
    display_word.append("_")

print(display_word)

end_of_game = False
winner = 0
wrong_answer = 0
player_lives = 6

while not end_of_game:
    guess = input("Guess a letter in the hidden word ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display_word[position] = letter

    if guess not in chosen_word:
        player_lives -= 1
        print(f"Wrong! You have {player_lives} lives left.")
        print(stages[player_lives])
        if player_lives == 0:
            print("Out of Lives! Try again next time.")
            end_of_game = True

    print(display_word)
