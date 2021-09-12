# Welcome to the python challenges of version 56.

"""
Write a Python program that simulates the "Rock, Paper, Scissors" game.

The game should ask the user to enter an option (either "Rock", "Paper", or "Scissors").

The player should play against the computer, which will select a random option.

The computer's selection will be compared against the player's selection to determine who wins.

A descriptive message should be displayed indicating if the player won, lost,
or if the game ended in a tie.

"""
import random


you_point = 0
opponent_point = 0


def game_start():
    print("=========== Welcome to the Game ===========")
    print("Game based on points with two members, starting points with 0 for both")
    print("Winning member gets +1 and the losing one gets -1 , if it is a tie nobody gets points\n Both can play unlimited times")

    member1 = "Shravan"
    member2 = input("Enter your name : ")
    member3 = member2.capitalize()

    choices = input("Please enter Rock, Paper, or Scissors Below : ")
    choice_cap = choices.capitalize()
    lists = ["Rock", "Paper", "Scissors"]
    opp_choice = random.choice(lists)

    print(f"Your's Choice : {choice_cap}")
    print(f"Opponent Choice : {opp_choice}")

    return game(you=choice_cap, opp=opp_choice, mem1=member1, mem2=member3)


def game(you, opp, mem1, mem2):
    global you_point
    global opponent_point
    if you == opp:
        print("It's a tie! Try again.")
        you_point += 0
        opponent_point += 0
        print(
            f"Points : {mem1} = {you_point} points and {mem2} = {opponent_point} points.\n ")
        try_again(mem1=mem1, mem2=mem2)
    elif you == "Paper" and opp == "Rock" or you == "Rock" and opp == "Scissors" or you == "Scissors" and opp == "Paper":
        print(f"You win! Your opponent chose {opp}")
        you_point += 1
        opponent_point += 0
        print(
            f"Points : {mem1} = {you_point} points and {mem2} = {opponent_point} points.\n ")
        try_again(mem1=mem1, mem2=mem2)
    else:
        print(f"You Lose! Your opponent chose {opp} ")
        you_point += 0
        opponent_point += 1
        print(
            f"Points : {mem1} = {you_point} points and {mem2} = {opponent_point} points.\n ")
        try_again(mem1=mem1, mem2=mem2)


def try_again(mem1, mem2):
    trying = input(
        "Do you want to play again.... Type y for Yes and n to exit : ")
    trying1 = trying.lower()
    if trying1 == "y":
        replay(mem1=mem1, mem2=mem2)
    elif trying1 == "n":
        game_end(mem2=mem2)


def replay(mem1, mem2):
    print("=========== Welcome to the Game Again ===========")
    choices = input(" Please enter Rock, Paper, or Scissors Below : ")
    choice_cap = choices.capitalize()
    lists = ["Rock", "Paper", "Scissors"]
    opp_choice = random.choice(lists)

    print(f"Your's Choice : {choice_cap}")
    print(f"Opponent Choice : {opp_choice}")

    return game(you=choice_cap, opp=opp_choice, mem1=mem1, mem2=mem2)


def game_end(mem2):
    print(f"BYE BYE {mem2}........ See you again *********")


game_start()
