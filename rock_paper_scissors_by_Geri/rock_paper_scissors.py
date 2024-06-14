import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"


def get_player_move():
    invalid_player_moves = 0

    while True:
        print("Choose [r] for rock, [p] for paper, or [s] for scissors: ")
        player_move = input()

        if player_move == "r":
            player_move = rock
            break
        elif player_move == "p":
            player_move = paper
            break
        elif player_move == "s":
            player_move = scissors
            break
        else:
            invalid_player_moves += 1

            if invalid_player_moves == 3:
                raise SystemExit("Invalid Input. Try again...")
            print(f"You entered an invalid move. \n{3 - invalid_player_moves} attempts left.")

    return player_move


def get_computer_move():

    computer_move = ""
    random_move = random.randint(1, 3)

    if random_move == 1:
        computer_move = rock
    elif random_move == 2:
        computer_move = paper
    elif random_move == 3:
        computer_move = scissors

    print(f"Computer choice was: {computer_move}.")
    return computer_move


def get_winner(player_move, computer_move):

    if (player_move == rock and computer_move == scissors) or \
            (player_move == scissors and computer_move == paper) or \
            (player_move == paper and computer_move == rock):
        print("You win!")
    elif player_move == computer_move:
        print("Draw")
    else:
        print("You lose!")


player_validated_move = get_player_move()
computer_random_move = get_computer_move()
get_winner(player_validated_move, computer_random_move)
