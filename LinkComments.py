import json

out_file = 'submissions_w_comments.json'
    
    
# O(don't worry about it)
def main():
    records = []
    s_i, com_i = 0, 0
    while len(records) < 2000 and s_i < 250:
        print("Next submission file...")
        subs = sub_file(s_i)
        for sub in subs:
            sub['comments'] = []
            
            while com_i <= 249:
                #print('Next comments file...')
                coms = c_file(com_i)
                
                has_match = False
                for comment in coms:
                    if comment['link_id'].split(sep='_')[1] == sub['id']:
                        sub['comments'].append(comment['body'])
                        has_match = True
                        print('match')
                if not has_match:
                    pass#com_i_min+=1
                
                com_i+=1
            if sub['comments']:
                records.append(sub)
        com_i=0
        s_i+=1
    
    print(len(records))
    with open(out_file, 'w') as f:
        json.dump(records, f, indent=2)
        
        
def sub_file(i):
    with open(f"submissions/sub{i}.json", "r") as f:
        data = json.load(f)
    return data

def c_file(i):
    with open(f"comments/com{i}.json", "r") as f:
        data = json.load(f)
    return data
            
    
    
if __name__ == '__main__':
    main()