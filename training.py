import services
import preprocess
import naivebayes

pos,neg = services.read_data('data.json')

train_x, test_x, train_y, test_y = services.train_test_split(0.75, pos, neg)
#print(len(train_x))
#print(len(test_x))

freqs = naivebayes.count_words(train_x, train_y)
logprior, loglikelihood = naivebayes.train(freqs, train_x, train_y)
#print(loglikelihood)

pred_y = []
for review in test_x:
    pred_y += [1 if naivebayes.predict(review, logprior, loglikelihood) > 0 else 0]

accuracy = services.accuracy(test_y, pred_y)
precision, recall = services.precision_recall(test_y, pred_y)
f1_score = 2 * ((precision * recall) / (precision + recall))
'''
print('Accuracy : ', accuracy)
print('Precision : ', precision)
print('Recall : ', recall)
print('F1 Score : ', f1_score)
'''

#save loglikelihood
services.save_loglikelihood('loglikelihood.txt', loglikelihood)

#save logprioro
services.save_logprior('logprior.txt', logprior)


    