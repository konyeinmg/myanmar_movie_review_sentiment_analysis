from tkinter import *

import services
import naivebayes

def classify():
    string = text.get("1.0", END)
    if string:
        output = 1 if naivebayes.predict(string, logprior, loglikelihood) > 0 else 0
        result = 'Good Review' if output > 0 else 'Bad Review'
        label.config(text = result)


#load loglikelihood
loglikelihood = services.get_loglikelihood('loglikelihood.txt')

#load logprior
logprior = services.get_logprior('logprior.txt')

#print(loglikelihood)
#print(logprior)

string = input("Enter a movie review : ")
output = 1 if naivebayes.predict(string, logprior, loglikelihood, True) > 0 else 0
result = 'Good review' if output > 0 else 'Bad review'
print(result)
'''
root = Tk()
root.call('encoding', 'system', 'utf-8')
root.geometry('400x200')
root.title('Myanmar Movie Sentiment Analysis')

text = Text(root,width=100, height=8)
text.pack(padx = 5, pady=10)

button = Button(root, width=10, height=2, text='Classify', command=classify)
button.pack(pady = 10)

label = Label(root)
label.pack(pady = 10)

root.mainloop()
'''