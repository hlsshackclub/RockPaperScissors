import random
import time

print("Welcome to Rock Paper Scissors!")

choices = ["rock", "paper", "scissors"]
choiceEmojis = ["🪨", "📄", "✂️"]
yourWinCount = 0
botWinCount = 0

while True:
    playerChoice = input("Enter your choice. (rock, paper, scissors): ")
    while(playerChoice not in choices):
        playerChoice = input("That is not a valid option. Please enter 'rock', 'paper', or 'scissors': ")
    playerChoiceNum = choices.index(playerChoice)

    botChoiceNum = random.randint(0, 2)
    botChoice = choices[botChoiceNum]

    time.sleep(0.5)
    playerChoiceEmoji = choiceEmojis[playerChoiceNum]
    print("🧑: " + playerChoiceEmoji)
    time.sleep(1)
    print("VS")
    time.sleep(1)
    botChoiceEmoji = choiceEmojis[botChoiceNum]
    print("🤖: " + botChoiceEmoji)
    
    time.sleep(1)
    if(playerChoiceNum == botChoiceNum):
        print("Its a draw")
    elif((playerChoiceNum + 1) % 3 == botChoiceNum): #is this too tricky?
        print("Bot wins!")
        botWinCount += 1
    else:
        print("You win!")
        yourWinCount += 1

    time.sleep(1)
    print("Score: 🧑 " + str(yourWinCount) + ", 🤖 " + str(botWinCount))
    
    time.sleep(1)
    if(input("Do you want to play again? (y, n): ") != "y"):
        print("Final score: 🧑 " + str(yourWinCount) + ", 🤖 " + str(botWinCount))
        print("Thanks for playing!")
        break
    else:
        print()