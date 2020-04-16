import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

score = sid.polarity_scores('this is sentence is the shit')
print(score)

from textblob import TextBlob
score = TextBlob('this is the best sentence ever').sentiment
print(score)

import flair
flair_sentiment = flair.models.TextClassifier.load('en-sentiment')
s = flair.data.Sentence('this is the best sentence ever')
flair_sentiment.predict(s)
total_sentiment = s.labels
print(total_sentiment)