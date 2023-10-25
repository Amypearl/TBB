import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from util import preprocess_text, load_dataset, load_to_json


dataset = load_dataset()

tweets = [tweet['tweet_text'] for tweet in dataset.values() if 'tweet_text' in tweet and tweet.get('tweet_text') is not None]

analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text: str):
    scores = analyzer.polarity_scores(text)
    if scores['pos'] >= 0.5:
        return 1
    elif scores['neu'] >= 0.5:
        return 1
    else:
        return 0

def analyze(text):
    preprocesed_text = preprocess_text(text)
    return get_sentiment(preprocesed_text)

dataset_as_list= list(dataset.values())


data = {
    'total': len(dataset_as_list),
    'positive': 0,
    'negative': 0
}

for tweet in tweets:
    sentiments_results = analyze(tweet)
    if sentiments_results > 0:
        data['positive']= data ['positive'] + 1
    else: 
        data ['negative'] = data ['negative'] + 1


print (data)
load_to_json (data, 'sentiment_analysis')


