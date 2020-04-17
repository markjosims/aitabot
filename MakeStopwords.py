from nltk.corpus import stopwords
import json

def main():
    stop_words = stopwords.words('english')
    stop_words_obj = {
        "stop_words": stop_words,
        "doc_str": ""
    }
    with open('stopwords.json', 'w') as f:
        json.dump(stop_words_obj, f, indent=2)


if __name__ == '__main__':
    main()