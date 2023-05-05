"""

This example illustrates how easy it is to build a
simple cross-platform, native app with Python.

Build a simple app that runs on Windows, or Mac, or Linux machines 
as a native app.

Uses only Python Standard Library modules:

- tkinter - for building the gui
- webbrowser - to open helpful web links

Overview:

tkinter offers user interfaces including 
windows, buttons, widgets, and text.

Background:

Tk is a cross platform widget toolkit used for building
cross-platform graphical user interface (GUI) native apps that
run unchanged across Windows, Mac OS X, Linux and more.

The Tk toolkit was originally used with Tool Command Language
(Tcl, pronounced “tickle”),
a powerful cross-platform scripting language,
but now we can use Python if we prefer.

Important:

Assign only the function name e.g show_py to a button.
Do not use  parenthesis - we do NOT want to actually call the function until
requested by a user event.

We want to execute the function only after a user event
(e.g. clicking a button).

Add a quit button early.
If you kill a process and it's still out there,
unreponsive, find the process in your OS and kill it / Quit / Force Quit.

For an example of how to force quit an app on Mac, see:
https://support.apple.com/guide/activity-monitor/quit-a-process-actmntr1002/mac
"""

# imports

import tkinter
import webbrowser

# declare variables to hold key information

title = "Build a Desktop App with Python"
is_width_resizeable = True
is_width_resizeable = True

url_python = "https://docs.python.org/"
url_std_library = "https://docs.python.org/3/library/"
url_python_style_guide = "https://peps.python.org/pep-0008/"
url_builtin_functions = "https://docs.python.org/3/library/functions.html"
url_stats = "https://docs.python.org/3/library/statistics.html"
url_web = "https://docs.python.org/3/library/webbrowser.html"
url_tkinter = "https://docs.python.org/3/library/tkinter.html"

icon_check = "\u2714"
icon_bullet = "\u2022"

# define some functions to perform on user events
# Note: Indentation matters!


def show_py():
    webbrowser.open_new(url_python)


def show_std_library():
    webbrowser.open_new(url_std_library)


def show_py_style():
    webbrowser.open_new(url_python_style_guide)


def show_builtin_functions():
    webbrowser.open_new(url_builtin_functions)


def show_stats():
    webbrowser.open_new(url_stats)


def show_web():
    webbrowser.open_new(url_web)


def show_tkinter():
    webbrowser.open_new(url_tkinter)


def quit():
    window.destroy()
    print("Application has been terminated.")


# -------------------------------------------------------------
# Call some functions and execute code!

print()
print("Starting up........................................")
print("Tab through your running apps if it doesn't appear.")
print("Close the app, or hit Control c (together) to close.")
print()

# Create the main window
window = tkinter.Tk()

# set the window title
window.title(title)

# set the window opening size
window.geometry("400x300")
window.resizable(is_width_resizeable, is_width_resizeable)

# add some wigets

tkinter.Label(window, text="hi").pack()

tkinter.Button(window, text="Python Docs", command=show_py).pack()

tkinter.Button(window, text="Python Style Guide", command=show_py_style).pack()

tkinter.Button(
    window, text="Built-In Functions (use anywhere)", command=show_builtin_functions
).pack()

tkinter.Button(
    window,
    text="See what comes free w/the Python Std Library",
    command=show_std_library,
).pack()

tkinter.Button(
    window, text=icon_check + " generate some statistics", command=show_stats
).pack()

tkinter.Button(
    window, text=icon_check + " open a browser          ", command=show_web
).pack()

tkinter.Button(
    window, text=icon_check + " build a GUI (like this) ", command=show_tkinter
).pack()

tkinter.Label(window, text="").pack()

tkinter.Button(window, text="Quit", command=quit).pack()  # quit app


# Start the window and listen continously for user events (like clicking)
window.mainloop()
