"""
Purpose: Illustrate how to write data to a file, read data from a file, 
process the data, and write processed information to a new file. 

Illustrates pathlib and the joinpath function for safe cross-platform file path creation.

Author: Denise Case

This file name is:   dataio.py
This module name is: dataio

IO = input / output

CSV files are comma-separated values files.
They are text files and very common in data analytics.
CSV files are easy to read and write in Python.

csv.writer writes all data as a string.
csv.reader reads add data as a string.

Later, we'll use more powerful external libraries to read and write files, e.g.:
- pylightxl to read and write Excel files
- pandas to read and write csv, Excel, yaml, json, and more

@ uses csv module to read and write csv files
@ uses pathlib module to create and access a relative folders
"""
import csv
import pathlib

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# Declare a data directory to store data files
data_dir = pathlib.Path("data")

# Create it if it doesn't exist
data_dir.mkdir(exist_ok=True)

# Declare the input and output file paths 
inpath = data_dir.joinpath("inputs.csv")
outpath = data_dir.joinpath("outputs.csv")

# Write input data based on our list to inputs.csv - w is for write
with open(inpath, "w", newline="") as file_wrapper:
    writer = csv.writer(file_wrapper)
    # write our list to the csv file - each row is a list
    writer.writerow(["animal", "weight_lbs", "age_years", "visit_cost"])
    writer.writerow(["cat", 14.7, 3, 100.00])
    writer.writerow(["dog", 89.4, 5, 100.00])
    writer.writerow(["lizard", 0.85, 1, 100.00])
    
# Read our data from inputs.csv - r is for read
datalist = []
with open(inpath, "r", newline="") as file_wrapper:
    rdr = csv.reader(file_wrapper)
    datalist = list(rdr)

logger.info(f"Read data from {inpath}:\n{datalist}")

# Initialize an empty list to store the transformed data
outlist = []

# Iterate over the data rows using their indexes
# Starting at index 1 to skip the header row (index 0)
for index in range(1, len(datalist)):
    # Get the row at the current index (the first data row)
    row = datalist[index]

    # Read each row into named variables
    animal,weight_lbs,age_years,visit_cost = row

    # Access the cost of the visit  and double it
    visit_cost_float = float(visit_cost)
    updated_cost = visit_cost_float * 2

    # Combine unchanged elements with the doubled cost and create a new row
    new_row = animal, weight_lbs, age_years, updated_cost

    # Append the new row to the outlist
    outlist.append(new_row)


# Add the header row back to the output list
outlist.insert(0, datalist[0])

# Write our processed data to outputs.csv - w is for write
with open(outpath, "w", newline="") as file_wrapper:
    csv_writer = csv.writer(file_wrapper)
    csv_writer.writerows(outlist)

logger.info(f"Wrote data to {outpath}:\n{outlist}")
logger.info("Check out the new files in the data folder.")


# Use built-in open() function to read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())


