# uses pushshift.io

import requests
import json
from time import time

# decorator
def time_exec(f):
    def g(*args, **kwargs):
        start = time()
        f(*args, **kwargs)
        end = time()
        print(str(f), end-start)
    return g

@time_exec
def main():
    data = []
    before="1356998400"
    no_data = 0
    while len(data) < 20000 and no_data < 20:
        # get submission objects
        print('Fetching submissions...currently have', len(data))
        new_data, before = fetch_submissions(before)
        #new_data, before = get_aggs('nta', before)
        if not new_data:
            no_data += 1
        else:
            data.extend(new_data)
            no_data = 0
    print(len(data))
    with open('submissions.json', 'w') as f:
        json.dump(data, f, indent=2)

def fetch_submissions(before):
    params = {
        'subreddit': 'amitheasshole', 
        'fields': ['title' , 'selftext', 'created_utc', 'id', 'link_flair_text', 'link_flair_css_class'],
        'size': 1000,
        'after': before,
        'num_comments': '>10',
    }
    response = requests.get("https://api.pushshift.io/reddit/submission/search", params)
    data = response.json()['data']
    if not data:
        return None, before
    cutoff = data[-1]['created_utc']
    data = [d for d in data if 'link_flair_text' in d or 'link_flair_css_class' in d]
    return data, cutoff

if __name__ == '__main__':
    main()