# datafun-01-getting-started

> Get started with Python for data analytics

We assume no prior programming experience and that you want to 
get productive as quickly as possible.

-----

## IMPORTANT

When working with computers, commands, and Python:

- **Spelling** is critical
- **Capitalization** is critical
- **Spacing** is critical

Computers are terribly pedantic. When things don't work, check spelling, capitalization, and spacing first.

-----

## On the Web (GitHub, Fork)

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

1. Installing tools from the web can be a bit painful, but it's a very valuable, widely-used skill. 
1. Read a little bit about Git at <https://git-scm.com/>.
1. DO NOT install GitHub Desktop (we'll use VS Code instead) - see the official instructions for your operating system. 
1. Install Git by clicking the recommended download button for your machine. "Standalone installer 64 bit" is a common choice on Windows.
1. This guide has more information (do NOT install GitHub Desktop): <https://github.com/git-guides/install-git>
1. We typically verify an installation by checking the version by running a simple command.  
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

1. Read a little bit about Python at https://www.python.org/ 
1. Click "Downloads" tab and choose (or accept) the best recommendation for your machine. 
1. Start the executable. Important: Click "Add python.exe to PATH" and continue.
1. Verify your installation by checking the default (usually most recent) Python version. 
1. You may have several versions of Python installed on your machine (3.10, 3.11, even earlier if needed for work).

  ```shell
  python --version
  ```


### Install VS Code Editor

Download and install VS Code.

1. Read a little bit about VS Code at <https://code.visualstudio.com/>.
1. Click "Download" and follow instructions for your machine.
1. If you need more help, use the official VS Code docs. For example, additional Mac instructions are [here](https://code.visualstudio.com/docs/setup/mac).
1. Recommended: If Mac, add VS Code to your Dock.
1. Recommended: If Windows, add VS Code to your Start Menu (Windows).

### Open VS Code to install extensions.

1. Explore the menus. 
1. Verify File / Autosave is checked.
1. Mouse over the icons down the left side. These are key. 
1. Look for an icon with 4 squares.
1. Mouse over it to see the tooltip "Extensions". Click it. 
1. Search for the Extension [Python by Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
1. Install it to your VS Code (it adds a lot of Python-specific functionality.

Whether working on a home or a project, powerful tools are worth learning. Learning the basics of VS Code can provide many happy returns.

1. Scan the article [Programming Languages in VS Code](https://code.visualstudio.com/docs/languages/overview) 
1. Scan the article [Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)

### After Installs, Restart To Update Your Environment

After doing any significant installation, it may help to restart. 

1. After adding extensions, you may be asked to restart VS Code.
1. After installing Git, Python, or tools that affect your environment, you may need to restart your terminal, IDE, and sometimes, your machine before continuing. 
1. Restart as needed to ensure your environments are fully updated.

-----

## On Your Machine (Grab it, Run it, Modify it, Push it Back)

### Get Your Code Down To Your Machine

Clone your new GitHub repo down to the Documents folder on your local machine. 

1. Open VS Code. 
1. From the menu: select View / Command Palette.
1. Start typing Git: Clone and select it from the options. 
1. Provide the URL for **your** new GitHub repo. It will have your username in the URL.
1. When it asks where to put it, select your Documents folder.
1. The first time you clone, you'll be guided through a process to sign into GitHub from VS Code. 
1. Follow the recommendations in VS Code. 
1. When complete, verify you have a new folder in your Documents directory: `Documents/datafun-01-getting-started`
1. You don't need VS Code to clone a repo, but most students like it. To clone without VS Code, follow instructions [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

### Explore and Execute Python Scripts

With your newly cloned repo folder open in VS Code, we can start exploring Python.

1. Click on the about.py file to open it for editing.
1. Can you figure out how to run the Python file? Hint: look for a "play" icon ▶️.
1. Click the run button (arrow) in the upper right to execute/run.
1. Watch what happens in the integrated terminal window. 
1. Click in the terminal window. 
1. Hit the up-arrow key 🔼 on your keyboard to get the last command.
1. Hit Return (or Enter) to rerun the file using the python command. 
1. Verify things are working - when successful, running about.py will create a new about.txt file. 
1. The about.py script provides useful information about your Python environment and can help us help you when things don't work. 
1. Optional: Learn more about executing a Python program in VS Code at [Run Hello World](https://code.visualstudio.com/docs/python/python-tutorial#_run-hello-world).

Open, read, and run each remaining Python script.

1. Each Python script has a .py file extension. 
1. Read and run each script in alphabetical order.
1. You do not need to fully understand the code. 
1. Just try to read the code for now. 
1. Try the suggestions - coding is hands on - treat them as mini puzzles and feel free to try things - the repo is YOURS to do with as you like. 

### Commit Your Changes and Push Back Up to GitHub

After making changes to the code, you'll want to get it back up to the cloud (GitHub) where it's safe. 

1. In VS Code, look for the "Source Control" icon down the left side (mouse over to find the right one). 
1. Click "Source Control" icon. 
1. Enter a short message describing the work you did, e.g., "initial exploration"
1. Note the Commit button has a drop-down - select "Commit and Push" (or "Commit and Sync") to send your changes back up to GitHub.

-----

## Skills Checklist

This file is written in [Markdown](https://denisecase.github.io/datafun-central/languages/markdown/index.html) - a super simple markup langage, widely used in Python notebooks.
If you like, see if you can change the open boxes [ ] to checked boxes [x] below as you demonstrate your new skills.

- [ ] Sign up for GitHub
- [ ] Fork a repo into your GitHub
- [ ] Install (and configure) Git
- [ ] Install Python 3
- [ ] Install VS Code and extensions
- [ ] Clone your new GitHub repo down to your machine
- [ ] Explore your repo in VS Code
- [ ] Execute Python scripts
- [ ] Edit Python scripts
- [ ] Commit changes (with a message!) and push/sync back up to GitHub for sharing
