
import random
import words
import hangman_art

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

word_list = words.word_list
ran_choice = random.randint(0, len(word_list))
chosen_word = word_list[ran_choice]
print(hangman_art.logo)

display_word = []

for element in chosen_word:
    display_word.append("_")

print(display_word)

end_of_game = False
winner = 0
wrong_answer = 0
player_lives = 6

while not end_of_game:
    guess = input("\nGuess a letter in the hidden word: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display_word[position] = letter

    if guess not in chosen_word:
        player_lives -= 1
        print(f"Wrong!\nYou guessed the letter '{guess}'\nYou have {player_lives} lives left.")
        print(stages[player_lives])
        if player_lives == 0:
            print(f"Out of Lives!\nThe word was {chosen_word}\nTry again next time.")
            end_of_game = True

    elif "_" not in display_word:
        winner = True
        print("You win!")
        print(display_word)
        break

    print(display_word)
