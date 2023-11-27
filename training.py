import numpy as np

import services
import preprocess
import naivebayes

pos,neg = services.read_data('data.json')

train_percent = 0.75

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

#print(len(train_x))
#print(len(test_x))

freqs = naivebayes.count_words(train_x, train_y)
logprior, loglikelihood = naivebayes.train(freqs, train_x, train_y)
#print(loglikelihood)

result = 0.0
for review,label in zip(test_x,test_y):
    output = 1 if naivebayes.predict(review, logprior, loglikelihood) > 0 else 0
    if label == output:
        result += 1
accuracy = (result / len(test_x)) * 100
print(accuracy) 
    