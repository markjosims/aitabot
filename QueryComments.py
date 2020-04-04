import json
import requests
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
    for i in range(1):    
        for sub in sub_file(i)[:10]:
            ids = get_comment_ids(sub['id'])
            get_comments(ids)

def get_comment_ids(sub_id):
    response = requests.get("https://api.pushshift.io/reddit/submission/comment_ids/"+sub_id)
    data = response.json()['data']
    return data

def get_comments(com_ids):
    params = {
        "ids": com_ids,
        "fields": "body"
    }
    response = requests.get("https://api.pushshift.io/reddit/comment/search", params=params)
    data = response.json()['data']
    return data
    

def sub_file(i):
    with open(f"submissions/sub{i}.json", "r") as f:
        data = json.load(f)
    return data

def write_sub_file(i, data):
    with open(f"submissions/sub{i}.json", "w") as f:
        json.dump(data, f)
        
if __name__ == '__main__':
    main()