# datafun-01-getting-started

> An opinionated way to get started with Python for data analytics

We assume no prior programming experience and that you want to 
get productive as quickly as possible.

We set up a professional environment using professional tools from the start.

## IMPORTANT

- Spelling matters
- Capitalization matters
- Spacing matters

Computers are pedantic - if/when things don't work, check spelling, capitalization, and spacing first.

-----

## On the Web: Sign Up for GitHub (free)

Sign up for a free account with [GitHub](https://github.com/), 
a code hosting platform that manages a vast number of programming projects. 
Join over 100 million developers and browse over 28 million public repositories.

-----

## On Your Machine: Install Git, Python, VS Code

Install some tools on your machine. 

### Install Git (for managing code and data files)

DO NOT install GitHub Desktop (we'll use VS Code instead) and go down to the instructions for your operating system. 

1. Read about Git at https://git-scm.com/
2. Install Git by clicking the recommended download button for your machine. "Standalone installer 64 bit" is a common choice on Windows.
3. This guide has more information (do NOT install GitHub Desktop): https://github.com/git-guides/install-git

Verify your installation. 

1. Find Git on your machine.
2. Check the version as described below.

Open a new Terminal (macOS) or PowerShell (Windows/macOS) and type the following, then hit return/enter:

```
git version
```

### Configure Git with your email and username

Configure Git so you have the ability to commit code.

In the commands below:

- Change "John Doe" to your name.
- Change johndoe@example.com to your email (the one you used for GitHub).

Open Git Bash or Terminal and configure your global username and email. 


```shell
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```

These may be shown with a $. 
If you see that, don't type the $.  
The dollar sign is used to indicate the type of terminal used to run the command. 
In this case, Git Bash. 

```shell
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```

Verify your configuration.

1. Verify your global username
2. Verify your global email
3. See all the git config entries

```
git config user.name
git config user.email
git config --list
```

Git is widely used in industry and academia. Congratulations on getting started! 

### Install Python 3

Download and install Python 3.

1. Read about Python at https://www.python.org/ 
2. Click "Downloads" tab and choose (or accept) the best recommendation for your machine. 
3. Start the executable. 
4. Important: Click "Add python.exe to PATH" and continue.

Verify your installation. 

1. Find it on your machine.
2. Check the default Python version. You may have several. More on this later.

```
python --version
```

### Install VS Code Editor

Download and install VS Code and add helpful extensions.

1. Read about VS Code at https://code.visualstudio.com/ 
2. Click "Download" button and follow instructions for your machine.

If you need more help, use the official VS Code docs. 
For example, additional Mac instructions are [here](https://code.visualstudio.com/docs/setup/mac).

Recommended

- Add VS Code to your Dock (macOS)
- Add VS Code to your Start Menu (Windows).

Open VS Code

- Explore the menus. 
- Verify File / Autosave is checked.
- Mouse over the icons down the left side. These are key. 
- Look for an icon with 4 squares.
- Mouse over it to see the tooltip "Extensions". Click it. 
- Search for the Extension [Python by Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- Install it to your VS Code (it adds a lot of Python-specific functionality.

Coding With VS Code

1. Scan the article [Programming Languages in VS Code](https://code.visualstudio.com/docs/languages/overview) 
2. Scan the article [Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)

### After Installs, Restart To Update Your Environment

After doing any significant installation, restart. 

After adding extensions, you may be asked to restart VS Code.

After installing Git, Python, or tools that affect your environment, 
you may need to restart your terminal, IDE, and sometimes, your machine before continuing. 

Ensure your environments are fully updated.

-----

## On the Web: Fork this Repo (Copy it into Your GitHub)

Now that your machine is ready - let's go back to the web to get some code. 

First, fork this repo (copy it into your GitHub account). 

1. Open your browser to <https://github.com/denisecase/datafun-01-getting-started>.
1. Look at the URL and the web page - note the account is denisecase.
1. Look at all the options available for a repo. 
1. Find and click the 'Fork' button at the top.
1. Keep the defaults and click 'Create Fork'. 
1. When it finishes, look at the repo - note the account (it should be yours).

Forking is just a term for copying a repo from one account to another.

## Clone Your Repo (down to your machine)

Now clone your new GitHub repo down to the Documents folder on your local machine. 

1. Open VS Code. 
1. From the menu: select View / Command Palette.
1. Start typing Git: Clone and select it.
1. Provide the URL of **your** new GitHub repo.
1. When it asks where to put it, select your Documents folder.

Note: The first time you do this, you'll be guided through a process to sign into GitHub from VS Code. 

You can read more about cloning - and clone your repo without VS Code by following the instructions [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

When complete, verify you have a new folder in your Documents directory:

`Documents/datafun-01-getting-started`

## On Your Machine: Explore Repo in VS Code

Explore your new project repo/folder/directory in VS Code. 

## On Your Machine: Execute Python Scripts

1. Click on the about.py file to open it for editing.
1. Can you figure out how to run the Python file? Hint: look for a "play" icon ▶️.
1. Click the run button (arrow) in the upper right to execute/run.
1. Watch what happens in the integrated terminal window. 
1. Click in the terminal window. 
1. Hit the up-arrow key 🔼 on your keyboard to get the last command.
1. Hit Return (or Enter) to rerun the file using the python command. 
1. If successful, you should get a new about.txt file. 

For more information about options for executing a Python program in VS Code, see [Run Hello World](https://code.visualstudio.com/docs/python/python-tutorial#_run-hello-world).

The about module provides a lot of useful information about your Python environment. 
Review these paths carefully - it tells a lot about your Python installation and environment. 

Open, read, and run each remaining Python script (each file will have a .py extension) in order.
You don't need to fully understand the code yet. 

## Edit Markdown

Next, edit this Markdown file to record how things went.

1. In the checklist below, mark the tasks completed that you were able to complete successfully. 
1. If any could not be completed, leave them as they are.  
1. Try to complete all but the last one.

## Commit Changes and Push to GitHub

Now it's time to get the local work you did (on your machine), 
back up to the cloud repo in GitHub.

With git, we first git add any new files, 
then git commit them to source control (with a message), 
then git push them up to GitHub. 

## Checklist

Change the open boxes [ ] below to checked boxes [x] as you complete the tasks.

- [ ] Sign up for GitHub
- [ ] Install (and configure) Git
- [ ] Install Python 3 (or other)
- [ ] Install VS Code and extensions
- [ ] Fork a repo into your GitHub
- [ ] Clone your new GitHub repo down to your machine
- [ ] Explore your repo in VS Code
- [ ] Execute a Python script.
- [ ] Edit a Markdown file
- [ ] Commit changes (with a message!) and push/sync to GitHub

Finally - after your initial commit and push, you can check the last box. 
Check the box, commit your changes (with a message!), and push/sync again. 

