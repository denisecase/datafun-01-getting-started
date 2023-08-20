# datafun-01-getting-started

> Get started with Python for data analytics

We assume no prior programming experience and that you want to
get productive as quickly as possible.

## Prerequisites

Your machine must have the following:

1. Python 3.10 or higher
1. VS Code
1. VS Code Extension: Python
1. Git (configured)

Remember:

- **Spacing, Spelling, Capitalization**: With computers, these are critical. Always double-check!

---

## Verify Installations / Update Default Python

In VS Code, open a terminal window (View / Terminal).
If macOS/Linux, change `python` to `python3` in the commands below.

```shell
git --version
python --version
python -m pip install --upgrade pip wheel
```

## Execute Utility Script (Diagnostics)

With your repo folder open in VS Code:

1. Click util_about.py.
1. If VS Code prompts, install the recommended Python extension.
1. Check the Python Interpreter: On the bottom-left status bar, you might see a version of Python indicated (e.g., Python 3.10.x).
1. If not, click on the bottom status bar where it should show the Python version or might say "Select Python Interpreter".
1. From the dropdown, choose your default Python version.
1. In VS Code, open a terminal window (View / Terminal).
1. If macOS/Linux, change `python` to `python3` below.

```shell
python util_about.py
```
---

## Explore & Execute Project Scripts

With your repo folder open in VS Code, start exploring.
Open, read, and run each project script (each file will have a .py extension) in order.
You don't need to fully understand the code yet. 
Instead, try to figure out what each file is doing.

1. Open acquainted.py (or another .py file).
1. Read the comments and code carefully.
1. Execute each script - one at a time.
1. On macOS/Linux, change `python` to `python3` in the commands below.

```shell
python acquainted.py
python basic_expressions.py
python basic_functions.py
python circle_calc.py
python data_io.py
python easy_stats.py
```

Helpful hint: Hit the **up arrow** in the terminal to get the last command. Edit as needed and hit return.

---

## Read and Modify Python Scripts

Read each script in alphabetical order.

1. Each project script has a .py file extension.
1. In the Explorer, click each script to open it in the editor.
1. Read the script.
1. You do NOT need to fully understand the code.
1. Instead, see which parts you can figure out.
1. By the end of the course, these will be very familiar.

Try the TODOs

1. When you see a TODO comment, try to do what it suggests.
1. Treat these as mini puzzles. Creating small syntax errors and fixing them are a great way to learn.
1. Want to see them all? In VS Code, use Edit / Find in Files and search for "TODO".
1. Want an extension to make it more fun? Try [TODO Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree).

Customize these project scripts.

1. Edit the author to your name.
1. Add / remove comments as you like.
1. Try new things!
1. Always run the scripts after making changes. Fix errors as they arise.

---

## Sync to GitHub

If things still work - sync the code back up to GitHub where it's safe.

1. On the VS Code side panel, click the source control icon (look for a blue bubble with an number in it).
1. Hint: Mouse over the icons to see their names.
1. Important! Above the Commit button, it will say "Message". 
1. You MUST include a commit message. 
1. In the commit message input box, type "first TODO".
1. Click the down arrow on the blue "Commit" button to "Commit and Push" to your GitHub repo.

Verify: Open a browser to your GitHub repo and verify the files have appeared. 
In addition to the original files, you should have one or more new files. 
If not, return to VS Code and edit/execute files as needed. 
Then commit and push again.

Common Issue: If your computer hangs because you forgot the commit message, 
just enter your message in the top line of the file it shows in the editor.
Then click the checkmark in the upper right to close that file and save your commit message.
"Sync your changes" to push to GitHub. 

---

## Update README.md

Edit this README.md file as you progress. It uses Markdown, a simple and easy markup language.

- Keep the prerequisites and task headings. 
- Within the task headings, keep only the commands that worked on YOUR machine. 
- Remove unnecessary instructions once you've mastered them.
- Add any additional notes that will help you in the future.

---

## Further Resources

1. Overview [Programming Languages in VS Code](https://code.visualstudio.com/docs/languages/overview)
1. Deep Dive [Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
