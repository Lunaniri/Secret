
from random import *
secret = randint(1, 50)
print secret
print "Guess the secret number between 1 nad 50"
guess = operation=int(raw_input("Type your guess here"))

if guess == secret:
      print "You won! Your guess was correct!"
else:
    print "Sorry, your guess was wrong. Try again!"