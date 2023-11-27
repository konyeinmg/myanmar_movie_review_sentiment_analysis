import json

def read_data(url):
    f = open(url)
    data = json.load(f)

    pos_reviews = data['pos']
    neg_reviews = data['neg']

    return pos_reviews, neg_reviews

'''
#main method is just to verify the upper methods
def main():
    pos, neg = read_data('data.json')
    #print("Positive reviews : " ,len(pos))
    #print("Negative reviews : ", len(neg))
'''