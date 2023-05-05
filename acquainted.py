"""
Purpose: Get acquainted with basic Python concepts.

Author: Denise Case

This file name is:   acquainted.py
This module name is: acquainted

Statements

All Python programs are composed of statements.
Statements are instructions that tell the computer to do something.
Each statement is written on a separate line.

Variables

Variables are used to store values.
Variables are created when they are first assigned a value.
Variables are used to refer to values later in the program.
Variables can be reassigned to refer to a different value.

Comments

Comments are used to document code.
Comments are ignored by the Python interpreter.
Comments are preceded by the # symbol.
Comments can be placed on their own line or at the end of a line.
Comments can be used to disable code.

Opening Remarks

These introductory remarks are comments. 
By wrapping a comment in triple quotes, we can make multi-line comments.

"""

# import some free code from the Python Standard Library
import logging
import pathlib

# Create a logs directory if it doesn't exist
logs_dir = pathlib.Path("logs")
logs_dir.mkdir(exist_ok=True)

# Create a log file name using the built-in __file__ variable
module_name = pathlib.Path(__file__).stem
log_file_name = logs_dir.joinpath(module_name + "log")

# set up a basic logger
logging.basicConfig(filename=log_file_name, filemode='w', level=logging.DEBUG, format='%(asctime)s %(message)s')

# Declare some variables - Python can figure out what type they are
# Try some string, integer, float, and boolean (True/False) variables
# TODO: Customize these by changing the values 
name = "John Doe"
state = "California"
country = "USA"

pet_count = 1
skill_count = 24

temperature_f = 81.5
pet_weight_lbs = 12.5

has_dog = False
likes_analytics = True
likes_python = True

# Log some information using f-strings (formatted strings)
# f-strings are a convenient way to embed variables in strings
# note that the f is placed BEFORE the opening quote
logging.info(f"Name: {name} ")
logging.info(f"State: {state}")
logging.info(f"Country: {country}")

logging.info(f"Pet count: {pet_count}")
logging.info(f"Skill count: {skill_count}")

logging.info(f"Temperature: {temperature_f}")
logging.info(f"Pet weight: {pet_weight_lbs}")

logging.info(f"Has dog: {has_dog}")
logging.info(f"Likes analytics: {likes_analytics}")
logging.info(f"Likes Python: {likes_python}")

# Print logged information to the terminal
with open(log_file_name, 'r') as file:
    print(file.read())
