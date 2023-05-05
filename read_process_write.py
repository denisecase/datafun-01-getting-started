"""
Purpose: Read a csv file, process the data, and write a new csv file.

Author: Denise Case

This file name is:   read_process_write.py
This module name is: read_process_write

CSV files are comma-separated values files.
They are text files and very common in data analytics.
CSV files are easy to read and write in Python.

"""
# import some free code from the Python Standard Library
import csv
import logging
import pathlib

# Create directories if they don't exist for data and logs
logs_dir = pathlib.Path("logs")
logs_dir.mkdir(exist_ok=True)
data_dir = pathlib.Path("data")
data_dir.mkdir(exist_ok=True)

# Create a log file name using the built-in __file__ variable
module_name = pathlib.Path(__file__).stem
log_file_name = logs_dir.joinpath(module_name + ".log")

# Set up a basic logger
logging.basicConfig(
    filename=log_file_name,
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
)

# Declare some variables 
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

logging.info(f"Read data from {inpath}:\n{datalist}")

# Process the data as you like - we'll double the cost of each visit
outlist = []

# Skip the header row and process the data rows
for row in datalist[1:]:
    new_row = row[:3] + [float(row[3]) * 2]  # Double the visit cost
    outlist.append(new_row)

# Add the header row back to the output list
outlist.insert(0, datalist[0])

# Write our processed data to outputs.csv - w is for write
with open(outpath, "w", newline="") as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerows(outlist)

logging.info(f"Wrote data to {outpath}:\n{outlist}")

# Print logged information to the terminal
with open(log_file_name, "r") as file:
    print(file.read())

# TODO: Rather than doubling each input, transform it in a different way.