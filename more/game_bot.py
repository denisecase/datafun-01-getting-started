"""
Purpose: Practice Python by customizing a game. 

Author: Denise Case (change to your name after customizations!)

"""
import logging
import pathlib
import random

# setup logging
logs_dir = pathlib.Path("logs")
logs_dir.mkdir(exist_ok=True)
module_name = pathlib.Path(__file__).stem
logname = logs_dir.joinpath(module_name + ".log")
logging.basicConfig(filename=logname, filemode='w', level=logging.DEBUG)

# TODO: Change the name from GameBot to something else.
name = "GameBot"
logging.info(f"Bot says: Hi, my name is {name}!\n")

# TODO: Change the function name to get_result (be sure to change it everywhere it's used)
def get_game_result(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "We tied!"
    elif (user_choice == "wolf" and bot_choice == "eagle") or (user_choice == "eagle" and bot_choice == "snake") or (user_choice == "snake" and bot_choice == "wolf"):
        return "You won!"
    else:
        return "I won!"

#TODO: Change the following line to use an f-string and {name} variable.
print("Hello, I'm " + name + ", your gamebot.")
print("Let's play rock, paper, scissors!")
print("  Rock crushes scissors.")
print("  Scissors cuts paper.")
print("  Paper covers rock.")
print("I'll pick one and you pick one and we'll see who wins.\n")

logging.info("Bot explained rock > scissors > paper > rock")    

# Make our choices lowercase to make comparisons easier.

user_choice = input("Enter your choice (rock, scissors, or paper): ").lower()

bot_choice = random.choice(["rock", "scissors", "paper"])

result = get_game_result(user_choice, bot_choice)

logging.info(f"Bot says: you choose {user_choice}, and I choose {bot_choice}. {result}")


# Use built-in open() function to read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())
