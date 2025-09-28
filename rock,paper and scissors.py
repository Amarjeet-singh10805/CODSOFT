import random
choice=['rock','paper','scissors']
c='y'
while c=='y':
  print("\n---WELCOME TO ROCK-PAPER-SCISSOR-GAME---\n")
  ch=input("Enter your choice (rock/paper/scissors):").lower()
  if ch not in choice:
    print("Please enter valid input")
    ch=input("Enter your choice again:").lower()
  comp_choice=random.choice(choice)
  print("Computer choice is:",comp_choice)
  print("Your choice is:",ch)
  if ch==comp_choice:
    print("IT'S A TIE")
  elif (ch=='rock' and comp_choice=='scissors') or (ch=='paper' and comp_choice=='rock') or (ch=='scissors' and comp_choice=='paper'):
    print("YOU WIN")
  else:
    print('COMPUTER WINS')
  c=input("Wanna play again(y/n):")
else:
  print("---GAME END---")