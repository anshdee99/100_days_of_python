import random
word_list = ["Apple","Banana","Orange"]
chosen_word = random.choice(word_list)
print (chosen_word)

guess = input("Guess a letter: ").lower()

#This is to create "-"" equals to the number of letters in the random generated word. 
i = len(chosen_word)
print ("-" * i)

#Creating an empty string. This string will be used to get the design during the game. Eg: If random word is apple this would return --a---
display = ""

for letter in chosen_word:
    if letter == guess:
        display += guess
    else: 
        display += "-"
#Executing this outside of the loop so it does not print all the values.         
print (display)
