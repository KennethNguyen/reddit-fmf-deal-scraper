import praw
from secret import my_reddit # this is my credentials for testing the script, hidden from github at the moment
from authentication import reddit # user's credentials
from datetime import datetime, timezone # for converting timezone and date logistics
import time # used for the sleep() function to automate messages in specific intervals

# function to convert the unix time taken from submission.created_utc (which the time a post is created in UNIX Time) to user's local time
def unix_to_local(unix_time):
    # convert the unix time to utc time
    utc_time = datetime.utcfromtimestamp(unix_time)
    # convert the utc time to local time
    local_time = utc_time.replace(tzinfo=timezone.utc).astimezone(tz=None)
    # format the local time to 'day/month/year hour:minute AM/PM' 
    local_time_format = local_time.strftime('%d/%m/%Y %I:%M %p') # https://docs.python.org/2/library/time.html ; look under time.strftime to see more time format options
    return local_time_format

# function creates a hyperlink title to the product deal if the post submission's title is a hyperlink 
def create_hyperlink(post):
    hyperlink = '[{title}]({link})'
    post_hyperlink = hyperlink.format(link = post.url, title = post.title)
    return post_hyperlink    

# function creates a simplified text of a submission post to add to the private message to be sent
def create_message(post):
    message = ''
    # ignores posts that are stickied and expired/out of stock
    if not post.stickied and not post.link_flair_text == "[Expired/OOS] ":
        # double space followed by new line allows private message format to have line breaks for each post title
        message += '{post_time_created} : {post_title} -> {post_link}  \n'.format(
            post_time_created = unix_to_local(post.created_utc), 
            post_title = post.title if post.is_self else create_hyperlink(post), # post.is_self is when the post does not have a hyperlink title
            post_link = post.shortlink # link to the original post
        )
    return message    

def main():
    # get 5 hot posts from the frugalmalefashion subreddit
    # can be top('hour/day/week/month/year', limit=x) or hot(limit=x) or new(limit=x), etc.
    hot_posts = my_reddit.subreddit('frugalmalefashion').hot(limit=5)

    # each post title and code/link of deal is concatenated to user_message string and used as PM to send to user
    user_message = ''
    for post in hot_posts:
        user_message += create_message(post)

    # messages user 
    my_reddit.redditor('SaltGrizzly').message('Hot Post Roundup', user_message)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(6000) # currently automate script to send new message every hour after execution of script