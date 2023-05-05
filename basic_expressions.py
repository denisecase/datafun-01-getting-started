"""
Purpose: Illustrate basic expresssions and operators in Python.

Author: Denise Case

This file name is:   basic_expressions.py
This module name is: basic_expressions

Expressions

Data analytics is all about getting value out of data.
Expressions are the building blocks of data analytics.

Rather like math expressions, or Excel expressions, Python expressions
are a combination of values, variables, operators, and function calls.

Expressions are made of operands and operators.

- Operators are symbols like +, -, *, /, and =.
- Operands can be values or variables, 
  and can include function calls like len() and str().

Writing expressions in Python is like writing formulas in Excel.
 
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

# Declare some variables 
# TODO: Try changing the values of these variables
triangle_base = 10
triangle_height = 5
i = 50
j = 20
a = 1.1
b = 2.2
c = 3.3

# Try some operators (multiply, divide, add, subtract)
triangle_area = triangle_base * triangle_height / 2
sum = a + b
difference = i - j

# Log some information using f-strings (formatted strings)
logging.info(f"triangle_area = {triangle_area}")
logging.info(f"sum = {sum}")
logging.info(f"difference = {difference}")


# Print logged information to the terminal
with open(log_file_name, 'r') as file:
    print(file.read())
