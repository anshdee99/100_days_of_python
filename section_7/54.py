import random
todo_list = ["apple", "orange", "octupus"]
random_word = random.choice(todo_list)
print(random_word)

guess = input("Guess a letter: \n").lower()

for i in random_word:
    if i == guess:
        print("Right")
    else:
        print("Wrong")
