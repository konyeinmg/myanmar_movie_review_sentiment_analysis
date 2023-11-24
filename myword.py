"""

This code is updated version of this: https://gist.github.com/markdtw/e2a4e2ee7cef8ea6aed33bb47a97fba6
Ye Kyaw Thu, LST, NECTEC, Thailand updated followings:
-- added recursion limit
-- changed P_unigram and P_bigram as module level global variable
-- using binary ngram dictionary
--  set N value of this: "def __init__(self, datafile=None, unigram=True, N=102490):"
-- Last Updated: 5 Sept 2021

# References:
- Python implementation of Viterbi algorithm for word segmentation: 
- Updated version of this: https://gist.github.com/markdtw/e2a4e2ee7cef8ea6aed33bb47a97fba6
- A clean-up of this: http://norvig.com/ngrams/ch14.pdf
- For recursion limit: https://www.geeksforgeeks.org/python-handling-recursion-limit/
- A. Viterbi, "Error bounds for convolutional codes and an asymptotically optimum decoding algorithm," in IEEE Transactions on Information Theory, vol. 13, no. 2, pp. 260-269, April 1967, doi: 10.1109/TIT.1967.1054010.

"""


import wordsegment as wseg
import sys

uni_dict_bin = './dict_ver1/unigram-word.bin'
bi_dict_bin = './dict_ver1/bigram-word.bin'      

def count_prob():  
    wseg.P_unigram = wseg.ProbDist(uni_dict_bin, True)
    wseg.P_bigram = wseg.ProbDist(bi_dict_bin, False)

def words(line):
    listString = wseg.viterbi(line.replace(" ", "").strip()) # remove space between words and pass to viterbi()
    return listString[1]
