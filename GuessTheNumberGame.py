import random  # Import the random module
from turtle import delay  # Import the delay module


target = random.randint(1, 100)
# Generate a random number between 1 and 100
guessed_number = 0
# Set guessed_number to 0
total = i = 6
# Set total to 6


print("Let's play a game. I'm thinking of a number between 1 and 100.\n")
# Print a message to the user
delay(3)
# Delay the program for 3 second
print("I've guessed a number. Can you guess it?")
delay(1)
# Delay the program for 1 second
print("You have 6 tries to guess the number.\n")
# Print a message to the user


while i != 0 and guessed_number != target:
    # The loop will run again and again while i is not 0 and guessed_number is not target

    i = i-1  # Decrease i by 1

    guessed_number = int(input("Guess the number from 1-100 : "))
    # Ask the user to guess the number
   

    # if-else loop starts here
    if(guessed_number == target):
        print(f"You guessed the number correctly in {total-i} attempts.")
    elif(guessed_number > target):
        print("The number is less than the entered number")
    elif(guessed_number < target):
        print("The number is greater than the entered number")
    else:
        print("You have entered an invalid number")
    # if-else loop ends here

    if i>0:
        print(f"You have {i} attempts left.")
        # Show the remaining attempts to the user
    
    if i==0:
        print("You have used all your attempts. Game Over.")
        break
        # Show the message to the user that he has used all the attempts
