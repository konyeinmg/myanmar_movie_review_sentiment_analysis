import json
import re
from string import punctuation

import myword

emotions = [
    ":)",       # Happy or friendly
    ":(",       # Sadness or disappointment
    ":D",       # Extreme happiness or joy
    ":/",       # Uncertainty or confusion
    ":O",       # Surprise or shock
    ":P",       # Playful or cheeky
    ":|",       # Neutrality or indifference
    ";)",       # Humor or playful wink
    ":'(",      # Intense sadness or crying
    "<3",       # Love or affection
    "xD"        #laugh
]

def read_data():
    f = open('data.json')
    data = json.load(f)

    pos_reviews = data['pos']
    neg_reviews = data['neg']

    return pos_reviews, neg_reviews

def sentence_cleaning(line):
    remove_eng = ''.join(re.findall("[^A-Za-z0-9]", line))
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
        words = myWord(filter_text)
        
        #emotions check
        for emotion in emotions:
            if emotion in item:
                words += [emotion]

        result += [words]

    return result

#main method is just to verify the upper methods
def main():
    pos, neg = read_data()
    #print("Positive reviews : " ,len(pos))
    #print("Negative reviews : ", len(neg))
    result = segment_words(pos[:10])
    print(result)


main()