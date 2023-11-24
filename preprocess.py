import json

def read_data():
    f = open('data.json')
    data = json.load(f)

    pos_reviews = data['pos']
    neg_reviews = data['neg']

    return pos_reviews, neg_reviews

def main():
    pos, neg = read_data()
    print("Positive reviews : " ,len(pos))
    print("Negative reviews : ", len(neg))

main()