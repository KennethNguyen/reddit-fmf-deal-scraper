from secret import reddit

# get 5 hot posts from the frugalmalefashion subreddit
hot_posts = reddit.subreddit('frugalmalefashion').hot(limit=5)
for post in hot_posts:
    print(post.title)