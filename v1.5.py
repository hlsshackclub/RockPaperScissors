import random
import time

print("Welcome to Rock Paper Scissors!")

playerChoice = input("Enter your choice. (rock, paper, scissors):")

botChoice = ''
botChoiceNum = random.randint(0, 2)
if(botChoiceNum == 0):
    botChoice = "rock"
elif(botChoiceNum == 1):
    botChoice = "paper"
else:
    botChoice = "scissors"

print("You have chosen: ")
time.sleep(0.5)
print(playerChoice)
time.sleep(0.5)
print("And the bot has chosen: ")
time.sleep(1)
print(botChoice)
time.sleep(0.5)
print("Thanks for playing!")