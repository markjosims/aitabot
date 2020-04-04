import praw
import json


params = {
    "client_id": "wUZdJo9oKd1yzQ",
    "client_secret": "PAIVLtVOoaS_BwnwJPnvkttjGQI",
    "user_agent": "AmITheAsshole-Scraper"
}

def main():
    reddit = praw.Reddit(**params)
    amita = reddit.subreddit('AmITheAsshole')
    data = []

    for post in amita.top(limit=1000):
        if not post.link_flair_text:
            continue
        this_post = {
            'body': post.selftext,
            'title': post.title,
            'link_flair_text': post.link_flair_text
        }
        data.append(this_post)
    with open('praw-data.json', 'w') as f:
        json.dump(data, f, indent=2)
    print(len(data))
    

if __name__ == '__main__':
    main()