import praw
from secret import reddit # this is my credentials for the script, hidden from github at the moment
# look into beautiful soup; python library for web scraping

def main():
    # get 5 hot posts from the frugalmalefashion subreddit
    # can be top('hour/day/week/month/year', limit=x) or new(limit=x), etc.
    hot_posts = reddit.subreddit('frugalmalefashion').new(limit=5)
    
    # each post title and code/link of deal is concatenated to user_message string and used as PM to send to user
    user_message = ''
    for post in hot_posts:
        # ignores posts that are stickied
        if not post.stickied:
            # if the post does not have a link in its title
            if post.is_self:
                # double space followed by new line allows PM format to have line breaks for each post title
                user_message += '{post_title} -> {post_link}  \n'.format(
                    post_title = post.title, post_link = post.shortlink)                
            else:
                hyperlink = '[{title}]({link})'
                post_hyperlink = hyperlink.format(
                    link = post.url, title = post.title)
                user_message += '{post_title} -> {post_link}  \n'.format(
                    post_title = post_hyperlink, post_link = post.shortlink)
            
            """ bottom code posts description of post, WIP to regex to extract discount code or link of deal
            if post.selftext != '':
                user_message += ' - {post_description}  {new_line}'.format(
                    post_description = post.selftext, new_line = "\n" * 2)
            else:
                user_message += '  {new_line}'.format(new_line = "\n" * 2)
            """

    # messages user 
    reddit.redditor('SaltGrizzly').message('Hot Post Roundup', user_message)

if __name__ == "__main__":
    main()