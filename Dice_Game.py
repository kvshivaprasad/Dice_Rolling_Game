import random  # Importing random to guess the any number 

while True: # To loop inifinite 
 dice = input("Roll the dice (y/n): ").lower()   # Ask the user to play this game simply yes or no
 if dice == "y": # condition checking 
    dice1 = random.randint(1,6) 
    dice2 = random.randint(1,6) # choose to dice to play the game 
    print(f"{dice1} and {dice2}")
 elif dice == "n": # Stop the game
    print("Thank you!")
    break # Break the loop 
 else:
    print("Invalid option") 
  