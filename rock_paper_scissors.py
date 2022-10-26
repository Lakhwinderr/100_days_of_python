import random
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

#Write your code below this line 👇
options = [rock, paper, scissors]
option_choosed = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors: "))

pc_choosed = random.randint(0,2)
print(options[option_choosed])
print(f"Computer chosed: \n{options[pc_choosed]}")
if(option_choosed == 0):
  if(pc_choosed == 0):
    print("Draw")
  else:
    print("You won")
if option_choosed == 1:
  if(pc_choosed == 1):
    print("Draw")
  else:
    print("You lose")
if(option_choosed == 2):
  if(pc_choosed == 2):
    print("Draw")
  if(pc_choosed == 0):
    print("You lose")
  else:
    print("You won")