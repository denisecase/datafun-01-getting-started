import csv

# Declare a variable to hold the input file name
input_file_name = "list_zipperout.csv"

# Declare a variable to hold the output file name
output_file_name = "read_process_writeout.csv"

# Create a file object for input (r = read access)
input_file = open(input_file_name, "r")

# Create a file object for output (w = write access)
output_file = open(output_file_name, "w")

# Create a csv reader object to make it a bit easier
csvreader = csv.reader(input_file)

# for each row in the csv reader object
for csvrow in csvreader:

    # unpack the tuple e.g., (x,y) into variables named x and y
    x, y = csvrow

    # process the data as desired - here we just add y squared
    y_squared = float(y) ** 2

    # create a string including the additional columns
    # end each line with a newline character \n
    outrow = f"{x},{y},{y_squared}\n"

    # write the string to the output file
    output_file.write(outrow)


# close the file objects when done
input_file.close()
output_file.close()
