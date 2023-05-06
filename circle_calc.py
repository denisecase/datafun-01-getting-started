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
import math  

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

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


# round the area to two decimal places
area = round(area, 2)

# log the results
logger.info(f"The area of a circle with radius {radius} is {area}.")
logger.info("Much better!")


# Use built-in open() function to read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())