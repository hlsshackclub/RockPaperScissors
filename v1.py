import random

print("Welcome to Rock Paper Scissors!")

playerChoice = input("Enter your choice. (rock, paper, scissors): ")

botChoice = ''
botChoiceNum = random.randint(0, 2)
if(botChoiceNum == 0):
    botChoice = "rock"
elif(botChoiceNum == 1):
    botChoice = "paper"
else:
    botChoice = "scissors"

print("You have chosen: " + playerChoice)
print("And the bot has chosen: " + botChoice)
print("Thanks for playing!")