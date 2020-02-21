import praw

# authenticating script usage using password flow

reddit = praw.Reddit(
    client_id='', # app unique id found under app's name
    client_secret='', # app's secret client string found next to 'secret'
    password='', # user's reddit password login
    username='', # user's reddit username login
    user_agent='FMFDeals Bot'
)