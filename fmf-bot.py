import praw
from secret import reddit

def main():
    # get 5 hot posts from the frugalmalefashion subreddit
    # can be top('hour/day/week/month/year', limit=x) or new(limit=x), etc.
    hot_posts = reddit.subreddit('frugalmalefashion').hot(limit=5)
    
    # each post title is concatenated to user_message string and used as PM to send to user
    user_message = ''
    for post in hot_posts:
        print(post.title)
        user_message += post.title + '  \n' # double space followed by new line allows PM format to have line breaks for each post title

    # messages user 
    reddit.redditor('SaltGrizzly').message('Hot Post Roundup', user_message)

if __name__ == "__main__":
    main()