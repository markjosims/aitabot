import json
import pandas as pd

praw_data_file = 'praw-data.json'
push_data_file = 'pushshift.json'

praw_keys = ('body', 'title', 'link_flair_text')
push_keys = ('selftext', 'created_utc', 'title', 
             'id', 'link_flair_css_class', 'link_flair_text')

ahole_strs = (
    'cunt', 'ass', 'ars', 'petty', 
    'kinda', 'dick', 'bitch', 'tantrum',
    'hole'
)

ignore_strs = (
    'meta', 'troll', 'long',
    'irrelevant', 'delete', 'best of',
    'update', 'bullshit', 'fake', 'new',
    'advice'
)

out_file = 'reddit_data.csv'

def main():
    flairs = set()
    praw_data = load_json(praw_data_file)
    push_data = load_json(push_data_file)
        
    for x in push_data:
        if not x['selftext'] or x['selftext'] == '[deleted]':
            continue
        elif 'link_flair_css_class' in x and x['link_flair_css_class']:
            flair = x['link_flair_css_class'].lower()
            categorize_flair(flair, x, flairs)
        else:
            assert 'link_flair_text' in x, x.keys()
            flair = x['link_flair_text'].lower()
            categorize_flair(flair, x, flairs)
    for x in praw_data:
        if not x['body'] or x['body'] == '[deleted]':
            continue
        flair = x['link_flair_text'].lower()
        categorize_flair(flair, x, flairs)
    
    df = pd.DataFrame(columns=('title', 'body', 'class'))
    for x in push_data:
        if 'label' not in x or x['label'] is None:
            continue
        df.loc[len(df)] = {
            'title': x['title'],
            'body': x['selftext'],
            'class': x['label']
        }
    for x in praw_data:
        if 'label' not in x or x['label'] is None:
            continue
        df.loc[len(df)] = {
            'title': x['title'],
            'body': x['body'],
            'class': x['label']
        }
        
    df.to_csv(out_file, index=False)
    

def categorize_flair(flair, record, flairs):
    if any(s in flair for s in ahole_strs) and 'no' not in flair:
        record['label'] = True
    elif ('everyone' in flair or 'all' in flair) and 'suck' in flair:
        record['label'] = True
    elif any(s in flair for s in ignore_strs):
        record['label'] = None
    elif ('shit' in flair and 'post' in flair):
        record['label'] = None
    elif 'no' in flair:
        record['label'] = False
    else:
        print(flair)
        assert False
    
    
def load_json(filename):
    with open(filename) as f:
        return json.load(f)

if __name__ == '__main__':
    main()