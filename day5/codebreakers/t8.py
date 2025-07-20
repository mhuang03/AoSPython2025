import random

beats = {"R": "S", "P": "R", "S": "P"}
names = {"R": "Rock", "P": "Paper", "S": "Scissors"}

comp_score, player_score = 0, 0
player = ""
while True:
    comp = random.choice(["R", "P", "S"])

    player = input("Rock (R), Paper (P), Scissors (S), or exit (X)? ")
    while player not in ["R", "P", "S", "X"]:
        player = input("Please enter one of R, P, S, or X: ")

    if player == "X":
        break

    print(f"Computer played {names[comp]}")
    if comp == player:
        print("Tie!")
    elif beats[player] == comp:
        print("You win!")
        player_score += 1
    else:
        print("You lose.")
        comp_score += 1
    print()

print(f"Final score: Computer - {comp_score} to Player - {player_score}")
