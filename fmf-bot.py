import praw
from secret import my_reddit # this is my credentials for testing the script, hidden from github at the moment
from authentication import reddit # user's credentials
from datetime import datetime, timezone # for converting timezone and date logistics
import time # used for the sleep() function to automate messages in specific intervals
# look into beautiful soup; python library for web scraping

# function to convert the unix time taken from submission.created_utc (which the time a post is created in UNIX Time) to user's local time
def unix_to_local(unix_time):
    # convert the unix time to utc time
    utc_time = datetime.utcfromtimestamp(unix_time)
    # convert the utc time to local time
    local_time = utc_time.replace(tzinfo=timezone.utc).astimezone(tz=None)
    # format the local time to 'day/month/year hour:minute AM/PM' 
    local_time_format = local_time.strftime('%d/%m/%Y %I:%M %p') # https://docs.python.org/2/library/time.html ; look under time.strftime to see more time format options
    return local_time_format

def main():
    # get 5 hot posts from the frugalmalefashion subreddit
    # can be top('hour/day/week/month/year', limit=x) or new(limit=x), etc.
    hot_posts = my_reddit.subreddit('frugalmalefashion').new(limit=5)
    
    # each post title and code/link of deal is concatenated to user_message string and used as PM to send to user
    user_message = ''
    for post in hot_posts:
        # ignores posts that are stickied
        if not post.stickied:
            # if the post does not have a link in its title
            if post.is_self:
                # double space followed by new line allows private message format to have line breaks for each post title
                user_message += '{post_time_created} : {post_title} -> {post_link}  \n'.format(
                    post_time_created = unix_to_local(post.created_utc) , post_title = post.title, post_link = post.shortlink)                
            else:
                hyperlink = '[{title}]({link})'
                post_hyperlink = hyperlink.format(
                    link = post.url, title = post.title)
                user_message += '{post_time_created} : {post_title} -> {post_link}  \n'.format(
                    post_time_created = unix_to_local(post.created_utc), post_title = post_hyperlink, post_link = post.shortlink)
            
            """ bottom code posts description of post, WIP to regex to extract discount code or link of deal
            if post.selftext != '':
                user_message += ' - {post_description}  {new_line}'.format(
                    post_description = post.selftext, new_line = "\n" * 2)
            else:
                user_message += '  {new_line}'.format(new_line = "\n" * 2)
            """

    # messages user 
    my_reddit.redditor('SaltGrizzly').message('Hot Post Roundup', user_message)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(6000) # automate script to send new message every hour after execution of script