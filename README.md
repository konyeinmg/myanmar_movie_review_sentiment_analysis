# myanmar_movie_review_sentiment_analysis
Myanmar Movie Sentiment Analysis with Naive Bayes Classifier

## Project
> It is NLP project with machine learning algorithm, Naive Bayes. It will classify movie review sentiments written in myanmar language. After I have completed NLP specialization of DeepLearning.ai, I always want to try sentiment analysis with myanmar language which is still in research area and have low resources for training. However, it has some progresses like myWord segmentation that I used in this project to segment words.

## Data Collection
> As I already mentioned, myanmar nlp field has low resources. So, I collected movie review comments from social media apps like facebook, the most widely used app in our country. 

## Word Segmentation
> In Myanmar language, words are not separated with spaces like English. So, in the earlier days, it is very challenge for myanmar researchers in which they mostly used traditional longest syllable matching technique. 
I used Dr Ye Kyaw Thu's myWord segmentation tool to extract words from sentences. This tool used viterbi algorithm to segment words. 

>Github Link <a href='https://github.com/ye-kyaw-thu/myWord'>https://github.com/ye-kyaw-thu/myWord</a>

### Requirements to run myWord
> This tool can be used to segment not only words but also phrases and syllables. This tool saves words in a given file. But I need words as python list so I changed a little bit in the tool. As Dr Ye Kyaw Thu mentioned in his github repository, we need to combine all small files before using this tool. So enter the dict_ver1 folder and run this command $bash ./combine-all-splitted-files.sh

## Preprocessing
> I removed all english words, numbers and punctuations. But I intentionally left stickers and emotions in reviews because they have great impact on sentiment of reviews such as <3, xD, :|, etc..

### Removing Stopwords
> It is very challenge for me because I collected reviews from social media so there are too many informal words (idioms currently used in social medias). Actually these informal words are stopwords in formal written language. So if I remove all stopwords from review, sometimes it will return empty array. That is why I used another list of stopwords in removing unnessary words. You will see two stopword arrays in this project. I got stopword lists from this github repository <a href = 'https://github.com/chanmratekoko/Awesome-Myanmar-Wordlists-Dictionary-Collection'>https://github.com/chanmratekoko/Awesome-Myanmar-Wordlists-Dictionary-Collection/blob/master/myanmar-data/stopword-lists/stop_words.txt</a>

### For Myanmar only
> ကျွန်တော်ဒီနေရာမှာတစ်ချက်ပြောစရာရှိတာက ကျွန်တော်တို့မြန်မာစာမှာ formal language ရဲ့stopword တွေကို informal written မှာ ဖြုတ်လိုက်ရင် review တစ်ခုလုံးအကုန်ပါသွားသလောက်ပါပဲ ဥပမာဆိုကြပါစို့ "ဆက်တင်ကဖြစ်သလိုလုပ်ထားတာပဲ" ဆိုတဲ့ bad review ဆိုပါစို့ ဒီစာကြောင်းကိုသာ stopword removal လုပ်လိုက်ရင် empty array ပဲကျန်တော့တာပဲ ဒါကြောင့်မို့ ကျွန်တော်ရဲ့ proj မှာ stopword list နှစ်ခုမှာ stopword2 ကိုပဲယူသုံးထားတာပါ နောက်တစ်ခုက ဗန်းစကားအသုံးအနှုန်းတွေကို ဖြုတ်တာမှာလည်းနည်းနည်းပြဿနာရှိတာပါပဲ ဒီခေတ်မှာ review ရေးရင်ဘယ်သူမှတော့ စာစီစာကုံးရေးသလို formal ဆန်ဆန်ရေးတာ မရှိသလောက်ပါပဲ ဒီတော့ကာ အချို့informal words တွေဟာလည်း sentiment အတွက် အရေးပါနေပြန်ပါတယ် ဥပမာဆိုကြပါစို့ "မကောင်းဘူး"၊ "အဆင်မပြေဘူး"၊"မကြိုက်ဘူး" ဒီစာကြောင်းတွေမှာဆို 'မ' နဲ့ 'ဘူး' ဟာ အငြင်းဝါဒပါ ဒီတော့ကာ "ဘူး" ကို stopword ပါဆိုပြီး removal လုပ်မိရင် negative review တွေမှာ တော်တော်impactရှိသွားတာပါပဲ မြန်မာစကားပုံမှာ ဘူးတစ်လုံးခံအိုတောင်မဆင်းရဲ ဆိုပြီးလည်းရှိသားပါပဲ။ ဒါကြောင့် ဒီ project မှာ stopword ကို mutually သေချာစစ်ယူပြီးထပ်လုပ်ဖို့ရှိပါသေးတယ်

## Model
> I used Naive Bayes ML algorithm to classify sentiments. As I said above, this project is my very first project after completing NLP specialization of DeepLearing.ai. So I refer to this specialization for the theory and approach that I used to implement this project. I saved loglikelihood and logprior in text files and load these files to run classification.

## Application
> Just run index.py to classify movie review. You need to write myanmar font with Unicode. There is no support for Zawgyi font(former common font in myanmar keyboard). If you want to train or check how trained the model, you can trace training.py and naivebayes.py.
> As first step, this application is just giving input from command so as future work I would like to build GUI for better UX. 

## Metrics
<ul>
    <li>Accuracy : 68%</li>
    <li>Precision : 0.714</li>
    <li>Recall : 0.6</li>
    <li>F1 Score : 0.652</li>
</ul>

> As I mentioned above, Myanmar has low resources for NLP. So this model was trained with just 200 reviews that is why accuracy cannot go over 70%. As a future work, I will add more data for better accuracy.

## Pros
> It is literally simple. Even if you want to train another sentiment analysis such as cyberbullying detection, restaurant review, you just need to change data in json file.

## Cons
> Naive Bayes works with probabilities, not like deep learning models such as LSTM, RNN. Therefore, it does not provide the ture meaning of words. It just count probabilites according to our dataset. And I have just 200 reviews. So it has big impact on accuracy.

## Future Work 
<ul>
    <li>More data</li>
    <li>Stopword checking</li>
    <li>Evaluation</li>
    <li>GUI building</li>
</ul>

## Citation


## Reference