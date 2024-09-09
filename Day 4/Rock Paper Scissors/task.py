rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
from random import choice

print("Pick Rock, Paper, or Scissors!")

moves = [ rock, paper, scissors]

# These start the commands
player = choice(moves)  #input("Enter the player's move: ")
print(f"The player = {player}.")

computer = choice(moves)
print(f"The computer = {computer}.")

# Logic (What happens if?)
if player == computer:
  print("This is a tie!")
elif (player == "rock" and computer == "scissors") or \
(player == "paper" and computer == "rock") or \
(player == "scissors" and computer == "paper"):
  print("The player won!")
else:
  print("The player lost, try again!")
