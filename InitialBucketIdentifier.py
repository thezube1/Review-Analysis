import pandas as pd
import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk

df = pd.read_csv(r'C:\Users\zubin\Desktop\Python\Sales NSAT Dec 2019 - Mar 2020.csv')

def identify_tags(text):
    words_in_text = word_tokenize(text)
    tagged = nltk.pos_tag(words_in_text)
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

verbs = {}
for i in df.EnglishWhy:
    try:
        text = i
        identified = identify_tags(text)
        identified_list = list_of_identifiers(identified)
        if 'JJ' in identified_list:
            for x in identified_list['JJ']:
                if x in verbs:
                   verbs[x] += 1
                else:
                    verbs[x] = 1
    except TypeError:
        pass

#print(list_of_identifiers())

print({k: v for k, v in sorted(verbs.items(), key=lambda item: item[1])})
