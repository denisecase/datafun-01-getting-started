"""

Purpose: Calculate the area of a circle.

Author: Denise Case

This script illustrates importing modules and using constants.

It illustrates the built-in function round().

When we install Python, it comes with the Python standard library.
Nearly all scripts will import at least one module from the standard library.

We can install additional, third-party modules using pip.
We'll do that later. 

All scripts in this repository use only the standard library.

@uses math module for pi constant

"""
# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------

# Import from Python Standard Library

import math

# Use the math module's constant for pi
pi = math.pi

# get the radius from the user - input result is always a string
# Use \n to add a blank new line to the terminal before we ask for input
radius_string = input("\nEnter the radius of a circle: ")

# convert the radius_string to a number
radius = float(radius_string)

# calculate the area using the numeric value (not the string)
area = pi * radius**2

# log the results
logger.info(f"The area of a circle with radius {radius} is {area}.")
logger.info("Eww... that's a lot of decimal places - tmi!")


# TODO Round the area to two decimal places.
# Pass in 2 arguments to the round() function.
#     The first argument is the value to round.
#     The second argument is the number of decimal places (make it 2 not 12)
area = round(area, 12)

# log the results
logger.info(f"The area of a circle with radius {radius} is {area}.")
logger.info("Much better! (After you fix it.)")
