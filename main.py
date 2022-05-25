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
games=[rock,paper,scissors]
chose=int(input("What do you choose. 0 for Rock, 1 for Paper, 2 for Scissors: "))
print("You Chose")
print(games[chose])


comp= random.randint(0,2)
print("Computer Chose")
print(games[comp])

#print(comp)
if chose >=3 or chose <=0:
    print("Invalid Input")
elif chose ==0 and comp ==2:
    print("You Win")
elif chose==2 and comp ==0:
    print("You lose")
elif chose>comp:
    print("You Win")
elif comp>chose:
    print("You lose")
elif chose==comp:
    print("Draw")