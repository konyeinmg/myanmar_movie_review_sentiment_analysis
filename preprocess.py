import json
import re
from string import punctuation

import myword

def read_data():
    f = open('data.json')
    data = json.load(f)

    pos_reviews = data['pos']
    neg_reviews = data['neg']

    return pos_reviews, neg_reviews

def sentence_cleaning(line):
    remove_eng = ''.join(re.findall("[^a-z0-9]", line))
    filter_text = ''

    for c in remove_eng:
        if c not in punctuation:
            filter_text += c
    
    return filter_text

def myWord(line):
    return myword.words(line)

def segment_words(data):
    myword.count_prob()
    result = []
    for item in data:
        filter_text = sentence_cleaning(item)
        result += [myWord(filter_text)]
    return result

def main():
    pos, neg = read_data()
    #print("Positive reviews : " ,len(pos))
    #print("Negative reviews : ", len(neg))
    result = segment_words(neg[-5:])
    print(result)


main()