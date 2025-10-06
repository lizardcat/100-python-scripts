import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while True:
    player = input("Choose rock, paper, scissors or q to quit: ").lower()
    if player == "q":
        print(f"\nFinal score - You: {player_score}, Computer: {computer_score}")
        break
    if player not in choices:
        print("Invalid choice")
        continue

    computer = random.choice(choices)
    print(f"Computer chose {computer}")

    if player == computer:
        print("Tie")
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("You win this round")
        player_score += 1
    else:
        print("You lose this round")
        computer_score += 1

    print(f"Score - You: {player_score}, Computer: {computer_score}\n")
