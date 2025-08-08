import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
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
lives = 6

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
# created a list outside to accumulate all the correctly guessed letters
#declared outside so that don't get modify everytime while loop runs
# asking the user of guess again and again through while loop
#like if guessed one letter correctly then ask to guess another one 
#also want to keep all the guessed letter together in one string only 

while not game_over: # while game over is false loop will work
    guess = input("Guess a letter: ").lower() # Adding the same number of underscores as of number of characters in choosen word

    display = ""

# Place the guessed character in right position and keep underscore in the rest
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess) # in order to keep all the guessed letters in string
        elif letter in correct_letters: # if the current letter we are looping in is in the list of correct letters
            display += letter # so added current letter to the display
        else:# one of the letters which we are looping in does not match guess but is present in the list of correct letters then it also gets added to display
            display += "_"

    print(display)

    # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")

    if "_" not in display:
        game_over = True
        print("You win.")

    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])