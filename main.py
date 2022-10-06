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
import random
user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
game=[rock, paper, scissors]
print(game[user])
random.seed()
computer=random.randint(0, 2)
Computer_choice=game[computer]
print(f"Computer chose:\n {Computer_choice}")
if user==0 and computer==0:
  print("Do it again")
elif user==0 and computer==1:
  print("You lose")
elif user==0 and computer==2:
  print("You win")
elif user==1 and computer==0:
  print("You win")
elif user==1 and computer==1:
  print("Do it again")
elif user==1 and computer==2:
  print("You lose")
elif user==2 and computer==0:
  print("You lose")
elif user==2 and computer==1:
  print("You win")
elif user==2 and computer==2:
  print("Do it again") 
  