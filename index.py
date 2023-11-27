import services
import naivebayes

#load loglikelihood
loglikelihood = services.get_loglikelihood('loglikelihood.txt')

#load logprior
logprior = services.get_logprior('logprior.txt')

#print(loglikelihood)
#print(logprior)
string = input("Enter a movie review : ")
output = 1 if naivebayes.predict(string, logprior, loglikelihood) > 0 else 0
result = 'Good review' if output > 0 else 'Bad review'
print(result)