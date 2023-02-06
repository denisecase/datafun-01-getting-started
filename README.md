# datafun-01-getting-started

> An opinionated way to get started with Python for data analytics

Set yourself up for productivity and collaboration.

We assume no prior programming experience and that you want to 
get productive as quickly as possible.

## Task 1. Sign Up for GitHub (free)

Sign up for a free account with [GitHub](https://github.com/), 
a code hosting platform that manages a vast number of programming projects. 

## Task 2. Install Git (for managing code and data files)

Install - and configure - your Git installation using this guide: <https://github.com/git-guides/install-git>.

Except do NOT install GitHub Desktop (we'll use VS Code for git) and go down to the instructions for your operating system. 

Verify installation by checking the version. 
Open a new Terminal (macOS) or PowerShell (Windows/macOS) and type the following, then hit return/enter:

`git version`

Configure git with your email and username before continuing.

## Task 3. Install Miniconda3 (to get Python and Conda)

If you've installed the full Anaconda as recommended in the textbook, that's perfect - don't also install Miniconda3. 
Anaconda is larger and has more Python modules built-in. 

Install Python 3 using the **Miniconda3** distribution by [following the instructions](https://docs.conda.io/en/latest/miniconda.html).
Installations depend on  operating system and machine (most will be 64-bit). Note:

_"On Windows, macOS, and Linux, it is best to install Miniconda **for the local user**, which does not require administrator permissions and is the most robust type of installation."._ 

**Miniconda3** includes Python and **conda** (an important tool for managing Python packages and environments). 

Once installation is complete, run the following command to initialize the conda environment:

`conda init`

Close and reopen your terminal window or command prompt, 
and you should now be able to use the conda command to manage your Python environment.
Open a new Terminal (macOS) or open Anaconda Prompt (Windows) and type the following. 
Hit return or enter after each line.

```
conda update conda
python --version
conda list
```


## Task 4. Install VS Code (to help with writing code)

Install the **VS Code** editor from here: <https://code.visualstudio.com/download>.

If you need more help, use the official VS Code docs. 
For example, additional Mac instructions are [here](https://code.visualstudio.com/docs/setup/mac).

- Add VS Code to your Dock (macOS)
- Add VS Code to your Start Menu (Windows).
- Open VS Code. 
- Explore the menus. 
- Mouse over the icons down the left side. These are key. 
- Verify File / Autosave is checked.

## Task 5. Install VS Code Extension: Python

After VS Code installs, install the VS Code Python extension from here: <https://marketplace.visualstudio.com/items?itemName=ms-python.python>.

- If you have issues, click the link that says "Trouble Installing?"
- It will show you how to add extensions from within VS Code.

Once you install the extension, it'll ask if you want to get started with Jupyter Notebooks.
Ignore this for now - close that tab in VS Code.

## Task 6. Install VS Code Extension: GitHub Repositories

In VS Code, look at the icons down the left. Look for 4 squares.
Mouse over it to see the tooltip "Extensions". Click it. 

On the top of the primary left side panel, you'll see the installed extensions. 

If **GitHub Repositories** is not installed, find it in the recommended list of extensions below, do a web search, or find it here: <https://marketplace.visualstudio.com/items?itemName=github.remotehub>

✅ Leveraging an IDE is an important skill and can increase productivity significantly.

## After Installs, Restart 

_Recommendation: After doing any significant installation, it may help to restart. After adding extensions, you may restart VS Code, after Git, Python, or tools that affect your environment, you may need to restart your terminal, IDE, and sometimes, your machine before continuing. Ensure your environments are fully updated._

## Task 7. Fork (Copy) this Repo (to Your GitHub)

Now that your machine is ready - let's get some code. 

First, fork (copy) this repo into **your** GitHub account. 

1. Open your browser to <https://github.com/denisecase/datafun-01-getting-started>.
1. Look at the URL and the web page - note the account is denisecase.
1. Look at all the options available for a repo. 
1. Find and click the 'Fork' button at the top.
1. Keep the defaults and click 'Create Fork'. 
1. When it finishes, look at the repo - note the account (it should be yours).

Forking is just a term for copying a repo from one account to another.

## Task 8. Clone Your Repo (down to your machine)

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

## Task 9. Explore Repo in VS Code (on your machine)

Explore your new project repo/folder/directory in VS Code. 

## Task 10. Execute Python Scripts

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


## Task 11. Check the Boxes

Next, edit this Markdown file to record how things went.

1. In the checklist below, mark the tasks completed that you were able to complete successfully. 
1. If any could not be completed, leave them as they are.  
1. Try to complete all but the last one.

## Task 12. Commit Changes and Push to GitHub

Now it's time to get the local work you did (on your machine), 
back up to the cloud repo in GitHub.

With git, we first git add any new files, 
then git commit them to source control (with a message), 
then git push them up to GitHub. 

## Checklist

Change the open boxes [ ] below to checked boxes [x] as you complete the tasks.

- [ ] Task 1. Sign up for GitHub
- [ ] Task 2. Install (and configure) Git
- [ ] Task 3. Install Miniconda3 (or other)
- [ ] Task 4. Install VS Code
- [ ] Task 5. Install VS Code Extension: Python
- [ ] Task 6. Install VS Code Extension: GitHub Repositories
- [ ] Task 7. Fork this repo into your account
- [ ] Task 8. Clone your new GitHub repo down
- [ ] Task 9. Explore the repo in VS Code
- [ ] Task 10. Execute a Python script.
- [ ] Task 11. Check the boxes (edit a Markdown file)
- [ ] Task 12. Commit changes (with a message!) and push to GitHub

Finally - after your initial commit and push, you can check the last box. 
Check the box, commit your changes (with a message!), and push/sync again. 

