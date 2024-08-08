import random
import time

print("Welcome to Rock Paper Scissors!")

while True:
    playerChoice = input("Enter your choice. (rock, paper, scissors): ")
    while(playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors"):
        playerChoice = input("That is not a valid option. Please enter 'rock', 'paper', or 'scissors': ")

    botChoice = ""
    botChoiceNum = random.randint(0, 2)
    if(botChoiceNum == 0):
        botChoice = "rock"
    elif(botChoiceNum == 1):
        botChoice = "paper"
    else:
        botChoice = "scissors"

    time.sleep(0.5)
    playerChoiceEmoji = ""
    if(playerChoice == "rock"):
        playerChoiceEmoji = "🪨"
    if(playerChoice == "paper"):
        playerChoiceEmoji = "📄"
    if(playerChoice == "scissors"):
        playerChoiceEmoji = "✂️"
    print("🧑: " + playerChoiceEmoji)
    time.sleep(1)
    print("VS")
    time.sleep(1)
    botChoiceEmoji = ""
    if(botChoice == "rock"):
        botChoiceEmoji = "🪨"
    if(botChoice == "paper"):
        botChoiceEmoji = "📄"
    if(botChoice == "scissors"):
        botChoiceEmoji = "✂️"
    print("🤖: " + botChoiceEmoji)
    time.sleep(1)
    if(playerChoice == "rock" and botChoice == "rock"):
        print("Its a draw")
    elif(playerChoice == "rock" and botChoice == "scissors"):
        print("You win!")
    elif(playerChoice == "rock" and botChoice == "paper"):
        print("Bot wins!")
    elif(playerChoice == "scissors" and botChoice == "scissors"):
        print("Its a draw")
    elif(playerChoice == "scissors" and botChoice == "paper"):
        print("You win!")
    elif(playerChoice == "scissors" and botChoice == "rock"):
        print("Bot wins!")
    elif(playerChoice == "paper" and botChoice == "paper"):
        print("Its a draw")
    elif(playerChoice == "paper" and botChoice == "rock"):
        print("You win!")
    else:
        print("Bot wins!")

    time.sleep(1)

    if(input("Do you want to play again? (y, n): ") != "y"):
        print("Thanks for playing!")
        break
    else:
        print()