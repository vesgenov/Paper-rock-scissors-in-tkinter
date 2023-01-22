from tkinter import *
import random

computer_move = 0
player_move = ''

player_wins = 0
computer_wins = 0


def scoreboard():                                           # scoreboard
    print(f"Score: Computer: {computer_wins}     Player: {player_wins}")

root = Tk()
root.title('Paper - Rock - Scissors   by vesGenov')
root.geometry('400x400')


def create_game_buttons():
    rock_button = Button(root, text='PAPER', command=paper())
    rock_button.pack(padx=20, pady=10)
    rock_button = Button(root, text='ROCK', command=rock())
    rock_button.pack(padx=20, pady=10)
    rock_button = Button(root, text='SCISSORS', command=scissors())
    rock_button.pack(padx=20, pady=10)


def computer_move_func(a):
    a = random.randint(1, 3)  # computer move
    if a == 1:  # equalize move (number changes to string)
        a = "paper"
    elif a == 2:
        a = "rock"
    elif a == 3:
        a = "scissors"


    label_computer_move = Label(text=f'Computer chose {a}')
    label_computer_move.pack(pady=20)
#   label_start = Label(text=f'Computer chose {computer_move}')
#   label_start.pack(pady=0)


def fight(a, d, b, c):
    if a == d:                # main logic - draw game
        print(f"You both choose {d}.")
        print("Game is draw")
        scoreboard()

    else:
        print(f"Computer choose {a}.")
        print(f"You choose {d}.")

    if a == "paper":                            # main logic - someone wins
        if d== "rock":
            print("Paper over the rock. Computer wins!")
            b += 1
        elif player_move == "scissors":
            print("The scissors cut the paper. Player wins!")
            c += 1
    elif a == "rock":
        if d == "scissors":
            print("The rock breaks the scissors. Computer wins!")
            b += 1
        elif d == "paper":
            print("Paper over the rock. Player wins!")
            c += 1
    elif a == "scissors":
        if d == "paper":
            print("The scissors cut the paper. Computer wins!")
            b += 1
        elif d == "rock":
            print("The rock breaks the scissors. Player wins!")
            c += 1


def rock():
    player_move = 'rock'
    fight(computer_move, player_move, computer_wins, player_wins)

def paper():
    player_move = 'paper'
    fight(computer_move, player_move, computer_wins, player_wins)

def scissors():
    player_move = 'scissors'
    fight(computer_move, player_move, computer_wins, player_wins)


def game_start():
    label_start = Label(text='The game has started')
    label_start.pack(pady=20)
    start_button.destroy()
    label_title = Label(text='Paper - Rock - Scissors   by vesGenov')
    label_title.pack(pady=20)
    computer_move_func(computer_move)


def comb_func_1():
    game_start()
    create_game_buttons()
    label_game()

    label_player_move = Label(text=f'Player chose {player_move}')
    label_player_move.pack(pady=20)


def label_game():
    label_game = Label(text='Paper, rock or scissors? Choose your destiny!!!')
    label_game.pack(pady=20)


start_button = Button(root, text='Start game', command=comb_func_1)
start_button.pack(pady=20)


mainloop()
