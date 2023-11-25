import pandas as pd
import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords
import string

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

df = pd.read_csv(r'C:\Users\zubin\Desktop\Python\Sales NSAT Dec 2019 - Mar 2020.csv')

def identify_tags(list_of_words):
    tagged = nltk.pos_tag(list_of_words)
    return tagged

def num_of_identifiers(tags):
    quantities = {}
    for i in range(len(tags)):
        lists = tags[i]
        if lists[1] not in quantities:
            quantities[lists[1]] = 1
        else:
            quantities[lists[1]] += 1

    return quantities

def list_of_identifiers(tags):
    parts = {}
    for i in range(len(tags)):
        lists = tags[i]
        if lists[1] not in parts:
            parts[lists[1]] = [lists[0]]
        else:
            parts[lists[1]].append(lists[0])

    return parts

def punctuation_clean(sentance):
    c = string.punctuation
    no_punct_string = ''
    for char in sentance:
        if char not in c:
            no_punct_string += char.lower()
    return no_punct_string

def lemmatize(list_of_words):
    for i in range(len(list_of_words)):
        list_of_words[i] = lemmatizer.lemmatize(list_of_words[i])
    
    return list_of_words

def stemmer(list_of_words):
    for i in range(len(list_of_words)):
        list_of_words[i] = ps.stem(list_of_words[i])
    
    return list_of_words


example_test = df.EnglishWhy[0]
no_char = punctuation_clean(example_test)
example_tokenized = word_tokenize(no_char)


stemmed = stemmer(example_tokenized)
lemmatized = lemmatize(example_tokenized)

verbs = {}
for i in df.EnglishWhy:
    try:
        text = i
        text_cleaned = punctuation_clean(text)
        text_tokenized = word_tokenize(text_cleaned)
        stopped_words = [w for w in text_tokenized if not w in stop_words]
        text_stemmed = stemmer(stopped_words)
        text_lemmatized = lemmatize(text_stemmed)
        identified = list_of_identifiers(identify_tags(text_lemmatized))
        if 'NN' in identified:
            for x in identified['NN']:
                if x in verbs:
                   verbs[x] += 1
                else:
                    verbs[x] = 1
    except TypeError:
        pass

print({k: v for k, v in sorted(verbs.items(), key=lambda item: item[1])})
