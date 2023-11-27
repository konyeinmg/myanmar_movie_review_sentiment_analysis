import json
import numpy as np


def read_data(url):
    f = open(url)
    data = json.load(f)

    pos_reviews = data['pos']
    neg_reviews = data['neg']

    return pos_reviews, neg_reviews

def train_test_split(train_percent, pos, neg):
    train_pos_len = int(len(pos) * train_percent)
    train_neg_len = int(len(neg) * train_percent)

    train_pos = pos[:train_pos_len]
    train_neg = neg[:train_neg_len]
    test_pos = pos[train_pos_len:]
    test_neg = neg[train_neg_len:]

    train_x = train_pos + train_neg
    test_x = test_pos + test_neg

    train_y = np.append(np.ones(len(train_pos)), np.zeros(len(train_neg)))
    test_y = np.append(np.ones(len(test_pos)), np.zeros(len(test_neg)))

    return train_x, test_x, train_y, test_y

'''
#main method is just to verify the upper methods
def main():
    pos, neg = read_data('data.json')
    #print("Positive reviews : " ,len(pos))
    #print("Negative reviews : ", len(neg))
'''