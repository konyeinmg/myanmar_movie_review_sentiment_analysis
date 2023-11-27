import json
import numpy as np

import naivebayes


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

def accuracy(actual_y,pred_y):
    result = 0.0
    for y,y_cat in zip(actual_y,pred_y):
        if y == y_cat:
            result += 1
    accuracy = (result / len(actual_y)) * 100
    return 

def save_loglikelihood(file_url, loglikelihood):
    with open(file_url, 'w') as f:
        for item in loglikelihood:
            string = item + '=>' + str(loglikelihood[item])
            f.write(string+'\n')
        
def save_logprior(file_url, logprior):
    with open(file_url, 'w') as f:
        f.write(str(logprior))
    
def get_loglikelihood(url):
    loglikelihood = {}
    with open(url) as f:
        for line in f:
            seg = line.split('=>')
            loglikelihood[seg[0].strip()] = float(seg[1].strip())
    return loglikelihood

'''
#main method is just to verify the upper methods
def main():
    pos, neg = read_data('data.json')
    #print("Positive reviews : " ,len(pos))
    #print("Negative reviews : ", len(neg))
'''