# reddit-fmf-deal-scraper (Work In Progress)

## Description
Script that scrapes /r/frugalmalefashion for new deals and notifies the user of said deals.

### Utilized
* Python3
* PRAW (Python Reddit API Wrapper)

## Prerequisite
Have Python 3.5+ installed to be able to run script

## Getting Started
The user must have PRAW installed on their work environment. After that, the user must create a Reddit application from their Reddit account. Finally, all the user has to do is to clone this repository, input their application's credentials into the authentication.py file and run the fmf-bot.py script.

### Installing PRAW
To install PRAW, type or paste the following code to your terminal
```
$ pip install praw
```
Depending on your system, you may need to use pip3 to install packages for Python 3

If PRAW needs to be updated, run
```
$ pip install --upgrade praw
```

### Register an application on Reddit to get credentials for script
1. Go [here](https://www.reddit.com/prefs/apps/) and click 'create app' at the bottom of the page (after logging in)
2. Give the app a name, label the app as a SCRIPT, give it a description, and set the redirect uri to be http://localhost:8080 

### Clone repository
On your local machine, clone this repository to your desired location by typing or pasting
```
$ git clone https://github.com/KennethNguyen/reddit-fmf-deal-scraper
```

### Adding in user/app credentials
Open the file authentication.py from the cloned repositry. Insert each credential accordingly to what the comments specify on each line within the quotes ('').

To change who you want to send the message to, change the redditor name on line 48 in the file fmf-bot.py

### Running the script
Run the script by typing
```
$ python3 fmf-bot.py
```
After this, you should see a message in your Reddit inbox or there should be a message in whoever you sent it to. 

## Author

Kenneth Nguyen