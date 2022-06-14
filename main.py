import random

while True:

    player_choice = None
    rock = "R"
    paper = "P"
    scissors = "S"

    choice = ["R", "P", "S"]
   
    random_choice=random.choice(choice)

    while player_choice not in choice:
      player_choice= input("What do you choose? Type R for Rock, P for paper and S for Scissor.").upper()

    if player_choice == "R":
      if random_choice == "R":
        print(f"Player1-Rock, computer-Rock, it's a tie!")
      elif random_choice == "P":
        print(f"player1-Rock, computer-Paper, You lost!!!")
      elif random_choice == "S":
        print(f"player1-Rock, computer-Scissors, You won!!!")

    elif player_choice == "P":
      if random_choice == "R":
        print(f"player1-Paper, computer-Rock,  You won!!!")
      elif random_choice == "P":
        print(f"player1-Paper, computer-Paper, It's a tie!!!")
      elif random_choice == "S":
        print(f"player1-Paper, computer-Scissors, You lost!!!")
    
    elif player_choice == "S":
      if random_choice == "R":
        print(f"player1-Scissors, computer-Rock, You lost!!!")
      elif random_choice == "P":
        print(f"player1-Scissors, computer-Paper, You won!!!")
      elif random_choice == "S":
        print(f"player1-Scissors, computer-Scissors, It's a tie!!!")
    
    Again = input("Do you want to play again? Type Y for yes and N for no").upper()

    if Again != "Y":
     break
print("Thanks for playing")