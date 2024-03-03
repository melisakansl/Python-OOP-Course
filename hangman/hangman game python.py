import random
word_list = ["mango", "yabanmersini", "portakal", "mandalina", "avokado"]
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

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_index = random.randint(0,2)
chosen_word = word_list[random_index]
chosen_words_letter_list = []
display = []
game_over = False
  
for i in range(0, len(chosen_word)):
  chosen_words_letter_list.append(chosen_word[i])
  display += "_"
print(display)
tries = 7
while not game_over:

  guessed_letter = input("Please guess a letter.\n").lower()

  for i in range(len(chosen_words_letter_list)):
    if guessed_letter == chosen_words_letter_list[i]:
      display[i] = chosen_words_letter_list[i]
  print(display)

  if guessed_letter not in chosen_words_letter_list:
    tries -= 1
    if tries<=0:
      print(f"Sorry! You lose. The word was {chosen_word}.")
      game_over = True
      print(" ")
      print(stages[0])
    else:
      print(" ")
      print(f"You have {tries} tries left.")
    
      print(stages[tries])

  if display == chosen_words_letter_list:
    print(f"Congrats! The word is {chosen_word}.")
    game_over = True