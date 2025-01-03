import json
import numpy as np

import naivebayes


def read_data(url):
    f = open(url)
    data = json.load(f)

    pos_reviews = data['pos']
    neg_reviews = data['neg']

    return pos_reviews, neg_reviews

#split data with train percentage
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

#calculate precision and recall
def precision_recall(actual_y, pred_y):
    TP = FP = FN = 0

    for i in range(len(actual_y)):
        if actual_y[i] == 1 and pred_y[i] == 1:
            TP += 1
        elif actual_y[i] == 1 and pred_y[i] == 0:
            FN += 1
        elif actual_y[i] == 0 and pred_y[i] == 1:
            FP += 1
    
    # Calculate Precision
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0.0

    # Calculate Recall
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0.0

    return precision,recall


#calculate accuracy
def accuracy(actual_y,pred_y):
    result = 0.0
    for y,y_cat in zip(actual_y,pred_y):
        if y == y_cat:
            result += 1
    accuracy = (result / len(actual_y)) * 100
    return accuracy

#save model loglikelihoods
def save_loglikelihood(file_url, loglikelihood):
    with open(file_url, 'w') as f:
        for item in loglikelihood:
            string = item + '=>' + str(loglikelihood[item])
            f.write(string+'\n')

#save log prior     
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

def get_logprior(url):
    logprior = 0
    with open(url) as f:
        for line in f:
            logprior = float(line.strip())
    return logprior

'''
#main method is just to verify the upper methods
def main():
    pos, neg = read_data('data.json')
    #print("Positive reviews : " ,len(pos))
    #print("Negative reviews : ", len(neg))
'''