# myanmar_movie_review_sentiment_analysis
Myanmar Movie Sentiment Analysis with Naive Bayes Classifier

## Project
> It is NLP project with machine learning alogorithm, Naive Bayes. It will classify movie review sentiments written in myanmar language. After I have completed NLP specialization of DeepLearning.ai, I always want to try sentiment analysis with myanmar language which is still in research area and have low resources for training. However, it has some progresses like myWord segmentation that I used in this project to segment words.

## Data Collection
> As I already mentioned, myanmar nlp field has low resources. So, I collected movie review comments from social media apps like facebook, the most widely used app in our country. 

## Word Segmentation
> In Myanmar language, words are not separated with spaces like English. So, in the earlier days, it is very challenge for myanmar researchers in which they mostly used traditional longest syllable matching technique. 
I used Dr Ye Kyaw Thu's myWord segmentation tool to extract words from sentences. This tool used viterbi algorithm to segment words. 

>Github Link <a href='https://github.com/ye-kyaw-thu/myWord'>https://github.com/ye-kyaw-thu/myWord</a>

### Requirements to run myWord
> This tool can also be used to segment not only words but also phrases and syllable. This tool saves words in a given file. But I need words as python list so I changed a little bit in the tool. As Dr Ye Kyaw Thu mentioned in his github repository, we need to combine all small files before using this tool. So enter the dict_ver1 folder and run this command $bash ./combine-all-splitted-files.sh
