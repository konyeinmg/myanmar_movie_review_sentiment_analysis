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

result = 0.0
for review,label in zip(test_x,test_y):
    output = 1 if naivebayes.predict(review, logprior, loglikelihood) > 0 else 0
    if label == output:
        result += 1
accuracy = (result / len(test_x)) * 100
print(accuracy) 
    