import random
computer_move = random.randint(1, 3)

paper = 1
rock = 2
scissors = 3

computer_wins = 0
player_wins = 0


def scoreboard():                                           # scoreboard
    print(f"Score: Computer: {computer_wins}     Player: {player_wins}")


while True:
    computer_move = random.randint(1, 3)        # computer move
    if computer_move == 1:                      # equalize move (number changes to string)
        computer_move = "paper"
    elif computer_move == 2:
        computer_move = "rock"
    elif computer_move == 3:
        computer_move = "scissors"

    print("Paper = 1, rock = 2, scissors = 3. Choose your destiny!")  # print main line
    player_move = input()                                               # take player move

    if not player_move.isdigit():                                          # input test
        if player_move == "quit" or player_move == "exit":
            scoreboard()
            break
        else:
            print("Wrong input! Try again!")
            continue


    if player_move == "1":                                # equalize player move (number changes to string)
        player_move = "paper"
    elif player_move == "2":
        player_move = "rock"
    elif player_move == "3":
        player_move = "scissors"

    if computer_move == player_move:                # main logic - draw game
        print(f"You both choose {player_move}.")
        print("Game is draw")
        scoreboard()
        continue
    else:
        print(f"Computer choose {computer_move}.")
        print(f"You choose {player_move}.")

    if computer_move == "paper":                            # main logic - someone wins
        if player_move == "rock":
            print("Paper over the rock. Computer wins!")
            computer_wins += 1
        elif player_move == "scissors":
            print("The scissors cut the paper. Player wins!")
            player_wins += 1
    elif computer_move == "rock":
        if player_move == "scissors":
            print("The rock breaks the scissors. Computer wins!")
            computer_wins += 1
        elif player_move == "paper":
            print("Paper over the rock. Player wins!")
            player_wins += 1
    elif computer_move == "scissors":
        if player_move == "paper":
            print("The scissors cut the paper. Computer wins!")
            computer_wins += 1
        elif player_move == "rock":
            print("The rock breaks the scissors. Player wins!")
            player_wins += 1

    scoreboard()
    continue
