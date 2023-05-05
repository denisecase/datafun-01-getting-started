"""
Purpose: Illustrate basic functions in Python.

Author: Denise Case

This file name is:   basic_functions.py
This module name is: basic_functions

Functions

Functions are reusable bits of code.
Functions are defined using the def keyword.
Functions are called using the function name and parentheses.
Functions can accept parameters (arguments).
Functions can return values.

Built-in Functions

Python has many helpful built-in functions.

len() is a built-in function that returns the length of an object.
min() is a built-in function that returns the smallest item in an iterable.
max() is a built-in function that returns the largest item in an iterable.  

print() is a built-in function that prints to the screen.
input() is a built-in function that gets input from the user.

str() is a built-in function that converts a value to a string.
int() is a built-in function that converts a value to an integer.


"""
# import some free code from the Python Standard Library
import logging
import pathlib
import webbrowser

# Create a logs directory if it doesn't exist
logs_dir = pathlib.Path("logs")
logs_dir.mkdir(exist_ok=True)

# Create a log file name using the built-in __file__ variable
module_name = pathlib.Path(__file__).stem
log_file_name = logs_dir.joinpath(module_name + "log")

# set up a basic logger
logging.basicConfig(filename=log_file_name, level=logging.DEBUG, format='%(asctime)s %(message)s')

# Declare some variables
url = "https://docs.python.org/3/library/functions.html"
number_list = [1, 2, 3, 4, 5]
length = len(number_list)
smallest = min(number_list)
largest = max(number_list)
hint = "HINT: In the terminal, hit up arrow to rerun a command.\n"

# Log some information 
logging.info(f"url = {url}")
logging.info(f"number_list = {number_list}")
logging.info(f"len(number_list) = {length}")
logging.info(f"min(number_list) = {smallest}")
logging.info(f"max(number_list) = {largest}")

# print an empty line to the terminal
print()

# print a string to the terminal
print("Greetings!")

# get input from the user
name = input("What's your name? (type your name and hit enter):")

# use what you got (their name) to print a greeting
message = "Hello " + name.capitalize() + "!"
print(message)
print()
logging.info(f"message = {message}")

response = input("Would you like to see all the built-in functions? (y/n)")
logging.info(f"response = {response}")
print(f"You said {response}!")
print(f"{hint}")

if response == "y":
    print()
    print("Let's open a web page. Python makes it easy!")
    webbrowser.open_new(url)
    print()
    print("There's a lot of built-in functions ready to use!")
    print("We'll learn more about them later.")
    print()

# TODO: Try running this with different responses n, y, other...