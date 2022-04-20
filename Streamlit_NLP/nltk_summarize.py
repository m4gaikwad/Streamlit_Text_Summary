# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 12:51:08 2022

@author: Mayur
"""

import nltk

from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
nltk.download('stopwords')
nltk.download('punkt')

# Please visit https://stackabuse.com/text-summarization-with-nltk-in-python/

from heapq import nlargest

def word_freq(tokens,stop_words,punctuation):
    punctuation = punctuation + '\n'
    word_frequencies = {}
    for word in tokens:
        if word.lower() not in stop_words:
            if word.lower() not in punctuation:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1
    
    max_frequency = max(word_frequencies.values())
        
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency
    
    return word_frequencies

def sent_score(sent_token,word_frequencies):
    sentence_scores = {}
    # for sent in sent_token:
    #     sentence = sent.split(" ")
    #     for word in sentence:
    #         if word.lower() in word_frequencies.keys():
    #             if sent not in sentence_scores.keys():
    #                 sentence_scores[word] = word_frequencies[word.lower()]
    #             else:
    #                 sentence_scores[word] += word_frequencies[word.lower()]
    for sent in sent_token:
        for word in word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
    return sentence_scores

def sentence_summary(sent_token,sentence_scores):
    select_length = int(len(sent_token)*30)
    heap_summary = nlargest(select_length,sentence_scores, key = sentence_scores.get)
    word_summary = [word for word in heap_summary]
    summary = ' '.join(word_summary)
    return summary


def nltk_summarize(raw_text):
    stop_words = stopwords.words('english')
    tokens = word_tokenize(raw_text)
    sent_token = sent_tokenize(raw_text)
    word_frequencies = word_freq(tokens, stop_words, punctuation)
    sentence_scores = sent_score(sent_token,word_frequencies)
    raw_text_summary = sentence_summary(sent_token,sentence_scores)
    return raw_text_summary
    

    
    