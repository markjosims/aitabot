import json

sub_file = "submissions.json"
c_file = "comments.json"

def main():
    with open(sub_file, 'r') as f:
        submissions = json.load(f)
    partition(submissions, 'submissions/sub')
    
    with open(c_file, 'r') as f:
        comments = json.load(f)
    partition(comments, 'comments/com')
    

def partition(data, filename):
    i=0
    while i < len(data):
        this_part = data[i:i+1000]
        part_filename = filename + str(i//1000) + '.json'
        with open(part_filename, 'w') as f:
            json.dump(this_part, f)
        i+=1000
        
if __name__ == '__main__':
    main()