"""

This example illustrates stats using the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

Uses only Python Standard Library modules.

"""

# imports at the top of the file

import statistics  # for descriptive stats
import turtle  # for drawing a chart
import sys  # for checking Python version

# is the user ready to see a chart?

ready_for_chart = True  # edit this when ready

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

# Descriptive: Averages and measures of central tendency

mean = statistics.mean(uni_data)
median = statistics.median(uni_data)
mode = statistics.mode(uni_data)

# Descriptive: Measures of spread

var = statistics.variance(uni_data)
stdev = statistics.stdev(uni_data)
lowest = min(uni_data)
highest = max(uni_data)

# use variable colon formatting to avoid unnecessary digits (e.g. .2f)
print()
print("=============================================================")
print()
print(f"Here's some univariant data (1 variable, many readings): {uni_data}")
print()
print("Descriptive statistics include measures of central tendancy:")
print(f"   mean={mean:.2f}")
print(f"   median={median:.2f}")
print(f"   mode={mode:.2f}")
print()
print("Descriptive statistics include measures of spread:")
print(f"   var={var:.2f}")
print(f"   stddev={stdev:.2f}")
print()

# Descriptive: Univariant Timeseries Data.........................

# describe relationships
# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
xtimes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
yvalues = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31, 32]

# if the lists are not the same size,
# print an error and quit the program
if len(xtimes) != len(yvalues):
    print("ERROR: The related sets are not the same size.")
    print(f"      {len(xtimes)}!={len(yvalues)}")
    quit()

print("Correlation requires Python version 3.10 or greater.")
print(f"Your version is {sys.version_info.major}.{sys.version_info.minor}")

if sys.version_info.minor < 10:
    print()
    print("Please update Python to 3.10 or greater")
    print("or use View / Command Palette / Python: Select Interpreter")
    print("to get a newer one.")
    print()
    quit()

# If we're still here, use the correlation function
xx_corr = statistics.correlation(xtimes, xtimes)
xy_corr = statistics.correlation(xtimes, yvalues)

# share what we learned
print()
print("=============================================================")
print()
print("Here's some time series data:")
print()
print(f"xtimes:{xtimes}")
print()
print(f"yvalues:{yvalues}")
print()
print(
    "Descriptive stats for time series may include measures of",
    "relationshiop or correlation:",
)
print()
print(f"   correlation between xtimes and xtimes = {xx_corr:.2f}")
print(f"   correlation between xtimes and yvalues = { xy_corr:.2f}")
print()
print(
    "Learn what else is possible at",
    "https://docs.python.org/3/library/statistics.html.",
)
print()


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

print()
print("=============================================================")
print()
print("Here's some bivariant data (2 variables, together):")
print()
print(f"x:{arrayX}")
print()
print(f"y:{arrayY}")
print()
print("Calculate the slope and intercept of a best fit straight line:")
print()
print(f"   slope = {slope:.2f}")
print(f"   intercept = { intercept:.2f}")
print()
print("Let's use our best fit line to PREDICT a future value.")
print()
print(f"   At future x = {future_x:d},")
print(f"   we predict the value of y will be { future_y:d}.")
print()
print("How'd we do? Does this make sense given the data?")
print()
print("Remember to close the app. Control c (or d or z maybe) to close it.")
print()


# if ready for the chart, let's show
# the data, the best fit line, and the future prediction

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
    print()

else:
    print("Ready for a chart? Edit this program to see an illustration.")
    print()
