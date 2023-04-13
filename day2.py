import random
def get_choices():
    player_choice = input("enter a choice(rock, paper, scissors:")
    # list
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    # dict in python (dictionary)
    choices = {"player": player_choice, "computer": str(computer_choice)}
    return choices

# function arguments
def check_win(player, computer):
    # concat using f string
    print(f"you choose {player}, computer chose {computer}")
    # if statement
    if player == computer:
        return "its a tie!"
    elif player == "rock":
         # nested elif
        if computer == "scissors":
            return "rock smashes scissors! You win!"
        else:
            return "paper cover rock! You Lose."
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock! You win!"
        else:
            return "scissors cuts paper! You Lose."
    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper! You win!"
        else:
            return "rock smashes scissors! You Lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
