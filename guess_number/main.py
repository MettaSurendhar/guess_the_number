from calendar import c
import random

def guess(x) :
  randNum = random.randint(1,x)
  print(randNum)
  guess=0

  while guess != randNum :
    guess = int(input(f"Guess a number between 1 and {x}:"))
    if guess < randNum:
      print('Sorry, Guess again. Too low')
    elif guess > randNum:
      print('Sorry, Guess again. Too high')
  else :
    print( f'You guessed the number {guess} correctly , Congratulations!!!')

# guess(10)

def computer_guess(x):
  low = 1
  high = x
  feedback = ''
  while feedback != 'c' :
    guess = random.randint(low,high)
    feedback = input(f'Is  {guess} is too high (H), too low (L), or correct (C) ').lower()
    if feedback == 'h':
      high = guess -1
    elif feedback== 'l':
      low = guess + 1
   
  print('correct')

  

limit = int(input('enter an limit : '))
computer_guess(limit)