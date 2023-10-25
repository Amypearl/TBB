from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import json
import string

def preprocess_text(text: str):
    lemmatized_tokens = preprocess_text_as_tokens(text)
    return ' '.join(lemmatized_tokens)

def preprocess_text_as_tokens(text: str):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [ token for token in tokens if token not in stopwords.words('english') and token not in string.punctuation and token is not None]
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in filtered_tokens]

def load_dataset():
    file = open('data.json', 'r', encoding='utf-8')
    return json.load(file)

def load_to_json (object, file_name: str):
    json_object = json.dumps(object)
    with open(file_name+'.json', 'w') as outfile:
        outfile.write(json_object)
