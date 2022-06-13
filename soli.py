import random
print("rock =(1) \npaper =(2) \nscissors =(3)")
print("game rules: \n rocke(1) vs scissors(3) -->roke(1) win \n scissors(3) vs paper(2) -->scissors(3) win \n paper(2) vs roke(1) -->paper(2) win  ")
while True :
  choices = ["rock", "paper", "scrissors"]
  choices = 1,2,3
  computer = int(random.choice(choices))
  player = int(input("chose your number : "))


  while player not in choices or player == computer  :
    if player == computer:
     print("sorry your choice = computer choice ")
     player = int(input("chose number again : "))
     computer = int(random.choice(choices))
    else :
      player = int(input("chose number 1 , 2 or 3 : "))
      computer = int(random.choice(choices))

   #if player == computer :
      #player = int(input("chose again number 1 , 2 or 3 : "))
     # computer = int(random.choice(choises))

  if player == 1 and computer == 2 :
    player = "rock"
    computer = "paper"
    print("paper vs rock \ncomputer win ! ")
  elif player ==1 and computer == 3 :
    player = "rock"
    computer = "scissors"
    print("rock vs scissors \nyeees sir ,your win ! ")
  elif player == 2 and computer == 1 :
    player = "paper"
    computer = "rock"
    print("paper vs rock \nyeees sir ,your win ! ")
  elif player == 2 and computer == 3 :
    player = "paper"
    computer = "scissors"
    print("scissore vs paper\ncomputer win !")
  elif player == 3 and computer == 1 :
    player = "scissors"
    computer = "rock"
    print("rock vs scissors \ncomputer win !")
  elif player == 3 and computer == 2 :
    player = "scissors"
    computer = "paper"
    print("scissors vs paper \nyeees sir ,your win !")

  print("computer choice : ",computer)
  print ("player choice :",player)
  print("good game ")

  rematch = input("you want to rematch (yes = y , no =n ) ? ")
  yes = "y"
  no = "n"
  while rematch != yes and rematch != no :
       rematch = input("you need to choice n/y ? ")
  if rematch == no :
       print("ok , goodbye my friend")
       break
  if rematch == yes :
       print("lets goooo ")

