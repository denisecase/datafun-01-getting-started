# datafun-01-getting-started

> Get started with Python for data analytics

We assume no prior programming experience and that you want to 
get productive as quickly as possible.

## IMPORTANT

When working with computers, commands, and Python:

- **Spelling** is critical
- **Capitalization** is critical
- **Spacing** is critical

Computers are pedantic. When things don't work, check spelling, capitalization, and spacing first.

-----

## On the Web (GitHub / Fork)

### Sign Up for GitHub

GitHub is a code hosting platform that manages a vast number of programming projects. 
Join over 100 million developers and browse over 28 million public repositories.

1. Sign up for a free account with [GitHub](https://github.com/).
1. While logged in, you can create/delete your own repositories (project folders). 
1. You can browse public repos - and if you see something you like, you can grab it and copy it into your account.
1. It's called forking (forking just means copying a repo from one account to another).

### Fork Some Free Code

Fork this repo (copy it into your GitHub account)

1. Open a browser (Chrome is recommended) to the URL of this repo: <https://github.com/denisecase/datafun-01-getting-started>.
1. Look at the URL - note the username is denisecase.
1. Look at all the options available for a repo. 
1. Find and click the **Fork** button up top.
1. Keep the defaults and click 'Create Fork'. 
1. When it finishes, check out your new repo. Note the URL and the username (it should be yours).
1. Explore!  GitHub is pretty fun and easy to use. You got it once you can get it again. You can delete your fork and fork it again. Be courageous and try the + in the upper right, and check out the tabs.

-----

## On Your Machine (Install Git, Python, and VS Code)

Install three important tools on your machine: 
[Git](https://denisecase.github.io/datafun-central/tools/git/index.html), 
[Python](https://denisecase.github.io/datafun-central/languages/python/index.html), and 
[VS Code](https://denisecase.github.io/datafun-central/tools/vs-code/index.html).

### Install Git (for managing code and data files)

1. Installing new tools from the web can be a bit painful, but it's a very valuable, widely-used skill. 
1. Read a bit about Git at <https://git-scm.com/>.
1. DO NOT install GitHub Desktop (we'll use VS Code instead) - see the official instructions for your operating system. 
1. Install Git by clicking the recommended download button for your machine. "Standalone installer 64 bit" is a common choice on Windows.
1. This guide has more information (do NOT install GitHub Desktop): <https://github.com/git-guides/install-git>.
1. We typically verify each installation by checking the version with a simple command.  
1. Open a new PowerShell window (on Windows/Mac) or Terminal (Mac/Linux) and type the following, then hit return/enter.

  ```shell
  git version
  ```

### Configure Git with your name and email. 

1. In the commands below,
1. Change "John Doe" to your name.
1. Change johndoe@example.com to your email (the one you used for GitHub).
1. Open PowerShell or Terminal and configure your global username.
1. Configure your global email address.
1. Verify your global username.
1. Verify your global email. 

  ```shell
  git config --global user.name "John Doe"
  git config --global user.email johndoe@example.com
  git config user.name
  git config user.email
  git config --list
  ```

Git is widely used in industry and academia. Congratulations on getting started with this popular tool! 

### Install Python 3

Download and install Python 3.

1. Read a bit about Python at https://www.python.org/ 
1. Click "Downloads" tab and choose (or accept) the best recommendation for your machine. 
1. Start the executable. Important: Click "Add python.exe to PATH" and continue.
1. Verify your installation by checking the default (usually most recent) Python version. 
1. You may have several versions of Python installed on your machine (3.10, 3.11, even earlier if needed for work).

  ```shell
  python --version
  ```

Install some essential Python packages into the default Python environment.

```shell
python -m pip install --upgrade pip build setuptools wheel 
python -m pip install --upgrade black ruff
python -m pip install --upgrade ipykernel jupyterlab
```

### Install VS Code Editor

Download and install VS Code. 
Python is not the only language we need - we'll use Markdown and SQL too.
VS Code is a great editor for many languages. 

1. Read a bit about VS Code at <https://code.visualstudio.com/>.
1. Click "Download" and follow instructions for your machine.
1. If you need more help, use the official VS Code docs. For example, additional Mac instructions are [here](https://code.visualstudio.com/docs/setup/mac).

-----

## On Your Machine (Get code, Run it, Modify it, Push it Back)

### Get Your Code Down To Your Machine

Clone your new GitHub repo down to the Documents folder on your local machine. 

1. Open VS Code. 
1. From the menu: select View / Command Palette.
1. Start typing Git: Clone and select it from the options. Click GitHub repo.
1. Provide the URL for **your** new GitHub repo. It should have YOUR GitHub username in the URL.
1. When it asks where to put it, select your Documents folder.
1. The first time you clone, you'll be guided through a process to sign into GitHub from VS Code. It's may be a slight challenge, but it's just this once. 
1. Follow the recommendations in VS Code. 
1. When complete, verify you have a new folder in your Documents directory: `Documents/datafun-01-getting-started`
1. You don't need VS Code to clone a repo, but most students prefer it. To clone without VS Code, follow instructions [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

### Execute Python Scripts

With your newly cloned repo folder open in VS Code, we can start exploring Python.
Get VS Code ready for Python. 

1. Click acquainted.py (or any .py file).
1. VS Code will ask if you want to install the recommended extension. 
1. Of course! Check the recommendation (Python by Microsoft). 
1. Consider the stars and downloads. Does it look good?
1. Click Install. 

Execute each script in alphabetical order.

1. Click the Explorer (top left) icon to see your files again. 
1. Click menu View / Terminal to open a terminal window.
1. There are many ways to execute scripts. 
1. Type the following commands to execute each script. 

  ```shell
  python acquainted.py
  python basic_expressions.py
  python basic_functions.py
  python circle_calc.py
  python data_io.py
  python easy_stats.py
  ```

Helpful hint: Hit the **up arrow** in the terminal to get the last command. Edit as needed and hit return.

On some machines, you may need to use `python3` instead of `python`.
On some machines, you may need to use `py` instead of `python`.
If all else fails, try clicking the play button 
in the upper right corner of the editor window or 
right-click on the file and select "Run Python File in Terminal".

Verify things are working - when successful, 
running any of these scripts will create a new log file.  
Log files provide information about your Python environment and can be helpful when things don't work

### Read and Modify Python Scripts

Read each script in alphabetical order.

1. Each Python script has a .py file extension.
1. In the Explorer, click each script to open it in the editor. 
1. Read the script.
1. You do NOT need to fully understand the code. 
1. Instead, just see which parts you can figure out. 
1. By the end of the course, these will be very familiar.

Try the TODOs

1. When you see a TODO comment, try to do what it suggests.
1. Treat these as mini puzzles. Creating small syntax errors and fixing them are a great way to learn. 

Optional: Customize the code

1. Edit the author to your name. 
1. Try some new things. 
1. Your repo is YOURS to do with as you like - we'll share them in class. 

Keep .gitignore and the datafun logger as they are

1. .gitignore is a special file that tells Git what to ignore. Keep it as is.
1. util_datafun_logger.py is our custom logger. Keep it as is.

### Commit Your Changes and Push Back Up to GitHub

After making changes to the code, you'll want to get it back up to the cloud (GitHub) where it's safe. 

1. In VS Code, look for the "Source Control" icon down the left side (mouse over to find the right one). 
1. Click "Source Control" icon. 
1. Enter a short message describing the work you did, e.g., "initial exploration"
1. Note the Commit button has a drop-down - select "Commit and Push" (or "Commit and Sync") to send your changes back up to GitHub.

-----

## Skills Checklist

This README.md file is written in [Markdown](https://denisecase.github.io/datafun-central/languages/markdown/index.html) - a super simple markup langage, widely used in Python notebooks.

Every repo has a README.md. Modify this file as you like. 
Delete parts you don't need anymore. 
Add your own notes in the README.md file. 
Markdown skills are valuable. 

If you like, change the open boxes [ ] below to checked boxes [x] as you gain new skills.

- [ ] Sign up for GitHub
- [ ] Fork a repo into your GitHub
- [ ] Install Git
- [ ] Configure Git
- [ ] Install Python 3
- [ ] Install VS Code 
- [ ] Clone your new GitHub repository/repo down to your machine
- [ ] Explore your local repo in VS Code
- [ ] Execute Python scripts
- [ ] Edit Python scripts
- [ ] Commit changes (with a message!) and push/sync back up to GitHub for sharing

Each time you make changes on your machine, commit and push back up to GitHub. 
When starting it's best to make small changes locally and commit and push often.

## Helpful Resources

Whether working on a home or a project, powerful tools are worth learning. 
Mastering VS Code can provide many happy returns.

1. Scan the article [Programming Languages in VS Code](https://code.visualstudio.com/docs/languages/overview) 
1. Scan the article [Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
