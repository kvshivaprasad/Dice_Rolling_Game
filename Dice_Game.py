import random 

while True:
 dice = input("roll the dice (y/n): ").lower()   
 if dice == "y":
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f"{dice1} and {dice2}")
 elif dice == "n":
    print("Thank you!")
    break
 else:
    print("Invalid option")
  