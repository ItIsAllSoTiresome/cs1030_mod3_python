import random

playOrNo = input("Do you want to play Rock, Paper, Scissors versus a computer?\n" 
                 "Enter 'Yes' or 'No': ")
while(playOrNo != 'Yes' and playOrNo != 'yes' and playOrNo != 'No' and playOrNo != 'no'):
   if(playOrNo != 'Yes' and playOrNo != 'yes' and playOrNo != 'No' and playOrNo != 'no'):
      playOrNo = input("Please input either 'Yes' or 'No' ONLY\n")
   else:
      break
randomInteger = random.randint(1,3)
print("Random Integer is ", randomInteger)

if(randomInteger == 1):
   computerChoice = "Paper"
elif(randomInteger == 2):
   computerChoice = "Scissors"
elif(randomInteger == 3):
   computerChoice = "Rock"
   
print("Computer choice is ", computerChoice)