"""
Purpose: Provide useful information to help with debugging.

Author: Denise Case

This file name is:   about.py
This module name is: about

It uses a triple-quoted string to provide a description of the file.
"""

# import some free code from the Python Standard Library
import datetime
import logging
import os
import pathlib
import platform
import sys

# Create a logs directory if it doesn't exist
logs_dir = pathlib.Path("logs")
logs_dir.mkdir(exist_ok=True)

# Create a log file name using the built-in __file__ variable
module_name = pathlib.Path(__file__).stem
log_file_name = logs_dir.joinpath(module_name + "log")

# set up a basic logger
logging.basicConfig(filename=log_file_name, filemode='w', level=logging.DEBUG)

# declare some variables
divider_string = "============================================================="
python_version_string  = platform.python_version()
active_pip_env = os.environ.get('PIP_DEFAULT_ENV')
today = datetime.date.today()

# define some functions (reusuable bits of code)
def get_source_directory_path():
    """Returns the absolute path to this source directory."""
    dir = os.path.dirname(os.path.abspath(__file__))
    return dir

# log some useful information
logging.info(divider_string)
logging.info(divider_string)
logging.info(f"Welcome!")
logging.info(f"Today is {today} at {datetime.datetime.now().strftime('%I:%M %p')}")
logging.info(f"This file is running on: {os.name} {platform.system()} {platform.release()}")
logging.info(f"The Python version is: {python_version_string}")
logging.info(f"The active conda environment is:  {os.environ.get('CONDA_DEFAULT_ENV') }")
logging.info(f"The active pip environment is:    {os.environ.get('PIP_DEFAULT_ENV') }")
logging.info(f"The active environment path is:   {sys.prefix}")
logging.info(f"The current working directory is: {os.getcwd()}")
logging.info(f"This source file is in:           {get_source_directory_path()}")
logging.info(divider_string)
logging.info(divider_string)

# Print logged information to the terminal
with open(log_file_name, 'r') as file:
    print(file.read())
