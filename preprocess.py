import json
import myword

def read_data():
    f = open('data.json')
    data = json.load(f)

    pos_reviews = data['pos']
    neg_reviews = data['neg']

    return pos_reviews, neg_reviews

def segment_words(data):
    myword.count_prob()
    words = myword.words(data)
    return words

def main():
    pos, neg = read_data()
    #print("Positive reviews : " ,len(pos))
    #print("Negative reviews : ", len(neg))
    for item in range(5):
        print(segment_words(pos[item]))


main()