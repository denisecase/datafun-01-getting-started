"""
Purpose: Get acquainted with basic Python concepts.

Author: Denise Case

This file name is:   acquainted.py
This module name is: acquainted

Statements:
- All Python programs are composed of statements.
- Statements are instructions that tell the computer to do something.
- Each statement is written on a separate line.

Variables:
- Variables are used to store values.
- Variables are created when they are first assigned a value.
- Variables are used to refer to values later in the program.
- Variables can be reassigned to refer to a different value.

Comments:
- Comments are used to document code.
- Comments are ignored by the Python interpreter.
- Comments are preceded by the # symbol.
- Comments can be placed on their own line or at the end of a line.
- Comments can be used to disable code.

Opening Remarks:
- These introductory remarks are comments. 
- By wrapping a comment in triple quotes, we can make multi-line comments.
"""

# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------


# Declare some variables - Python will infer the data type
# Try string, integer, float, and boolean (True/False) variables

# TODO: Customize these by changing the values - use your own name, etc.

# String data types
name = "John Doe"
state = "California"
country = "USA"

# Integer data types
pet_count = 1
skill_count = 24

# Float data types (floating point numbers, with a decimal point)
temperature_f = 81.5
pet_weight_lbs = 12.5


# Boolean data types (True or False)
has_dog = False
likes_analytics = True
likes_python = True

# Log some information using f-strings (formatted strings)
# f-strings are a convenient way to embed variables and expressions in strings
# the f is placed BEFORE the opening quote
# and variables (or expressions) are placed inside curly braces

logger.info(f"Name: {name} ")
logger.info(f"State: {state}")
logger.info(f"Country: {country}")
logger.info(f"Pet count: {pet_count}")
logger.info(f"Double the pet count: {pet_count * 2}")
logger.info(f"Skill count: {skill_count}")
logger.info(f"Temperature: {temperature_f}")
logger.info(f"Pet weight: {pet_weight_lbs}")
logger.info(f"Has dog: {has_dog}")
logger.info(f"Likes analytics: {likes_analytics}")
logger.info(f"Likes Python: {likes_python}")
