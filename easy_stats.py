"""

Purpose: Illustrate the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

Uses only Python Standard Library modules.

@ uses statistics module for descriptive stats
@ uses turtle module for drawing a chart
@ uses sys module for checking Python version

"""
import statistics 
import turtle  
import sys  

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# Descriptive: Univariant Data..................................

# univariant data (one varabile, many readings)
uni_data = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]
logger.info("uni_data = " + str(uni_data))

# Descriptive: Averages and measures of central tendency

mean = statistics.mean(uni_data)
median = statistics.median(uni_data)
mode = statistics.mode(uni_data)

# log use variable colon formatting to avoid unnecessary digits (e.g. .2f)

logger.info(f"mean   = {mean:.2f}")  
logger.info(f"median = {median:.2f}")
logger.info(f"mode   = {mode:.2f}")

# Descriptive: Measures of spread

var = statistics.variance(uni_data)
stdev = statistics.stdev(uni_data)
lowest = min(uni_data)
highest = max(uni_data)

# TODO: change to f-strings and use 2 decimal places (like we did above)
logger.info("var    = " + str(var))
logger.info("stdev  = " + str(stdev))
logger.info("lowest = " + str(lowest))
logger.info("highest= " + str(highest))


# Descriptive: Univariant Timeseries Data.........................

# describe relationships
# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
xtimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
yvalues = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31, 32]

# if the lists are not the same size,
# log an error and quit the program
if len(xtimes) != len(yvalues):
    logger.error("ERROR: The related sets are not the same size.")
    logger.error(f"      {len(xtimes)}!={len(yvalues)}")
    quit()

# check the Python version before using the correlation function
logger.warn("Correlation requires Python version 3.10 or greater.")
logger.warn(f"Your version is {sys.version_info.major}.{sys.version_info.minor}")

# if the Python version is too old, we can quit now
if sys.version_info.minor < 10:
    logger.error("Please update Python to 3.10 or greater")
    logger.error("or use View / Command Palette / Python: Select Interpreter")
    logger.error("to get a newer one.")
    quit()

# If we're still here, use the correlation function from the statistics module
xx_corr = statistics.correlation(xtimes, xtimes)
xy_corr = statistics.correlation(xtimes, yvalues)

# log the information 
logger.info("Here's some time series data:")
logger.info(f"xtimes:{xtimes}")
logger.info(f"yvalues:{yvalues}")
logger.info(f"correlation between xtimes and xtimes = {xx_corr:.2f}")
logger.info(f"correlation between xtimes and yvalues = {xy_corr:.2f}")

# Calculate slope and intercept of a line

# Here's some bivariant data (two series of data)

arrayX = [-200, -150, -100, 50, 0, 50, 100, 150]
arrayY = [-240, -165, -99, 35, 19, 75, 130, 125]

# Call linear_regression() function -
# and get back 2 values: slope and intercept
# describing the 'best fit' line through the data
slope, intercept = statistics.linear_regression(arrayX, arrayY)

# Choose an x value off in the future (future x)
future_x = 200

# Extend the line out into the unknown future
# and read the value (of future y)
future_y = round(slope * future_x + intercept)

logger.info("Here's some bivariant data (2 variables, together):")
logger.info(f"x:{arrayX}")
logger.info(f"y:{arrayY}")
logger.info("Calculate the slope and intercept of a best fit straight line:")
logger.info(f"   slope = {slope:.2f}")
logger.info(f"   intercept = { intercept:.2f}")
logger.info("Let's use our best fit line to PREDICT a future value.")
logger.info(f"   At future x = {future_x:d},")
logger.info(f"   we predict the value of y will be { future_y:d}.")
logger.info("How'd we do? Does this make sense given the data?")
logger.info("Remember to close the app. Control c (or d or z maybe) to close it.")

# is the user ready to see a chart?
# TODO: change this to True when ready
ready_for_chart = False

logger.info(f"ready_for_chart = {ready_for_chart}")

# if ready for the chart, show the data, the best fit line, and the future prediction

if ready_for_chart:

    screen = turtle.Screen()
    screen.title("Linear Regression and Prediction")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(3)  # range 1-10  (slow-fast)

    w, h = screen.window_width(), screen.window_height()
    # e.g. 512, 480

    # Draw Axes
    t.penup()
    t.goto(w / 2, 0)
    t.pendown()
    t.goto(-w / 2, 0)
    t.penup()
    t.goto(0, h / 2)
    t.pendown()
    t.goto(0, -h / 2)

    # draw points
    for index, year in enumerate(arrayX):
        t.penup()
        t.goto(arrayX[index], arrayY[index])
        t.pendown()
        t.pencolor("blue")
        t.dot(20)

    # draw best-fit line
    h = int(slope * w + intercept)
    t.penup()
    t.goto(w, h)
    w = -w
    h = int(slope * w + intercept)
    t.pencolor("green")
    t.pensize(2)
    t.pendown()
    t.goto(w, h)

    # draw prediction dot
    t.penup()
    t.goto(future_x, future_y)
    t.pendown()
    t.pencolor("red")
    t.dot(20)

    turtle.done()
    screen.mainloop()
    logger.info("Done with the chart.")

else:
    logger.info("Ready for a chart? Edit this program to see an illustration.\n")

# Use built-in open() function to read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())