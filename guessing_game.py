"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print("Welcome to the number guessing game!")
    game = True
    high_score = 1000
    while game == True: 
      random_num = random.randrange(0,11)
      correct = False
      attempts = 0
      while correct == False:
        #exception handling
        #adds attempt including invalids
        attempts += 1
        try:
          user_guess = input("What do you think is the number? ")
          user_guess = int(user_guess)
        except ValueError:
          print("That is not a valid guess sorry try again")
          continue
        #checking number within range
        if user_guess < 0 or user_guess > 10:
          print("Sorry the number you entered is not between 0-10 please try again!")
          continue
        #checking guess
        if user_guess == random_num:
          print("Congratulations you got the number correct!! ")
          print("You completed the game in ", attempts, "attempts")
          correct = True
        elif user_guess < random_num:
          print("Nice try, but the number is greater than your guess. ")
        elif user_guess > random_num:
          print("Nice try, but the number is less than your guess. ")
      
      playagain = input("Would you like to play again? enter y for yes and n for no. ")
      if playagain == "n":
        game = False
        print("Thanks for playing having a great day!")
      if playagain == "y":
        if attempts < high_score:
          high_score = attempts
        print("The Highscore is", high_score, "Try to beat it if you can")
    
# Kick off the program by calling the start_game function.
start_game()