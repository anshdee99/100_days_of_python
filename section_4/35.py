import random
your_choice = input("What do you choose ? Rock, Paper , Scissors\n").lower()
computer = ["Rock", "Paper", "Scissors"]

#Randomisation logic
computer_choice = random.choice(computer).lower()
print (f"Computer chose {computer_choice}")

#Rock beats Scissors
if your_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif your_choice == "scissors" and computer_choice == "rock":
    print("You lose!")

#Paper beats Rock
elif your_choice == "paper" and computer_choice == "rock":
    print ("You win!")
elif your_choice == "rock" and computer_choice == "paper":
    print ("You lose!")

#Scissors beats Paper
elif your_choice == "scissors" and computer_choice == "paper":
    print ("You win!")
elif your_choice == "paper" and computer_choice == "scissors":
    print ("You lose!")

#Tie conditions 
# This can be simplified if you add:
# elif your_choice == computer choice:
# print ("It's a tie ")
elif your_choice == "rock" and computer_choice == "rock":
    print ("It's a tie")
elif your_choice == "paper" and computer_choice == "paper":
    print ("It's a tie")
elif your_choice == "paper" and computer_choice == "paper":
    print ("It's a tie")

else: 
    print ("Invalid input. You lose!")
