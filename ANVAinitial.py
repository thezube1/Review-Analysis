import string
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk import ngrams
df = pd.read_csv(r'C:\Users\zubin\Desktop\Python\Sales NSAT Dec 2019 - Mar 2020.csv')
#df = df.dropna()

def punctuation_clean(sentance):
    c = string.punctuation
    no_punct_string = ''
    for char in sentance:
        if char not in c:
            no_punct_string += char.lower()
    return no_punct_string

lemmatizer = WordNetLemmatizer()

def lemmatize(list_of_words):
    for i in range(len(list_of_words)):
        list_of_words[i] = lemmatizer.lemmatize(list_of_words[i])
    
    return list_of_words

ps = PorterStemmer()

def stemmer(list_of_words):
    for i in range(len(list_of_words)):
        list_of_words[i] = ps.stem(list_of_words[i])
    
    return list_of_words

stop_words = set(stopwords.words('english'))




#text = df.EnglishWhy[0]
#n = 4
#trigrams = ngrams(text.split(), n)

#for grams in trigrams:
#  print(grams)

n = 2
results = {}
for text in df.EnglishWhy:
    cleaned = punctuation_clean(text)
    text_tokenized = word_tokenize(cleaned)
    stopped_words = [w for w in text_tokenized if not w in stop_words]
    v = ' '.join(stopped_words)
    try:
        trigrams_result = ngrams(v.split(), n)
        for grams in trigrams_result:
            if grams in results:
                results[grams] += 1
            else:
                results[grams] = 1
    except AttributeError:
        pass
    except TypeError:
        pass

#print({k: v for k, v in sorted(results.items(), key=lambda item: item[1])})
         
#cleaned = punctuation_clean(text)
#text_tokenized = word_tokenize(cleaned)
#stopped_words = [w for w in text_tokenized if not w in stop_words]
#v = ' '.join(stopped_words)
#text_tagged = nltk.pos_tag(stopped_words)

#print(v)