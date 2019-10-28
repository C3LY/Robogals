import random
print("Hello")
userInputNumber=0
playGame=True
while(playGame==True):
  win=False
  x=random.randint(1,10)
  userInputNumber=0
  print("pick a number")
  while(win==False):
    userInput = input("type here:")
    userInputNumber = int(userInput)
    print(userInputNumber)
    if(userInputNumber<x):
     print("too low")
    elif(userInputNumber>x):
      print("too high")
    else:
     print("You win!")
     win=True
  playAgainUserInput = input("Would you like to play again? y for yes, n for no")
  if(playAgainUserInput!="y"):
    playGame=False
print("closing...")

#other challenge:
# 2 player mode
#menu
#robustness
#capitalize letter game
#coderbyte challenges
