import random

winner = ''

#let the compuer randomly select rock, paper or scissor using random function
random_choice = random.randint(0,2)

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

#take input form user
user_choice = ''
while(user_choice != 'rock' and
      user_choice != 'paper' and
      user_choice != 'scissors'):
    user_choice = input('rock, paper or scissors? ')

#determine who wins
if (computer_choice == user_choice):
    winner = 'Tie'
elif (computer_choice == 'rock' and user_choice == 'scissor'):
    winner = 'Computer'
elif (computer_choice == 'paper' and user_choice == 'rock'):
    winner = 'Computer'
elif (computer_choice == 'scissor' and user_choice == 'paper'):
    winner = 'computer'
else:
    winner = 'User'

#print winner
if (winner == 'Tie'):
    print('We both chose', computer_choice + ', play again.')
else:
    print(winner, 'won. The computer chose', computer_choice)
