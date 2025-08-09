import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
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
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

#This is for chosing a random word. 
word_list = ["Apple", "Banana", "Orange", "nimbusoda"]
chosen_word = random.choice(word_list).lower()
print (chosen_word)

lives = 6 #This is the max lifes a user has. 


correct_letters = [] #If this is kept within the while loop, it will be wiped to 0 when the loop repeats. 

game_over = False
while not game_over: 

#This is for number of letters to chose from
    placeholder = ""
    for j in chosen_word: 
        placeholder += "-"
    print (placeholder)

    guess = input ("Guess a letter: ").lower()

#This is for shwowing the progress that is made. 
    display = ""
    for letter in chosen_word:
        if letter == guess: 
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters: #This elif is needed because when the guess 1 is made, it will show the guess1 along with the second guess and so on. 
            display += letter
        else: 
            display += "-"
            correct_letters.append(guess)
    print (display)

#This is for when a user makes an incorrect attempt. 
    if guess not in chosen_word:
        lives -= 1
        if lives == 0: 
            game_over = True
            print ("Game Over, you lose!")

#The code can exit the while loop using this. 
    if "-" in display:
        game_over = False
    else: 
        game_over = True
        print ("You win!")

#Calling the ASCII art from the list. 
    print(stages[lives])
