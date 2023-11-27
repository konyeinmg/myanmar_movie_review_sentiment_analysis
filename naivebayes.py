import preprocess
import numpy as np

def count_words(data, y):
    result = dict()
    for y,sentence in zip(y, data):
        for word in preprocess.segment_words(sentence):
            pair = (word, y)
            
            if pair in result:
                result[pair] += 1
            else: result[pair] = 1

    return result 

def train(counts, X, y):
    loglikelihood = {}
    logprior = 0

    words = set(pair[0] for pair in counts.keys())
    V = len(words)

    N_pos = N_neg = V_pos = V_neg = 0
    for pair in counts:
        if pair[1] > 0:
            V_pos += 1
            N_pos += counts[pair]
        else:
            V_neg += 1
            N_neg += counts[pair]
    
    D = len(y)
    D_pos = len([item for item in y if item > 0])
    D_neg = D - D_pos
    logprior = np.log(D_pos) - np.log(D_neg)

    for word in words:
        freq_pos = counts.get((word,1), 0)
        freq_neg = counts.get((word,0), 0)

        p_w_pos = (freq_pos + 1) / (N_pos + V)
        p_w_neg = (freq_neg + 1) / (N_neg + V)

        loglikelihood[word] = np.log(p_w_pos/p_w_neg)
    
    return logprior, loglikelihood


def predict(review, logprior, loglikelihood, log=False):
    words = preprocess.segment_words(review)
   
    p = 0
    p += logprior

    for word in words:
        if word in loglikelihood:
            p += loglikelihood[word]
            if log:
                print(word + ' : ' + str(loglikelihood[word]))
    
    if log:
        print('Probability : ', p)
    return p



'''
#main method is just to verify upper methods
def main():
    data = ["ဇာတ်လမ်းကချာတယ်",
            "တကယ် ချာချက်",
            "ဇာတ်လမ်းအစမှာထဲက ကိုမကြိုက်တာ:(",
            "နောက်ဆုံးခန်းကြီးက ရုပ်ပေါက်လွန်းပါတယ်",
            "စောက်ပေါကားကြီး:/",
            "မြန်မာဇာတ်လမ်းတွဲတွေလဲ သူ့ဟာနဲ့သူ ပိုပိုပြီးကောင်းလာနေတာကို",
            "ကြည့်ပြီးပြီငိုလိုက်ရတာအရမ်းပဲတစ်ကားလုံး Notting Hill ပြီးရင်ဒီကားကိုအကြိုက်ဆုံးပဲ❤️",
            "စောင်ရမ်းမိုက်လွန်းပါတယ်❤",
            "အရမ်းမိုက်တယ်။👍👍👍",
            "ကြည့်ရတာ တန်သွားပြီ",]
    y = [0,0,0,0,0,1,1,1,1,1]
    result = count_words(data, y)
    logprior, loglikelihood = train(result, data, y)
    sentence = 'မိုက် ကြိုက် တန် ပို'
    result = predict(sentence, logprior, loglikelihood)
    print(sentence + ' : ' + str(result))

main()
'''
