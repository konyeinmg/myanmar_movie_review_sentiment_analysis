import json
import re
from string import punctuation
from stopwords import stopwords2

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


def sentence_cleaning(line):
    remove_eng = ''.join(re.findall("[^A-Za-z0-9]", line)) #remove all english characters
    filter_text = ''

    for c in remove_eng:
        if c not in punctuation: #remove all punctuation characters
            filter_text += c
    
    return filter_text

def myWord(line):
    return myword.words(line)

#check emotion with original text and append to last of word list
def add_emotions(clean_text, original):
    for emotion in emotions:
        if emotion in original:
            clean_text += [emotion]
    
    return clean_text

#remove myanmar stopwords
def remove_stopwords(data):
    return [item for item in data if item not in stopwords2]

def segment_words(data):
    #myword.count_prob()
    filter_text = sentence_cleaning(data)
    words = myWord(filter_text)
        
    #check emotions
    words = add_emotions(words, data)
        
    #remove stopwords
    words = remove_stopwords(words)

    return words

'''
#main method is just to verify the upper methods
def main():
    for i in range(3):
        print(segment_words(neg[i]))


main()
'''
