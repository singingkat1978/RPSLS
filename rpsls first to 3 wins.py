#Hello world. This is my first test program in Python.
#I followed the lesson here http://www.thehelloworldprogram.com/python/python-game-rock-paper-scissors/
#and then added on some BBT love.

from random import randint
t = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
human_score = 0
computer_score = 0
user_has_quit = False
while not user_has_quit:
    while not (computer_score >= 3 or human_score >= 3):
        computer = t[randint(0,4)]
        player = input("Rock, Paper, Scissors, Lizard, Spock?  ")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Spock":
                print("You lose!", computer, "vaporizes", player)
                computer_score += 1
            elif computer == "Paper":
                print("You lose!", computer, "covers", player)
                computer_score += 1
            elif computer == "Lizard":
                print("You win!", player, "crushes", computer)
                human_score += 1
            elif computer == "Scissors":
                print("You win!", player, "smashes", computer)
                human_score += 1
        elif player == "Paper":
            if computer == "Spock":
                print("You win!", player, "disproves", computer)
                human_score += 1
            elif computer == "Rock":
                print("You win!", player, "covers", computer)
                human_score += 1
            elif computer == "Lizard":
                print("You lose!", computer, "eats", player)
                computer_score += 1
            elif computer == "Scissors":
                print("You lose!", computer, "cuts", player)
                computer_score += 1
        elif player == "Scissors":
            if computer == "Spock":
                print("You lose!", computer, "smashes", player)
                computer_score += 1
            elif computer == "Rock":
                print("You lose!", computer, "crushes", player)
                computer_score += 1
            elif computer == "Lizard":
                print("You win!", player, "decapitates", computer)
                human_score += 1
            elif computer == "Paper":
                print("You win!", player, "cuts", computer)
                human_score += 1
        elif player == "Lizard":
            if computer == "Spock":
                print("You win!", player, "poisons", computer)
                human_score += 1
            elif computer == "Paper":
                print("You win!", player, "eats", computer)
                human_score += 1
            elif computer == "Rock":
                print("You lose!", computer, "crushes", player)
                computer_score += 1
            elif computer == "Scissors":
                print("You lose!", computer, "decapitates", player)
                computer_score += 1
        elif player == "Spock":
            if computer == "Paper":
                print("You lose!", computer, "disproves", player)
                computer_score += 1
            elif computer == "Lizard":
                print("You lose!", computer, "poisons", player)
                computer_score += 1
            elif computer == "Rock":
                print("You win!", player, "vaporizes", computer)
                human_score += 1
            elif computer == "Scissors":
                print("You win!", player, "smashes", computer)
                human_score += 1
        else:
            print("That's not a valid entry. Check your spelling!")
    print("Final score: Human -", human_score, "Computer -", computer_score)

    answer = input("Would you like to play again? ")

    if answer in ["Yes", "yes", "YES"]:
        human_score = 0
        computer_score = 0
    else:
        user_has_quit = True
print ("Thanks for playing!")
