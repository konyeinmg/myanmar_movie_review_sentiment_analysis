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
#print(accuracy)

#save loglikelihood
services.save_loglikelihood('loglikelihood.txt', loglikelihood)

#save logprioro
services.save_logprior('logprior.txt', logprior)


    