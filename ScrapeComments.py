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
    after="1356998400"
    no_data_ct = 0
    while len(data) < 20000 and no_data_ct < 50:
        # get submission objects
        print('Fetching comments...currently have', len(data))
        new_data, after = fetch_comments(after)
        #new_data, before = get_aggs('nta', before)
        if not new_data:
            no_data_ct += 1
        else:
            no_data_ct = 0
            data.extend(new_data)
    print(len(data))
    with open('comments.json', 'w') as f:
        json.dump(data, f, indent=2)

def fetch_comments(after):
    params = {
        'subreddit': 'amitheasshole', 
        'fields': ['body', 'created_utc', 'id', 'link_id'],
        'size': 1000,
        'after': after,
        'author': "Judgement_Bot_AITA"
    }
    response = requests.get("https://api.pushshift.io/reddit/comment/search", params)
    data = response.json()['data']
    if not data:
        print("no more data")
        return None, None
    cutoff = data[-1]['created_utc']
    return data, cutoff

if __name__ == '__main__':
    main()