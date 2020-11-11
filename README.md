# A comprehensive guide on how to install VSCode, Git, Python and start your Django server. 

## The Set Up 

#### Install VSCode
Mac: https://code.visualstudio.com/docs/setup/mac

Windows: https://code.visualstudio.com/docs/setup/windows

#### Install Python 
https://www.python.org/downloads/

The best way to install python is to download python from the python.org website! 

To make sure you have installed python correctly: open up your `terminal` and type `python --version`. If you have it successfully installed it should return with a version number! 

#### Install Git 
Website: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git/

Installing on macOS
> There are several ways to install Git on a Mac. The easiest is probably to install the Xcode Command Line Tools. On Mavericks (10.9) or above you can do this simply by trying to > run git from the Terminal the very first time.

> $ git --version
> If you don’t have it installed already, it will prompt you to install it.

Installing on Windows 
>Another easy way to get Git installed is by installing GitHub Desktop. The installer includes a command line version of Git as well as the GUI. It also works well with PowerShell, and sets up solid credential caching and sane CRLF settings. We’ll learn more about those things a little later, but suffice it to say they’re things you want. You can download this from the GitHub Desktop website.

#### Make a github account
If you have not made a github account, please do so! You can sign up for one here: https://github.com/

#### Set your commit email in github / git 
Now that you have a github account and are looking to make contributions you have to make sure your email address is correctly linked!
https://docs.github.com/en/free-pro-team@latest/github/setting-up-and-managing-your-github-user-account/setting-your-commit-email-address

#### Make a github folder in your computer file system 
Not necessarily needed as you can have a git repository in any folder, however just for organizational sake I would recommend making one! I have my github folder in my documents folder.


## Getting your environment ready 

#### Fork this django-tutorial repo in github

How to fork a repo:
https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo

#### In your terminal or command prompt, navigate to the github folder you've created
If you made your github folder in your documents folder like I did: 
```
cd documents
cd github
```

#### Clone the repository that you have forked

`git clone repo-url`

To make sure the git clone worked you can navigate to your forked folder either through finder or by typing 

```
ls
```

in your terminal and you should see an output of the folder you pulled.

## Running the application 

#### Getting the environment ready & installing the requirements needed.

Open up VSCode. Click open folder. Navigate to your django-tutorial folder and click `open`. 

In VSCode, open the `terminal`.

in the terminal run: 
```
pip install -r requirements.txt
```

#### Run your Django application 

In your VSCode `terminal`

`cd django_tutorial` to navigate to the django_tutorial folder. 

In the `django_tutorial` folder run:
```
python manage.py migrate
```
and then run 
```
python manage.py runserver
```
