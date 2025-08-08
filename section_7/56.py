import random

#This is for chosing a random word. 
word_list = ["Apple", "Banana", "Orange", "nimbusoda"]
chosen_word = random.choice(word_list).lower()
print (chosen_word)

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

#The code can exit the while loop using this. 
    if "-" in display:
        game_over = False
    else: 
        game_over = True
        print ("You win!")
